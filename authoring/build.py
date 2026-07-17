"""
build.py — turn a SELECTION of bank problems (an assignment) into the public
lesson file + secret keys the app uses.

    python build.py lesson_01                         # build one assignment
    python build.py lesson_01 --push <url> --token T  # ...and upload its keys
    python build.py --all --push <url> --token T      # build every assignment
    python build.py --bank                            # emit bank.json for builder.html

An assignment (assignments.py) is just an ordered list of problem ids from the
bank (bank.py). Questions are numbered q1..qn in that order, so the app + grader
format is unchanged — only the authoring is now bank + selection.
"""

import argparse
import importlib
import json
import urllib.request
from pathlib import Path

import norm
import refmd
from bankmd import BANK
from assignments import ASSIGNMENTS

HERE = Path(__file__).resolve().parent
PUBLIC_DIR = HERE.parent / "lessons"
KEYS_DIR = HERE.parent / "keys"


def expected_for_code_fn(p, qid):
    ref = p["reference"]; out = []
    for args in p["inputs"]:
        try: out.append(norm.normalize(ref(*args)))
        except Exception as e:  # noqa: BLE001
            raise SystemExit(f"[{qid}] reference failed on input {args}: {e}")
    return out


def expected_for_code_var(p, qid):
    ns = {}
    exec(p["reference"], ns)  # noqa: S102 -- author-trusted reference
    if p["entry"] not in ns:
        raise SystemExit(f"[{qid}] reference did not define {p['entry']!r}")
    return norm.normalize(ns[p["entry"]])


def check_unit(assignment_id, a):
    """An assignment cannot cover less material than its own problems need — that
    would unlock practice for a unit whose homework hasn't been released."""
    needed = max((unit_of(BANK[pid]) for pid in a["problems"]), default=1)
    if a.get("unit", 1) < needed:
        worst = [pid for pid in a["problems"] if unit_of(BANK[pid]) == needed]
        raise SystemExit(
            f"[{assignment_id}] says unit={a.get('unit', 1)} but contains {worst[0]!r}, "
            f"which needs unit {needed} ({UNIT_NAMES[needed]}). Either raise the "
            f"assignment's unit to {needed} or drop that problem.")


