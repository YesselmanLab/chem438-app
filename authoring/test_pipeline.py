"""
test_pipeline.py -- prove the grading pipeline end to end, in Python.

Simulates what really happens across the wire:
  * CLIENT (Pyodide): runs the student's code, produces + normalizes outputs.
  * SERVER (Apps Script): compares those outputs to the hidden expected keys.

We assert the three properties the whole design rests on:
  1. a correct solution passes every question,
  2. a wrong solution fails the right question,
  3. a HARD-CODED CONSTANT passes the visible example but FAILS overall, because
     the varied grading inputs need varied outputs (the anti-cheating claim).

Run:  python test_pipeline.py
"""

import json
from pathlib import Path

import norm
from lesson_01 import LESSON

KEYS = json.loads((Path(__file__).resolve().parent.parent / "keys" / "keys_lesson_01.json").read_text())["keys"]


def client_run_code_var(student_code, entry):
    ns = {}
    exec(student_code, ns)  # noqa: S102 -- simulates Pyodide running student code
    return norm.normalize(ns[entry])


def client_run_code_fn(student_code, entry, inputs):
    ns = {}
    exec(student_code, ns)  # noqa: S102
    fn = ns[entry]
    return [norm.normalize(fn(*args)) for args in inputs]


def grade_question(q, student_code_or_choice):
    """Return True/False the way the server would."""
    k = KEYS[q["id"]]
    if q["kind"] == "code_var":
        got = client_run_code_var(student_code_or_choice, q["entry"])
        return norm.compare(k["expected"], got, k["tol"])
    if q["kind"] == "code_fn":
        got = client_run_code_fn(student_code_or_choice, q["entry"], q["inputs"])
        return norm.compare(k["expected"], got, k["tol"])
    if q["kind"] == "mcq":
        return student_code_or_choice == k["answer"]
    return None  # written: not auto-graded


def qget(qid):
    return next(q for q in LESSON["questions"] if q["id"] == qid)


passed = 0
failed = 0

def check(label, got, want):
    global passed, failed
    ok = got == want
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}: got {got}, want {want}")
    passed += ok
    failed += not ok


print("1) A correct solution passes every auto-graded question")
correct = {
    "q1": "a = 7\nb = 5\ntotal = a + b",
    "q2": "rem = 17 % 5",
    "q3": "def double(x):\n    return x * 2",
    "q4": "def area(length, width):\n    return length * width",
    "q5": "def is_even(n):\n    return n % 2 == 0",
    "q6": 1,
    "q7": 1,
}
for qid, ans in correct.items():
    check(f"{qid} correct", grade_question(qget(qid), ans), True)

print("\n2) Wrong solutions fail the right question")
check("q3 unfixed bug (x+2)", grade_question(qget("q3"), "def double(x):\n    return x + 2"), False)
check("q4 wrong (l+w)", grade_question(qget("q4"), "def area(length, width):\n    return length + width"), False)
check("q5 wrong (always True)", grade_question(qget("q5"), "def is_even(n):\n    return True"), False)
check("q6 wrong choice", grade_question(qget("q6"), 0), False)

print("\n3) Hard-coding the visible example FAILS on the varied grading inputs")
# q4's first grading input is [3,4] -> 12. A cheater hardcodes 12.
check("q4 hardcoded 12 (passes only [3,4])",
      grade_question(qget("q4"), "def area(length, width):\n    return 12"), False)
# q3's first input is [4] -> 8. Hardcode 8.
check("q3 hardcoded 8", grade_question(qget("q3"), "def double(x):\n    return 8"), False)
# sanity: the cheater DOES pass if there were only the one visible case
single = norm.compare([norm.normalize(12)], client_run_code_fn("def area(l,w):\n return 12", "area", [[3,4]]), 1e-6)
check("(sanity) hardcoded WOULD pass with only 1 input", single, True)

print("\n4) Float tolerance works")
check("float 0.1+0.2 vs 0.3", norm.compare(0.3, 0.1 + 0.2), True)

print("\n5) Non-whitelisted output is rejected at author time")
try:
    norm.normalize({"a": 1})
    check("dict rejected", False, True)
except TypeError:
    check("dict rejected", True, True)

print(f"\n{'='*50}\n{passed} passed, {failed} failed")
raise SystemExit(1 if failed else 0)
