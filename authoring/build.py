"""
build.py -- split one authored lesson into a PUBLIC file and a SECRET key file.

    python build.py lesson_01

Produces:
  ../lessons/lesson_01.json   PUBLIC  -> commit to the GitHub Pages repo.
                              Contains prompts, starter code, grading inputs,
                              and MCQ choice TEXT. No expected outputs, no MCQ
                              answer index, no reference solutions.
  ../keys/keys_lesson_01.json SECRET  -> pushed to the Apps Script "Keys" tab
                              (see README). Contains expected outputs + MCQ
                              answers. NEVER commit this; it's gitignored.

The expected answers are computed by running your reference solutions through
norm.normalize(), the exact function the student's browser will use -- so the
author side and the grade side are guaranteed to agree.
"""

import argparse
import importlib
import json
import urllib.request
from pathlib import Path

import norm

HERE = Path(__file__).resolve().parent
PUBLIC_DIR = HERE.parent / "lessons"
KEYS_DIR = HERE.parent / "keys"


def expected_for_code_fn(q):
    """Run the reference function on each input list; normalize each output."""
    ref = q["reference"]
    out = []
    for args in q["inputs"]:
        try:
            out.append(norm.normalize(ref(*args)))
        except Exception as e:  # noqa: BLE001
            raise SystemExit(
                f"[{q['id']}] reference solution failed on input {args}: {e}"
            )
    return out


def expected_for_code_var(q):
    """Exec the reference code; normalize the entry variable's value."""
    ns = {}
    exec(q["reference"], ns)  # noqa: S102 -- author-trusted reference code
    if q["entry"] not in ns:
        raise SystemExit(f"[{q['id']}] reference did not define {q['entry']!r}")
    return norm.normalize(ns[q["entry"]])


def build(lesson_module_name):
    lesson = importlib.import_module(lesson_module_name).LESSON
    public_qs, keys = [], {}

    for q in lesson["questions"]:
        kind = q["kind"]
        if kind == "code_var":
            keys[q["id"]] = {"kind": kind, "expected": expected_for_code_var(q),
                             "tol": q.get("tol", 1e-6)}
            public_qs.append({"id": q["id"], "kind": kind, "prompt": q["prompt"],
                              "starter": q["starter"], "entry": q["entry"]})
        elif kind == "code_fn":
            keys[q["id"]] = {"kind": kind, "expected": expected_for_code_fn(q),
                             "tol": q.get("tol", 1e-6)}
            public_qs.append({"id": q["id"], "kind": kind, "prompt": q["prompt"],
                              "starter": q["starter"], "entry": q["entry"],
                              "inputs": q["inputs"]})   # inputs public; outputs hidden
        elif kind == "mcq":
            keys[q["id"]] = {"kind": kind, "answer": q["answer"]}
            public_qs.append({"id": q["id"], "kind": kind, "prompt": q["prompt"],
                              "choices": q["choices"]})   # no answer index
        elif kind == "written":
            public_qs.append({"id": q["id"], "kind": kind, "prompt": q["prompt"]})
        else:
            raise SystemExit(f"[{q['id']}] unknown kind {kind!r}")

    public = {"id": lesson["id"], "title": lesson["title"],
              "intro": lesson.get("intro", ""), "questions": public_qs}

    PUBLIC_DIR.mkdir(exist_ok=True)
    KEYS_DIR.mkdir(exist_ok=True)
    pub_path = PUBLIC_DIR / f"{lesson['id']}.json"
    key_path = KEYS_DIR / f"keys_{lesson['id']}.json"
    pub_path.write_text(json.dumps(public, indent=2))
    key_path.write_text(json.dumps({"lesson": lesson["id"], "keys": keys}, indent=2))

    update_manifest(lesson["id"], lesson["title"])

    n_auto = sum(1 for q in lesson["questions"] if q["kind"].startswith("code") or q["kind"] == "mcq")
    print(f"built {lesson['id']}: {len(public_qs)} questions ({n_auto} auto-graded)")
    print(f"  PUBLIC -> {pub_path}")
    print(f"  SECRET -> {key_path}  (do not commit)")
    print(f"  MANIFEST updated -> {PUBLIC_DIR / 'index.json'}")
    return lesson["id"], keys


def update_manifest(lesson_id, title):
    """Keep lessons/index.json in sync so the app's lesson picker sees this lesson."""
    idx = PUBLIC_DIR / "index.json"
    data = {"lessons": []}
    if idx.exists():
        try: data = json.loads(idx.read_text())
        except Exception: pass
    lessons = [l for l in data.get("lessons", []) if l.get("id") != lesson_id]
    lessons.append({"id": lesson_id, "title": title})
    lessons.sort(key=lambda l: l["id"])
    idx.write_text(json.dumps({"lessons": lessons}, indent=2))


def push_keys(lesson_id, keys, url, token):
    """Upload the hidden keys to the Apps Script grader (no service account)."""
    payload = json.dumps({"action": "set_keys", "token": token,
                          "lesson": lesson_id, "keys": keys}).encode()
    req = urllib.request.Request(url, data=payload,
                                 headers={"Content-Type": "text/plain;charset=utf-8"})
    with urllib.request.urlopen(req, timeout=30) as r:
        resp = json.loads(r.read().decode())
    if not resp.get("ok"):
        raise SystemExit(f"key push rejected: {resp}")
    print(f"  KEYS pushed to grader ({'updated' if resp.get('updated') else 'added'} {lesson_id})")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Build a lesson into public + secret files.")
    ap.add_argument("lesson", nargs="?", default="lesson_01", help="lesson module name")
    ap.add_argument("--push", metavar="GRADER_URL", help="also upload keys to the Apps Script grader")
    ap.add_argument("--token", help="admin token (must match the grader's ADMIN_TOKEN)")
    args = ap.parse_args()
    lid, keys = build(args.lesson)
    if args.push:
        if not args.token:
            raise SystemExit("--push requires --token")
        push_keys(lid, keys, args.push, args.token)
