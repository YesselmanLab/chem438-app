"""
bankmd.py — read the markdown problem bank (bank/*.md) into a BANK dict.

Each problem is a `## id` block with `key: value` metadata and `### prompt`,
`### starter`, `### solution`, `### check` sections. On load this module:
  1. runs every problem's `### check` assertions against its `### solution` —
     if any fails, the build STOPS with a clear error (a broken problem never
     ships), and
  2. derives the grading inputs from the checks (so you write the checks once
     and they both verify the solution and define the tests).

build.py imports BANK from here; nothing downstream changes.
"""

from __future__ import annotations

import ast
import contextlib
import io
import re
from pathlib import Path

BANK_DIR = Path(__file__).resolve().parent / "bank"


def _blocks(text):
    """Yield (id, metadata dict, sections dict) for each `## id` block in a file."""
    cur_id = None
    meta, sections = {}, {}
    section, buf, in_meta = None, [], False

    def close_section():
        if section is not None:
            sections[section] = "\n".join(buf)

    for line in text.split("\n"):
        if line.startswith("## ") and not line.startswith("### "):
            if cur_id is not None:
                close_section()
                yield cur_id, meta, sections
            cur_id = line[3:].strip()
            meta, sections, section, buf, in_meta = {}, {}, None, [], True
            continue
        if cur_id is None:
            continue
        if line.startswith("### "):
            close_section()
            section, buf, in_meta = line[4:].strip().lower(), [], False
            continue
        if in_meta:
            m = re.match(r"^([A-Za-z_]+):\s*(.*)$", line)
            if m:
                meta[m.group(1)] = m.group(2).strip()
            continue
        if line.strip() in ("---", "***", "___"):
            continue        # markdown horizontal rule — a visual separator, not content
        buf.append(line)
    if cur_id is not None:
        close_section()
        yield cur_id, meta, sections


def _code(section_text):
    """Return the contents of a ```fenced``` code block, verbatim."""
    lines, out, in_fence = section_text.split("\n"), [], False
    for ln in lines:
        if ln.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            out.append(ln)
    return "\n".join(out) if out else section_text.strip("\n")


def _call_inputs(check, entry):
    """From `entry(args) == v` (or `is v`) return [args]; None if not that shape."""
    try:
        node = ast.parse(check.strip(), mode="eval").body
    except SyntaxError:
        return None
    if not isinstance(node, ast.Compare) or len(node.ops) != 1:
        return None
    left = node.left
    if isinstance(left, ast.Call) and isinstance(left.func, ast.Name) and left.func.id == entry:
        try:
            return [ast.literal_eval(a) for a in left.args]
        except (ValueError, SyntaxError):
            return None
    return None


TIERS = ("starter", "easy", "medium", "hard")


def _fails(code, checks):
    """True if `code` is genuinely broken — it errors, or misses a check."""
    ns = {}
    # A starter is allowed to print (a classic bug is print-instead-of-return);
    # swallow its output so running it here can't pollute the build log.
    with contextlib.redirect_stdout(io.StringIO()):
        try:
            exec(code, ns)  # noqa: S102 -- author-trusted starter
        except Exception:  # noqa: BLE001
            return True                 # doesn't even run: definitely broken
        for c in checks:
            try:
                if eval(c, dict(ns)) is not True:  # noqa: S307
                    return True
            except Exception:  # noqa: BLE001
                return True
    return False


def load_file(path):
    """Parse + verify one bank file. Raises SystemExit on the first bad problem."""
    path = Path(path)
    out = {}
    for pid, meta, sec in _blocks(path.read_text()):
        if pid in out:
            raise SystemExit(f"duplicate problem id {pid!r} (in {path.name})")
        out[pid] = _problem(pid, meta, sec, path.name)
    return out


