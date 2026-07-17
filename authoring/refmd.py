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


def slug(text):
    """Heading -> stable anchor id. A problem's `see:` points at one of these, so
    changing a heading breaks a link — the build checks, it won't drift silently."""
    s = text.replace("`", "").replace("**", "").lower()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def md_to_html(md, anchors=None):
    out, lines, i = [], md.split("\n"), 0
    para, bullets, nums, quote = [], [], [], []
    n_ex = [0]

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
            lang = ln.strip()[3:].strip().lower()
            i += 1
            code = []
            while i < len(lines) and not lines[i].strip().startswith("```"):
                code.append(lines[i]); i += 1
            i += 1
            body = html.escape("\n".join(code))
            if lang in ("python", "py"):
                # A live example: the student can edit it and run it right here.
                # data-i orders it on the page, so running one example can reuse the
                # variables defined by the ones above it, like reading top to bottom.
                out.append(f'<div class="ex" data-i="{n_ex[0]}">'
                           f'<pre class="ref-code">{body}</pre>'
                           f'<div class="exbar"><button class="exrun">▸ Run</button>'
                           f'<span class="exhint"></span></div>'
                           f'<pre class="exout"></pre></div>')
                n_ex[0] += 1
            else:
                # a bare fence is display-only: expected output or a traceback, as text
                out.append(f'<pre class="ref-out">{body}</pre>')
            continue
        if ln.startswith("### "):
            flush()
            t = ln[4:].strip()
            if anchors is not None: anchors.append(slug(t))
            out.append(f'<h3 id="{slug(t)}">' + _inline(t) + "</h3>")
        elif ln.startswith("## "):
            flush()
            t = ln[3:].strip()
            if anchors is not None: anchors.append(slug(t))
            out.append(f'<h2 id="{slug(t)}">' + _inline(t) + "</h2>")
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
        anchors = []
        html_body = md_to_html("\n".join(lines[2:]), anchors)
        dupes = {a for a in anchors if anchors.count(a) > 1}
        if dupes:
            raise SystemExit(f"[{path.name}] two headings make the same anchor {sorted(dupes)} — "
                             f"a `see:` link couldn't tell them apart; reword one")
        pages.append({
            "id": path.stem,
            "title": lines[0][2:].strip(),
            "unit": int(m.group(1)),
            "html": html_body,
            "anchors": anchors,
        })
    ids = [p["id"] for p in pages]
    if len(set(ids)) != len(ids):
        raise SystemExit("duplicate reference page id")
    return pages


def anchor_index():
    """{'02_strings#slicing': 'Slicing', ...} — every target a `see:` may point at."""
    idx = {}
    for p in load():
        for a in p["anchors"]:
            idx[f"{p['id']}#{a}"] = p["title"]
    return idx


if __name__ == "__main__":
    import sys
    if "--anchors" in sys.argv:
        # ground truth for anyone writing a `see:` line in the bank
        for p in load():
            print(f"\n# {p['title']}  (unit {p['unit']}) — page id: {p['id']}")
            for a in p["anchors"]:
                print(f"  see: {p['id']}#{a}")
        raise SystemExit(0)
    for p in load():
        n = p["html"].count('<div class="ex"')
        print(f"OK {p['id']}: unit {p['unit']} · {p['title']!r} · "
              f"{n} runnable examples · {len(p['anchors'])} anchors")
