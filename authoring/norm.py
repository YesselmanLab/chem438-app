"""
norm.py -- the normalization + comparison contract (the source of truth).

This is the piece that guarantees author-time and grade-time can never disagree.
The SAME normalize() runs in two places:
  1. build.py (here, at authoring time) turns each reference solution's outputs
     into the hidden "expected" values.
  2. The student's browser (Pyodide) runs the identical normalize() on their
     code's outputs before sending them.
So both sides speak the same canonical form. The server (Apps Script) only has
to compare already-normalized values with compare() -- which is mirrored in
grader.gs. If you change either function, change both.

Autograded outputs are restricted to a safe whitelist: int, float, str, bool,
None, and lists/tuples of those. dict/set/objects are rejected at AUTHOR time
(build.py fails loudly), never silently mis-graded on a student.
"""

from __future__ import annotations


def normalize(v):
    """Return a canonical, JSON-serializable form of an autograded output.

    Raises TypeError on anything outside the whitelist so bad questions are
    caught when the instructor builds the lesson, not when a student submits.
    """
    if isinstance(v, bool):
        return v                      # bool before int (True is an int in Python)
    if v is None or isinstance(v, (int, str)):
        return v
    if isinstance(v, float):
        # collapse -0.0 and integral floats deterministically
        return 0.0 if v == 0 else float(v)
    if isinstance(v, (list, tuple)):
        return [normalize(x) for x in v]
    raise TypeError(
        f"Output type {type(v).__name__!r} is not autogradable. "
        "Allowed: int, float, str, bool, None, list/tuple of these. "
        "Route dict/set/object questions to multiple-choice or manual grading."
    )


def compare(expected, actual, tol=1e-6):
    """Structural equality with float tolerance. Mirrored in grader.gs.

    bool compares exactly (True != 1); numbers compare within a relative+absolute
    tolerance; lists compare elementwise; str/None compare exactly.
    """
    if isinstance(expected, list):
        return (
            isinstance(actual, list)
            and len(expected) == len(actual)
            and all(compare(e, a, tol) for e, a in zip(expected, actual))
        )
    if isinstance(expected, bool) or isinstance(actual, bool):
        return expected is actual
    if isinstance(expected, (int, float)) and isinstance(actual, (int, float)):
        return abs(expected - actual) <= tol + tol * max(abs(expected), abs(actual))
    return expected == actual