def build(assignment_id):
    if assignment_id not in ASSIGNMENTS:
        raise SystemExit(f"unknown assignment {assignment_id!r}; have {sorted(ASSIGNMENTS)}")
    a = ASSIGNMENTS[assignment_id]
    public_qs, keys = [], {}

    for pid in a["problems"]:
        if pid not in BANK:
            raise SystemExit(f"[{assignment_id}] problem {pid!r} is not in the bank")

    # mode="challenges": the assignment is just an ordered list of practice
    # challenges. Students solve each on its own; there's no single submit, and no
    # keys to hide — the challenge already carries its own grading.
    if a.get("mode") == "challenges":
        for pid in a["problems"]:
            if BANK[pid]["kind"] == "written":
                raise SystemExit(
                    f"[{assignment_id}] {pid!r} is a written question, which can't check "
                    f"itself — a challenge-series assignment needs auto-gradable problems.")
        check_unit(assignment_id, a)
        public = {"id": assignment_id, "title": a["title"], "intro": a.get("intro", ""),
                  "unit": a.get("unit", 1), "mode": "challenges", "challenges": list(a["problems"])}
        PUBLIC_DIR.mkdir(exist_ok=True)
        (PUBLIC_DIR / f"{assignment_id}.json").write_text(json.dumps(public, indent=2))
        update_manifest(assignment_id, a["title"])
        print(f"built {assignment_id}: {len(a['problems'])} challenges (series, self-checking)")
        return assignment_id, {}

    for i, pid in enumerate(a["problems"], 1):
        p = BANK[pid]
        qid = f"q{i}"
        kind = p["kind"]
        if kind == "code_var":
            keys[qid] = {"kind": kind, "expected": expected_for_code_var(p, qid), "tol": p.get("tol", 1e-6)}
            public_qs.append({"id": qid, "kind": kind, "prompt": p["prompt"], "starter": p["starter"], "entry": p["entry"]})
        elif kind == "code_fn":
            keys[qid] = {"kind": kind, "expected": expected_for_code_fn(p, qid), "tol": p.get("tol", 1e-6)}
            public_qs.append({"id": qid, "kind": kind, "prompt": p["prompt"], "starter": p["starter"],
                              "entry": p["entry"], "inputs": p["inputs"]})
        elif kind == "mcq":
            keys[qid] = {"kind": kind, "answer": p["answer"]}
            public_qs.append({"id": qid, "kind": kind, "prompt": p["prompt"], "choices": p["choices"]})
        elif kind == "written":
            public_qs.append({"id": qid, "kind": kind, "prompt": p["prompt"]})
        else:
            raise SystemExit(f"[{qid}] unknown kind {kind!r}")

    check_unit(assignment_id, a)
    public = {"id": assignment_id, "title": a["title"], "intro": a.get("intro", ""),
              "unit": a.get("unit", 1), "questions": public_qs}
    # VIABILITY MODE: ship the answer keys so the browser can grade (soft-hidden).
    # To re-hide, drop this line and grade server-side via GRADER_URL instead.
    public["grade"] = keys

    PUBLIC_DIR.mkdir(exist_ok=True); KEYS_DIR.mkdir(exist_ok=True)
    (PUBLIC_DIR / f"{assignment_id}.json").write_text(json.dumps(public, indent=2))
    (KEYS_DIR / f"keys_{assignment_id}.json").write_text(json.dumps({"lesson": assignment_id, "keys": keys}, indent=2))
    update_manifest(assignment_id, a["title"])

    n_auto = sum(1 for q in public_qs if q["kind"].startswith("code") or q["kind"] == "mcq")
    print(f"built {assignment_id}: {len(public_qs)} questions ({n_auto} auto-graded) from bank")
    return assignment_id, keys


def update_manifest(assignment_id, title):
    idx = PUBLIC_DIR / "index.json"
    data = {"lessons": []}
    if idx.exists():
        try: data = json.loads(idx.read_text())
        except Exception: pass
    a = ASSIGNMENTS[assignment_id]
    lessons = [l for l in data.get("lessons", []) if l.get("id") != assignment_id]
    entry = {"id": assignment_id, "title": title,
             "unit": a.get("unit", 1), "open": bool(a.get("open", False))}
    if a.get("mode") == "challenges":
        # ship the list so the app can show progress without fetching the lesson
        entry["mode"] = "challenges"
        entry["challenges"] = list(a["problems"])
    lessons.append(entry)
    lessons.sort(key=lambda l: (l.get("unit", 1), l["id"]))
    # The gate: the furthest unit any OPEN assignment reaches. Everything up to
    # there is unlocked — an assignment covering unit 3 has necessarily taught
    # units 1-2, whether or not their own assignments are open yet.
    reached = [l["unit"] for l in lessons if l.get("open")]
    max_open = max(reached) if reached else 0
    by_unit = sorted(lessons, key=lambda l: l["unit"])
    units = []
    for n, name, _ in UNITS:
        # for a locked unit, name the assignment that will unlock it, so the app
        # can tell a student WHY something is locked instead of just hiding it
        nxt = next((l for l in by_unit if l["unit"] >= n), None)
        units.append({"n": n, "name": name, "open": n <= max_open,
                      "opens_with": None if n <= max_open or not nxt else nxt["title"]})
    idx.write_text(json.dumps({"lessons": lessons, "units": units,
                               "max_open_unit": max_open}, indent=2))


XP_BY_DIFF = {"starter": 5, "easy": 10, "medium": 20, "hard": 35}

