"""
verify_notebook.py — run every code cell of a Colab homework notebook and report.

Independent check on the generated notebooks: it executes each code cell in order,
in one shared namespace (the way a student running top to bottom would), and reports
whether each ran clean, errored, or was left empty for the student. It prints the
output of the final "check in" cell so the check-in answer can be confirmed.

    python verify_notebook.py hw_pandas_basics.ipynb
    python verify_notebook.py --all

Notes
- `!pip ...` and `%magic` lines are stripped (Colab-only; the libraries are already
  installed here).
- Empty cells are the student's to fill — skipped, and counted.
- Some teaching cells RAISE ON PURPOSE (the "read the error" reasoning questions).
  A cell that errors is reported, not silently passed — you confirm by eye that the
  adjacent markdown is teaching that error. That judgment can't be automated, so it
  isn't pretended away.
- matplotlib runs headless (Agg) so plot cells don't hang.
"""

from __future__ import annotations

import contextlib
import io
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def _src(cell):
    s = cell.get("source", "")
    return s if isinstance(s, str) else "".join(s)


def _runnable(code):
    """Drop Colab-only lines; return "" if nothing executable remains."""
    keep = [ln for ln in code.split("\n")
            if not ln.strip().startswith(("!", "%"))]
    return "\n".join(keep).strip()


def verify(path):
    nb = json.loads(Path(path).read_text())
    ns = {}
    # headless plotting so plot cells don't block
    try:
        import matplotlib
        matplotlib.use("Agg")
    except Exception:  # noqa: BLE001
        pass
    ran = empty = errored = 0
    last_out = ""
    problems = []
    code_cells = [c for c in nb["cells"] if c.get("cell_type") == "code"]
    for i, cell in enumerate(code_cells):
        code = _runnable(_src(cell))
        if not code:
            empty += 1
            continue
        buf = io.StringIO()
        try:
            with contextlib.redirect_stdout(buf):
                exec(code, ns)  # noqa: S102 -- author-trusted teaching notebook
            ran += 1
            if buf.getvalue().strip():
                last_out = buf.getvalue().strip()
        except Exception as e:  # noqa: BLE001
            errored += 1
            head = code.split("\n")[0][:50]
            problems.append(f"    code cell {i}: {type(e).__name__}: {e}   [{head}...]")
    name = Path(path).name
    print(f"{name}: {ran} ran clean · {empty} left for the student · {errored} errored")
    for p in problems:
        print(p)
    if last_out:
        # the check-in cell is the last one that printed
        tail = last_out.split("\n")[-1]
        print(f"    check-in prints: {tail!r}")
    return errored, problems


if __name__ == "__main__":
    args = sys.argv[1:]
    if "--all" in args:
        paths = sorted(HERE.glob("hw_*.ipynb"))
    else:
        paths = [HERE / a if not a.startswith("/") else Path(a) for a in args]
    if not paths:
        raise SystemExit("usage: python verify_notebook.py <file.ipynb> | --all")
    total = 0
    for p in paths:
        if not p.exists():
            print(f"{p.name}: NOT FOUND"); continue
        total += verify(p)[0]
    print("\n" + (f"{total} errored cell(s) — inspect each (some may be intentional error demos)"
                  if total else "every runnable cell ran clean"))