def _problem(pid, meta, sec, where):
    kind = meta.get("kind")
    if not kind:
        raise SystemExit(f"[{pid}] missing 'kind' ({where})")
    if meta.get("difficulty", "easy") not in TIERS:
        raise SystemExit(f"[{pid}] difficulty must be one of {TIERS}, got "
                         f"{meta['difficulty']!r} ({where})")
    prob = {
        "kind": kind,
        "title": meta.get("title", pid),
        "tags": [t.strip() for t in meta.get("tags", "").split(",") if t.strip()],
        "difficulty": meta.get("difficulty", "easy"),
        "prompt": sec.get("prompt", "").strip("\n"),
        # optional worked example — shown behind a "Show me how" toggle
        "walkthrough": sec.get("walkthrough", "").strip("\n"),
        # optional: pin this problem to a curriculum unit, overriding the unit
        # its tags imply (build.py derives one when this is absent)
        "unit": int(meta["unit"]) if meta.get("unit") else None,
    }
    if kind in ("code_var", "code_fn"):
        prob["entry"] = meta["entry"]
        prob["starter"] = _code(sec.get("starter", ""))
        # Without a starter the student opens an empty editor and isn't even told
        # the function name. Nothing else catches this, so catch it here.
        if not prob["starter"].strip():
            raise SystemExit(f"[{pid}] has no '### starter' — a student would open "
                             f"this to a blank editor ({where})")
        solution = _code(sec.get("solution", sec.get("reference", "")))
        checks = [c for c in sec.get("check", "").split("\n") if c.strip()]
        ns = {}
        try:
            exec(solution, ns)  # noqa: S102 -- author-trusted solution
        except Exception as e:  # noqa: BLE001
            raise SystemExit(f"[{pid}] solution has an error: {e}")
        if prob["entry"] not in ns:
            raise SystemExit(f"[{pid}] solution doesn't define {prob['entry']!r}")
        inputs = []
        for c in checks:
            try:
                ok = eval(c, dict(ns))  # noqa: S307 -- author-trusted check
            except Exception as e:  # noqa: BLE001
                raise SystemExit(f"[{pid}] check errored: {c!r} -> {e}")
            if ok is not True:
                raise SystemExit(f"[{pid}] SOLUTION FAILS ITS OWN CHECK: {c!r}")
            if kind == "code_fn":
                args = _call_inputs(c, prob["entry"])
                if args is None:
                    raise SystemExit(
                        f"[{pid}] can't read a test input from check {c!r} — "
                        f"write it as {prob['entry']}(args) == expected")
                inputs.append(args)
        if kind == "code_fn":
            prob["inputs"] = inputs
            prob["reference"] = ns[prob["entry"]]     # callable
        else:
            prob["reference"] = solution              # code string
        # A "fix the bug" problem whose starter already passes is a dud: the
        # student has nothing to find. Prove the bug is real.
        if {"bugs", "debug"} & set(prob["tags"]) and not _fails(prob["starter"], checks):
            raise SystemExit(
                f"[{pid}] is tagged as a bug hunt, but its starter already passes "
                f"every check — there is no bug to fix ({where})")
    elif kind == "mcq":
        prob["choices"] = [ln[1:].strip() for ln in sec.get("choices", "").split("\n")
                           if ln.strip().startswith("-")]
        prob["answer"] = int(meta["answer"]) - 1      # 1-based md -> 0-based
    elif kind == "written":
        pass
    else:
        raise SystemExit(f"[{pid}] unknown kind {kind!r}")
    return prob




def _build():
    if not BANK_DIR.exists():
        raise SystemExit(f"no bank folder at {BANK_DIR}")
    bank = {}
    for path in sorted(BANK_DIR.glob("*.md")):
        for pid, prob in load_file(path).items():
            if pid in bank:
                raise SystemExit(f"duplicate problem id {pid!r} (also in {path.name})")
            bank[pid] = prob
    return bank


BANK = _build()


if __name__ == "__main__":
    # Verify one or more bank files without touching the rest of the bank:
    #     python bankmd.py bank/lists.md
    import sys
    if len(sys.argv) < 2:
        raise SystemExit("usage: python bankmd.py <file.md> [file.md ...]")
    for arg in sys.argv[1:]:
        probs = load_file(arg)
        print(f"OK {arg}: {len(probs)} problems, every solution passes its own checks")