# ---------------------------------------------------------------- curriculum
# The course in order. A unit is a body of material; an assignment declares the
# unit it covers and whether it is open yet (see assignments.py). Practice
# challenges unlock with the material: when the assignment covering unit N is
# open, students get every challenge in units 1..N.
UNITS = [
    (1, "Variables & math", {"language_fundamentals", "math", "numbers", "algebra", "geometry", "types"}),
    (2, "Strings", {"strings", "formatting", "indexing"}),
    (3, "Functions", {"functions"}),
    # booleans are separate from if/elif/else on purpose: returning a comparison
    # (is_even) is not the same skill as branching
    (4, "Booleans & comparisons", {"logic", "validation"}),
    (5, "If / else", {"conditions"}),
    (6, "Lists", {"arrays", "sorting"}),
    (7, "Loops", {"loops"}),
    (8, "Dictionaries", {"dicts"}),
]
UNIT_NAMES = {n: name for n, name, _ in UNITS}
# These describe a problem's SHAPE, not the skill it needs, so they say nothing
# about when it unlocks.
META_TAGS = {"bugs", "concept", "predict", "written", "algorithms"}


def unit_of(p):
    """Which unit a problem belongs to: the LATEST skill it needs.

    A problem can't be attempted until everything it uses has been taught, so the
    most advanced tag wins. An explicit `unit:` in the bank overrides this.
    """
    if p.get("unit"):
        return p["unit"]
    tags = {t for t in p.get("tags", []) if t not in META_TAGS}
    hits = [n for n, _, unit_tags in UNITS if tags & unit_tags]
    return max(hits) if hits else 1


def emit_challenges():
    """Publish every gradeable bank problem as a standalone practice challenge."""
    pages = refmd.load()
    items = []
    for pid, p in BANK.items():
        if p["kind"] == "written":
            continue                                  # not auto-gradeable → not a challenge
        diff = p.get("difficulty", "easy")
        item = {"id": pid, "title": p.get("title", pid), "kind": p["kind"],
                "tags": p.get("tags", []), "difficulty": diff, "unit": unit_of(p),
                "xp": p.get("xp", XP_BY_DIFF.get(diff, 10)), "prompt": p["prompt"]}
        see = resolve_see(p, pid, pages)
        if see:
            item["see"] = see
        if p.get("walkthrough"):
            item["walkthrough"] = p["walkthrough"]
        if p["kind"] == "code_var":
            item["starter"] = p["starter"]; item["entry"] = p["entry"]
            item["grade"] = {"kind": "code_var", "expected": expected_for_code_var(p, pid),
                             "tol": p.get("tol", 1e-6)}
        elif p["kind"] == "code_fn":
            item["starter"] = p["starter"]; item["entry"] = p["entry"]; item["inputs"] = p["inputs"]
            item["grade"] = {"kind": "code_fn", "expected": expected_for_code_fn(p, pid),
                             "tol": p.get("tol", 1e-6)}
        elif p["kind"] == "mcq":
            item["choices"] = p["choices"]
            item["grade"] = {"kind": "mcq", "answer": p["answer"]}
        items.append(item)
    PUBLIC_DIR.mkdir(exist_ok=True)
    (PUBLIC_DIR / "challenges.json").write_text(json.dumps({"challenges": items}, indent=2))
    print(f"wrote lessons/challenges.json  ({len(items)} practice challenges)")


