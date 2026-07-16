# CHEM 438 Homework App

Students open a URL, pick their name, type/run Python and answer questions, and
hit **Submit**. Grading happens **off the browser** (answers stay hidden) and
results land in a **Google Sheet** automatically.

```
GitHub Pages (static)        Student's browser              Google (your account)
──────────────────────       ──────────────────             ──────────────────────
index.html                   Pyodide runs the student's     Apps Script (grader.gs):
lessons/lesson_01.json  ──▶  Python locally; on Submit,  ──▶   • holds hidden answer keys
                             sends only its OUTPUTS            • grades, writes a row
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
  bank/*.md        the problem bank — markdown files of problems, split by topic/week
  bankmd.py        parses bank/*.md and verifies every solution passes its own checks
  assignments.py   each assignment = { title, intro, problems: [bank ids...] }
  build.py         resolves an assignment's ids → public lesson JSON + secret keys
  builder.html     a visual tool: browse the bank, pick problems, save an assignment
```

### Add a problem to the bank (markdown)
Drop a problem into any file under `bank/` (or make a new topic file). Format:

````markdown
## double_fix
kind: code_fn
title: Fix the double function
tags: functions, debug, week1
entry: double

### prompt
Fix the bug: `double` should return its input doubled.

### starter
```python
def double(x):
    return x + 2      # <-- wrong, fix it
```

### solution
```python
def double(x):
    return x * 2
```

### check
double(4) == 8
double(10) == 20
double(0) == 0
````

Optional sections: **`### walkthrough`** is a worked example, shown on the challenge
behind a collapsed "Show me how" toggle, so it helps a stuck student without
spoiling the answer. `difficulty: starter|easy|medium|hard` sets the XP (5/10/20/35).

Verify one file on its own with `python bankmd.py bank/<file>.md`. Beyond running
every check against the solution, it rejects a `bugs`-tagged problem whose starter
isn't actually broken, and a code problem with no `### starter` (which would open a
blank editor for the student).

The **`### check` lines must pass against the `### solution`** — if they don't,
the build stops with an error, so a broken problem never ships. The checks also
*define the grading*: write them as `entry(args) == expected` (or `is True/False`),
several varied ones so hard-coding fails. `code_var` uses `variable == expected`;
`mcq` uses an `answer:` line (1-based) + `### choices`; `written` needs only a
prompt. Autograded outputs must be int/float/str/bool/list.

### Hotfix a problem
Edit the line in the relevant `bank/*.md`, then one command republishes it:
`python build.py <lesson> --push "<url>" --token "<token>" && git push`. The
self-check re-runs, so you can't accidentally push a broken fix.

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
  re-run submitted code server-side (a small executor), reusing this same auth,
  table, and authoring — only the grade endpoint changes.

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

## Instructor login (admin gradebook)

Once Supabase email login is on, you get an **instructor view** automatically:
list your email in `ADMIN_EMAILS` (near the top of `index.html`) and, when you
sign in with it, you see the **gradebook** instead of the student assignment list.

For the gradebook to have data, create the `submissions` table once. In Supabase
open **SQL Editor → New query**, paste this, and Run (change the admin email):

```sql
create table submissions (
  email      text not null,
  lesson     text not null,
  score      int  default 0,
  out_of     int  default 0,
  results    jsonb,
  updated_at timestamptz default now(),
  primary key (email, lesson)
);
alter table submissions enable row level security;

-- students can read/write ONLY their own rows
create policy "own rows" on submissions
  for all
  using  (auth.jwt()->>'email' = email)
  with check (auth.jwt()->>'email' = email);

-- instructor(s) can read everything (add each admin email)
create policy "admin read all" on submissions
  for select
  using (auth.jwt()->>'email' = any (array['jyesselm@unl.edu']));
```

Now each student submit records a row (their email, assignment, score), and your
admin login shows the live gradebook. Row-Level Security guarantees a student can
only ever see their own row — never the keys or another student's work.

## Course sections (what students can see)

The bank is a curriculum, not a flat list. `UNITS` in `build.py` defines the course
in order; each problem's section is the LATEST skill it needs (derived from tags,
overridable with `unit:` in the bank). An assignment declares the section it covers
and whether it's `open`.

**Releasing an assignment reveals every challenge and topic page in its section and
earlier. Nothing beyond is rendered at all** — a student cannot see a problem before
its material is taught. The build refuses an assignment that declares a lower
section than its own problems need.

To release the next one: set `open=True` in `assignments.py`, then
`python build.py --all && git add -A && git commit -m "open hw2" && git push`.
The instructor console's Assignments tab has a "preview student view as of section N"
control to see any week of the term without rebuilding.

## Learn: topic reference pages

`authoring/reference/*.md` are the explainers that sit alongside lecture — plain
markdown, one per section, gated exactly like practice.

```
# Strings
unit: 2

## Making a string
...
```

Supported: `##`/`###`, paragraphs, ```python fences, `-`/`1.` lists, `>` callouts,
**bold**, `inline code`. Nothing else.

**Every code example is executed and checked against its stated output:**
```bash
python check_reference.py          # runs every block, compares each # comment to real Python
```
A reference page is read by students who can't tell a typo from a rule, so a wrong
output comment teaches a wrong fact. Run this before shipping an edit.
