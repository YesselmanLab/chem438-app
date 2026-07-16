"""
refmd.py — read the reference pages (reference/*.md) into HTML the app can show.

These are the "how does this topic work" explainers that sit alongside lectures:
one page per course section, heavy on worked examples. They are plain markdown so
you can edit them without touching any code.

File format — first two lines are the header, then the body:

    # Strings
    unit: 2

    ## Making a string
    ...

Supported markdown (deliberately a small set — this is a renderer, not a CMS):
    ## h2      ### h3      paragraphs      - bullets      1. numbered
    > callout  ```python fenced code       **bold**       `inline code`

A page's `unit:` ties it to a course section (see UNITS in build.py), so a page
stays hidden until the homework covering that section is released.
"""

from __future__ import annotations

import html
import re
from pathlib import Path

REF_DIR = Path(__file__).resolve().parent / "reference"


def _inline(t):
    """Escape, then apply inline markup: `code` and **bold**."""
    t = html.escape(t)
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    t = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", t)
    return t


def md_to_html(md):
    out, lines, i = [], md.split("\n"), 0
    para, bullets, nums, quote = [], [], [], []

    def flush():
        # close whichever block we were accumulating
        if para:
            out.append("<p>" + _inline(" ".join(para)) + "</p>"); para.clear()
        if bullets:
            out.append("<ul>" + "".join(f"<li>{_inline(b)}</li>" for b in bullets) + "</ul>"); bullets.clear()
        if nums:
            out.append("<ol>" + "".join(f"<li>{_inline(b)}</li>" for b in nums) + "</ol>"); nums.clear()
        if quote:
            paras = [q for q in quote if q]
            out.append("<blockquote>" + "".join(f"<p>{_inline(q)}</p>" for q in paras) + "</blockquote>")
            quote.clear()

    while i < len(lines):
        ln = lines[i]
        if ln.strip().startswith("```"):
            flush()
            i += 1
            code = []
            while i < len(lines) and not lines[i].strip().startswith("```"):
                code.append(lines[i]); i += 1
            i += 1
            out.append('<pre class="ref-code" data-lang="python">' + html.escape("\n".join(code)) + "</pre>")
            continue
        if ln.startswith("### "):
            flush(); out.append("<h3>" + _inline(ln[4:].strip()) + "</h3>")
        elif ln.startswith("## "):
            flush(); out.append("<h2>" + _inline(ln[3:].strip()) + "</h2>")
        elif ln.startswith(">"):
            if para or bullets or nums: flush()
            body = ln[1:].strip()
            # A wrapped callout is ONE paragraph — join continuation lines rather than
            # breaking the sentence. A bare '>' starts a new paragraph inside the quote.
            if not body:
                quote.append("")
            elif quote and quote[-1]:
                quote[-1] += " " + body
            else:
                quote.append(body)
        elif re.match(r"^\s*- ", ln):
            if para or nums or quote: flush()
            bullets.append(ln.strip()[2:])
        elif re.match(r"^\s*\d+\. ", ln):
            if para or bullets or quote: flush()
            nums.append(re.sub(r"^\s*\d+\.\s*", "", ln))
        elif not ln.strip():
            flush()
        elif (bullets or nums) and ln.startswith((" ", "\t")):
            # an indented line under a bullet continues it — without this, the wrapped
            # half of a long bullet breaks out and becomes its own paragraph
            (bullets if bullets else nums)[-1] += " " + ln.strip()
        elif quote and not ln.startswith(">"):
            flush(); para.append(ln.strip())
        else:
            if bullets or nums or quote: flush()
            para.append(ln.strip())
        i += 1
    flush()
    return "\n".join(out)


def load():
    """Every reference page, in file order. Raises SystemExit on a bad header."""
    if not REF_DIR.exists():
        return []
    pages = []
    for path in sorted(REF_DIR.glob("*.md")):
        text = path.read_text()
        lines = text.split("\n")
        if not lines or not lines[0].startswith("# "):
            raise SystemExit(f"[{path.name}] must start with '# Title'")
        m = re.match(r"^unit:\s*(\d+)\s*$", lines[1].strip() if len(lines) > 1 else "")
        if not m:
            raise SystemExit(f"[{path.name}] line 2 must be 'unit: N'")
        pages.append({
            "id": path.stem,
            "title": lines[0][2:].strip(),
            "unit": int(m.group(1)),
            "html": md_to_html("\n".join(lines[2:])),
        })
    ids = [p["id"] for p in pages]
    if len(set(ids)) != len(ids):
        raise SystemExit("duplicate reference page id")
    return pages


if __name__ == "__main__":
    for p in load():
        n = p["html"].count('<pre class="ref-code"')
        print(f"OK {p['id']}: unit {p['unit']} · {p['title']!r} · {n} code examples")
