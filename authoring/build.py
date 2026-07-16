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


def build(assignment_id):
    if assignment_id not in ASSIGNMENTS:
        raise SystemExit(f"unknown assignment {assignment_id!r}; have {sorted(ASSIGNMENTS)}")
    a = ASSIGNMENTS[assignment_id]
    public_qs, keys = [], {}

    for i, pid in enumerate(a["problems"], 1):
        if pid not in BANK:
            raise SystemExit(f"[{assignment_id}] problem {pid!r} is not in the bank")
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

    public = {"id": assignment_id, "title": a["title"], "intro": a.get("intro", ""), "questions": public_qs}
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
    lessons = [l for l in data.get("lessons", []) if l.get("id") != assignment_id]
    lessons.append({"id": assignment_id, "title": title})
    lessons.sort(key=lambda l: l["id"])
    idx.write_text(json.dumps({"lessons": lessons}, indent=2))


XP_BY_DIFF = {"starter": 5, "easy": 10, "medium": 20, "hard": 35}


def emit_challenges():
    """Publish every gradeable bank problem as a standalone practice challenge."""
    items = []
    for pid, p in BANK.items():
        if p["kind"] == "written":
            continue                                  # not auto-gradeable → not a challenge
        diff = p.get("difficulty", "easy")
        item = {"id": pid, "title": p.get("title", pid), "kind": p["kind"],
                "tags": p.get("tags", []), "difficulty": diff,
                "xp": p.get("xp", XP_BY_DIFF.get(diff, 10)), "prompt": p["prompt"]}
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
    targets = list(ASSIGNMENTS) if args.all else ([args.assignment] if args.assignment else [])
    if not targets and not args.bank:
        ap.error("give an assignment id, --all, or --bank")
    for aid in targets:
        lid, keys = build(aid)
        if args.push:
            if not args.token:
                raise SystemExit("--push requires --token")
            push_keys(lid, keys, args.push, args.token)