def resolve_see(p, pid, pages):
    """Where a problem sends a student who wants to read up on it.

    An explicit `see:` wins and must resolve; otherwise fall back to the page for
    the problem's unit. Returns None if that unit has no page yet.
    """
    by_unit = {pg["unit"]: pg for pg in pages}
    want = p.get("see")
    if want:
        page_id, _, anchor = want.partition("#")
        page = next((pg for pg in pages if pg["id"] == page_id), None)
        if not page:
            raise SystemExit(f"[{pid}] see: {want!r} — no reference page {page_id!r}. "
                             f"Run `python refmd.py --anchors` for the real targets.")
        if anchor and anchor not in page["anchors"]:
            raise SystemExit(f"[{pid}] see: {want!r} — {page_id!r} has no section {anchor!r}. "
                             f"Run `python refmd.py --anchors` for the real targets.")
        if page["unit"] > unit_of(p):
            raise SystemExit(f"[{pid}] see: {want!r} points at unit {page['unit']} material, "
                             f"but the problem is unit {unit_of(p)} — a student would be sent "
                             f"to a page they can't open yet.")
        return {"page": page_id, "anchor": anchor or None, "title": page["title"]}
    page = by_unit.get(unit_of(p))
    return {"page": page["id"], "anchor": None, "title": page["title"]} if page else None


def emit_reference():
    """Publish the topic explainers. Each page names its unit, so it stays hidden
    until the homework covering that section is released — same gate as practice."""
    pages = refmd.load()
    known = {n for n, _, _ in UNITS}
    for p in pages:
        if p["unit"] not in known:
            raise SystemExit(f"[{p['id']}] unit {p['unit']} is not a course section {sorted(known)}")
        p["unit_name"] = UNIT_NAMES[p["unit"]]
    PUBLIC_DIR.mkdir(exist_ok=True)
    (PUBLIC_DIR / "reference.json").write_text(json.dumps({"pages": pages}, indent=2))
    print(f"wrote lessons/reference.json  ({len(pages)} topic pages)")


def emit_bank_json():
    """Public metadata for every bank problem, for the visual builder (no answers)."""
    items = []
    for pid, p in BANK.items():
        items.append({"id": pid, "title": p.get("title", pid), "kind": p["kind"],
                      "tags": p.get("tags", []), "difficulty": p.get("difficulty", ""),
                      "prompt": p["prompt"]})
    payload = {"problems": items}
    (HERE / "bank.json").write_text(json.dumps(payload, indent=2))
    # bank.js lets builder.html open directly from disk (file://) without a server
    (HERE / "bank.js").write_text("window.BANK_DATA = " + json.dumps(payload) + ";")
    print(f"wrote bank.json + bank.js  ({len(items)} problems) — open builder.html to compose assignments")


def push_keys(lesson_id, keys, url, token):
    payload = json.dumps({"action": "set_keys", "token": token, "lesson": lesson_id, "keys": keys}).encode()
    req = urllib.request.Request(url, data=payload, headers={"Content-Type": "text/plain;charset=utf-8"})
    with urllib.request.urlopen(req, timeout=30) as r:
        resp = json.loads(r.read().decode())
    if not resp.get("ok"):
        raise SystemExit(f"key push rejected: {resp}")
    print(f"  keys pushed to grader ({'updated' if resp.get('updated') else 'added'} {lesson_id})")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Build assignments from the problem bank.")
    ap.add_argument("assignment", nargs="?", help="assignment id (from assignments.py)")
    ap.add_argument("--all", action="store_true", help="build every assignment")
    ap.add_argument("--bank", action="store_true", help="emit bank.json for the visual builder")
    ap.add_argument("--push", metavar="GRADER_URL", help="also upload keys to the Apps Script grader")
    ap.add_argument("--token", help="admin token (matches the grader's ADMIN_TOKEN)")
    args = ap.parse_args()

    if args.bank:
        emit_bank_json()
    emit_challenges()          # practice challenges are always kept in sync with the bank
    emit_reference()           # ...and so are the topic explainers
    targets = list(ASSIGNMENTS) if args.all else ([args.assignment] if args.assignment else [])
    if not targets and not args.bank:
        ap.error("give an assignment id, --all, or --bank")
    for aid in targets:
        lid, keys = build(aid)
        if args.push:
            if not args.token:
                raise SystemExit("--push requires --token")
            push_keys(lid, keys, args.push, args.token)
