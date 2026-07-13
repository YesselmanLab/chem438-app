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

## Problem bank + assignments (the authoring model)

Problems live **once** in a reusable bank; an assignment is just a **selection**
of problems from it. Write a problem one time, drop it into any assignment.

```
authoring/
  bank.py          the problem bank — every problem, keyed by a short id, with tags
  assignments.py   each assignment = { title, intro, problems: [bank ids...] }
  build.py         resolves an assignment's ids → public lesson JSON + secret keys
  builder.html     a visual tool: browse the bank, pick problems, save an assignment
```

### Add a problem to the bank
Add one entry to `bank.py` (a `code_var`, `code_fn`, `mcq`, or `written`). For
code you write a **reference solution** — you never type expected answers;
`build.py` runs your reference to generate them. Use **several varied inputs** on
`code_fn` (that's what stops hard-coding). Autograded outputs must be
int/float/str/bool/list; route dict/set/random-output problems to `mcq`/`written`.

### Build an assignment two ways

**Visually (easiest):** run `python build.py --bank`, then open
`authoring/builder.html` in a browser. Search/filter the bank by tag, click the
problems you want, order them, name the assignment, and **Copy** the entry — paste
it into `assignments.py`.

**By hand:** add an entry to `assignments.py` listing the problem ids you want.

### Publish it
```bash
python build.py lesson_03 --push "https://…/exec" --token "YOUR_ADMIN_TOKEN"
git add lessons/ && git commit -m "add lesson 3" && git push
```
It appears on the students' assignment list automatically (`build.py` updates the
manifest). Build everything at once with `python build.py --all --push … --token …`.

*Verify the bank grades correctly anytime:* `python build.py lesson_01 && python test_pipeline.py`.

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

## Email login (optional accounts)

By default the app uses simple name entry. To turn on real accounts with verified
identity (students sign in with a code emailed to them — no passwords, no Google),
do this once:

1. Create a free project at **supabase.com**. Open **Project Settings → API** and
   copy the **Project URL** and the **anon public** key.
2. Paste both into the CONFIG block near the top of `index.html`:
   `const SUPABASE_URL = "...";` and `const SUPABASE_ANON = "...";`
   (Both are safe to commit — the anon key is designed to live in browsers.)
3. In Supabase **Authentication → Providers → Email**, confirm **Email OTP** is on
   (it is by default).
4. `git push`. The start screen now asks for an email, emails a 6-digit code, and
   signs the student in. Their email becomes their identity, so grades attribute
   cleanly across devices.

**Sending the emails:** Supabase's built-in mailer sends only a few per hour —
enough for you to test, not a whole class. For real use, set
**Authentication → Emails → SMTP** to your university mail server or a free tier
(Resend / SendGrid / Amazon SES) so codes arrive reliably. You can also restrict
sign-ups to your `@huskers.unl.edu` domain in the Auth settings.
