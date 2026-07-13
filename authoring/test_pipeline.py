"""
test_pipeline.py — prove the grading pipeline end to end, in Python.

Builds the lesson_01 question list from the bank + assignment (the same way the
app gets it), then simulates CLIENT (run student code, normalize) → SERVER
(compare to the hidden keys). Asserts the three load-bearing properties:
  1. a correct solution passes every question,
  2. a wrong solution fails the right question,
  3. a HARD-CODED CONSTANT passes the visible example but FAILS overall.

Run:  python build.py lesson_01 && python test_pipeline.py
"""

import json
from pathlib import Path

import norm
from bankmd import BANK
from assignments import ASSIGNMENTS

KEYS = json.loads((Path(__file__).resolve().parent.parent / "keys" / "keys_lesson_01.json").read_text())["keys"]

# Reconstruct the positional q1..qn questions for lesson_01 from the bank.
QS = {}
for i, pid in enumerate(ASSIGNMENTS["lesson_01"]["problems"], 1):
    p = BANK[pid]
    QS[f"q{i}"] = {"id": f"q{i}", "kind": p["kind"], "entry": p.get("entry"), "inputs": p.get("inputs")}


def client_run_code_var(code, entry):
    ns = {}; exec(code, ns); return norm.normalize(ns[entry])


def client_run_code_fn(code, entry, inputs):
    ns = {}; exec(code, ns); fn = ns[entry]
    return [norm.normalize(fn(*args)) for args in inputs]


def grade(qid, answer):
    q, k = QS[qid], KEYS[qid]
    if q["kind"] == "code_var":
        return norm.compare(k["expected"], client_run_code_var(answer, q["entry"]), k["tol"])
    if q["kind"] == "code_fn":
        return norm.compare(k["expected"], client_run_code_fn(answer, q["entry"], q["inputs"]), k["tol"])
    if q["kind"] == "mcq":
        return answer == k["answer"]
    return None


passed = failed = 0
def check(label, got, want):
    global passed, failed
    ok = got == want
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}: got {got}, want {want}")
    passed += ok; failed += not ok


print("1) Correct solutions pass")
for qid, ans in {
    "q1": "a = 7\nb = 5\ntotal = a + b",
    "q2": "rem = 17 % 5",
    "q3": "def double(x):\n    return x * 2",
    "q4": "def area(length, width):\n    return length * width",
    "q5": "def is_even(n):\n    return n % 2 == 0",
    "q6": 1, "q7": 1,
}.items():
    check(f"{qid} correct", grade(qid, ans), True)

print("\n2) Wrong solutions fail")
check("q3 unfixed bug", grade("q3", "def double(x):\n    return x + 2"), False)
check("q4 wrong (l+w)", grade("q4", "def area(length, width):\n    return length + width"), False)
check("q6 wrong choice", grade("q6", 0), False)

print("\n3) Hard-coding the visible example fails on the varied inputs")
check("q4 hardcoded 12", grade("q4", "def area(length, width):\n    return 12"), False)
check("q3 hardcoded 8", grade("q3", "def double(x):\n    return 8"), False)

print(f"\n{'='*46}\n{passed} passed, {failed} failed")
raise SystemExit(1 if failed else 0)
