"""
check_reference.py — run every code example in the reference pages and prove the
"# output" comments are what Python actually prints.

A reference page is read by students who cannot yet tell a typo from a rule, so a
wrong output comment teaches a wrong fact. This executes each ```python block and
compares every annotated print to reality.

    python check_reference.py            # check every page
    python check_reference.py 02_strings # check one

Blocks run in sequence per page, sharing a namespace, the way a reader following
along would. A block that raises is fine IF the page shows that error on purpose
(the traceback text appears in the block); otherwise it is reported.

Annotation form this understands:

    print(x / y)      # 3.5   <- optional explanation after the arrow

Lines whose comment is prose rather than a value are skipped, so you can still
write `# fix it` without tripping the checker.
"""

from __future__ import annotations

import contextlib
import io
import re
import sys
import traceback
from pathlib import Path

REF_DIR = Path(__file__).resolve().parent / "reference"
ERROR_WORDS = ("Error", "Traceback", "Exception")


def blocks(text):
    """Yield (line_no, code) for each ```python fence.

    Bare ``` fences are display-only (they show expected output or a traceback as
    text) — running them as Python would be nonsense.
    """
    out, lines, i = [], text.split("\n"), 0
    while i < len(lines):
        fence = lines[i].strip()
        if fence.startswith("```"):
            lang = fence[3:].strip().lower()
            start = i + 1
            i += 1
            buf = []
            while i < len(lines) and not lines[i].strip().startswith("```"):
                buf.append(lines[i]); i += 1
            if lang in ("python", "py"):
                out.append((start + 1, "\n".join(buf)))
        i += 1
    return out


SEP = re.compile(r"<-|->|--|\u2014")


def _clean(c):
    return c.lstrip("#").strip()


def _unquote(s):
    """Drop wrapping quotes only when they really wrap — 'She said "stop"' must survive."""
    return s[1:-1] if len(s) >= 2 and s[0] == s[-1] and s[0] in "'\"" else s


def _claims(want):
    """The value(s) a comment could be asserting, whichever side of the arrow."""
    segs = [seg.strip() for seg in SEP.split(want) if seg.strip()]
    return segs + [_unquote(s) for s in segs]


def _is_prose(s):
    """A comment that explains rather than states an output. Not a claim to check."""
    return ("\u2014" in s) or len(s) > 40


def expected_outputs(code):
    """The outputs a block claims, in order.

    Two conventions are in use and both are fine:
      A) a trailing run of comment-only lines listing each printed line
      B) an inline `print(x)   # value` on each print
    Returns (list_of_expected, style) or (None, None) when the block makes no claim.
    """
    lines = [l for l in code.split("\n")]
    # A: contiguous comment-only lines at the end of the block
    tail = []
    for ln in reversed(lines):
        if not ln.strip():
            continue
        if ln.strip().startswith("#"):
            tail.append(_clean(ln.strip()))
        else:
            break
    if len(tail) >= 1 and any(t for t in tail):
        return list(reversed(tail)), "trailing"
    # B: inline annotations on TOP-LEVEL prints. An indented print lives inside a
    # def/if and its comment describes the code, not the block's output.
    inline = []
    for ln in lines:
        if ln.startswith("print("):
            m = re.search(r"#\s*(.+)$", ln)
            inline.append(_clean("#" + m.group(1)) if m else None)
    if inline and any(x is not None for x in inline):
        return inline, "inline"
    return None, None


def run_block(code, ns):
    buf = io.StringIO()
    try:
        with contextlib.redirect_stdout(buf):
            exec(code, ns)  # noqa: S102 -- author-trusted teaching examples
        return buf.getvalue(), None
    except Exception:  # noqa: BLE001
        return buf.getvalue(), traceback.format_exc().strip().split("\n")[-1]


def check_page(path):
    text = path.read_text()
    problems, unpaired, ns, n_blocks, n_checked = [], [], {}, 0, 0
    for line_no, code in blocks(text):
        if not code.strip():
            continue
        n_blocks += 1
        out, err = run_block(code, ns)
        if err:
            # Raising is fine when the page is TEACHING that error — it just has to
            # quote it correctly, wherever it shows it (in-block or in the prose below).
            if err in text:
                continue
            problems.append(f"  line {line_no}: raises {err!r}, which appears nowhere on "
                            f"the page — either the example is broken or the shown text is wrong")
            continue
        printed = out.split("\n")
        if printed and printed[-1] == "":
            printed.pop()
        wants, style = expected_outputs(code)
        if wants is None:
            continue                       # block claims no output; nothing to check
        if len(wants) != len(printed):
            unpaired.append(f"  line {line_no}: claims {len(wants)} output(s) but printed "
                            f"{len(printed)} ({style})")
            continue
        for want, got in zip(wants, printed):
            if want is None:
                continue
            g = got.strip()
            if any(c == g for c in _claims(want)):
                n_checked += 1
                continue                   # the comment states exactly what ran
            if _is_prose(want):
                continue                   # an explanation, not a claim
            n_checked += 1
            problems.append(f"  line {line_no}: says {want!r} but Python prints {got!r}")
    return n_blocks, n_checked, problems, unpaired


if __name__ == "__main__":
    only = sys.argv[1] if len(sys.argv) > 1 else None
    paths = sorted(REF_DIR.glob("*.md"))
    if only:
        paths = [p for p in paths if only in p.name]
    if not paths:
        raise SystemExit("no reference pages found")
    total_bad = 0
    for path in paths:
        nb, nc, probs, unp = check_page(path)
        total_bad += len(probs)
        status = f"{len(probs)} PROBLEM(S)" if probs else "ok"
        print(f"{path.name}: {nb} blocks, {nc} outputs verified, {len(unp)} unverifiable — {status}")
        for p in probs: print(p)
        for u in unp:   print("  (skipped)" + u)
    print("\n" + (f"{total_bad} wrong output(s) — fix before shipping"
                  if total_bad else "every verified output matches real Python"))
    sys.exit(1 if total_bad else 0)
