# CHEM 438 Homework App

Students open a URL, pick their name, type/run Python and answer questions, and
hit **Submit**. Grading happens **off the browser** (answers stay hidden) and
results land in a **Google Sheet** automatically.

```
GitHub Pages (static)        Student's browser              Google (your account)
──────────────────────       ──────────────────             ──────────────────────
index.html                   Pyodide runs the student's     Apps Script (grader.gs):
lessons/lesson_01.json  ──▶  Python locally; on Submit,  ──▶   • holds hidden answer keys
roster.json                  sends only its OUTPUTS            • grades, writes a row
                             + MCQ choices + text             • Sheet = live gradebook
```

The browser never receives answer keys — only the test *inputs*. It runs the
student's code on them and sends the *outputs*; the Apps Script compares those to
the hidden expected values. See the vetted design notes at the bottom.

---

## One-time setup (~20 min)

**1. Make the gradebook + grader (Google).**
- Create a new Google Sheet (this is your gradebook).
- **Extensions → Apps Script.** Delete the sample, paste all of `grader.gs`, Save.
- **Project Settings (gear) → Script properties → Add**: name `ADMIN_TOKEN`,
  value = a long random string (make one up). Save.
- **Deploy → New deployment → type: Web app.** Execute as **Me**, Who has access
  **Anyone**. Deploy, authorize, and **copy the Web app URL** (ends in `/exec`).

**2. Point the app at the grader.**
- Open `index.html`, set `const GRADER_URL = "…/exec";` to that URL.

**3. Upload the hidden keys** (no key ever touches the public repo):
```bash
cd authoring
python build.py lesson_01 --push "https://…/exec" --token "YOUR_ADMIN_TOKEN"
```
This rebuilds the public lesson file *and* writes the answers into a "Keys" tab of
your Sheet via the grader.

**4. Set your class list.** Edit `roster.json` (name + a short unique id each).

**5. Publish the front end.** Commit and push this folder to a GitHub repo, then
**Settings → Pages → Source: deploy from branch `main`, folder `/`**. Your
student link is `https://<org>.github.io/<repo>/` (add `?lesson=lesson_01`).

Done. The **Gradebook** tab fills itself as students submit; the **Keys** tab
holds the hidden answers.

---

## Authoring a new lesson (each week, <15 min)

1. Copy `authoring/lesson_01.py` to `authoring/lesson_02.py`, edit the questions.
   Each coding question needs a **reference solution** — you never type expected
   answers; `build.py` runs your reference to generate them.
2. Build + push keys:
   ```bash
   python build.py lesson_02 --push "https://…/exec" --token "YOUR_ADMIN_TOKEN"
   ```
3. `git add lessons/ && git commit && git push` (publishes the public file).
   Students use `…github.io/<repo>/?lesson=lesson_02`.

**Question kinds:** `code_var` (define a variable), `code_fn` (write a function,
graded on several inputs), `mcq`, `written`. Use **several varied inputs** on
`code_fn` — that's what stops hard-coding. Autograded outputs must be
int/float/str/bool/list; route dict/set/random-output questions to `mcq` or
`written` (build.py will error if you forget).

---

## Testing it

- **Grading logic** (no browser needed): `cd authoring && python test_pipeline.py`
  — proves correct passes, wrong fails, and hard-coded constants fail.
- **The app**: open the Pages URL. Before you set `GRADER_URL` it runs in
  **preview mode** (code runs, submit isn't graded). After setup, submit lands a
  real row in the Sheet.

---

## Design notes (why it's built this way)

This is the survivor of a 4-strategy bake-off + 2 rounds of adversarial review.
- **Answer secrecy:** keys live only in the Apps Script / Keys tab. The client
  gets inputs, returns outputs, gets back a boolean.
- **Robust collection:** one row per (student, lesson) via `LockService` upsert;
  the client re-queues failed submits in `localStorage` and retries when online;
  "Submitted ✓" shows only on a confirmed response.
- **Graceful degradation:** MCQ + written need no Python, so a phone that can't
  load Pyodide can still submit; code is saved for manual grading.
- **Honest limitation:** grading checks *outputs*, so it verifies the answer is
  right, not that this code produced it — fine for formative homework, not exam
  proctoring. If you ever need fabrication-proof grading, the upgrade is to
  re-run submitted code server-side (a small executor), reusing this same roster,
  Sheet, and authoring — only the grade endpoint changes.
