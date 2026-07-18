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
`mcq` uses an `answer:` line (1-based) + `### choices`; a **predict-output** `mcq` may add a `### code` block — the build
runs it and rejects the problem unless the marked answer is exactly what it prints; `written` needs only a
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

## Accounts (email + password)

Students **create an account** with their email and a password, then sign in with
it — no Google, and no reliance on emailed codes for everyday login. Their email is
their identity, so grades follow them across devices.

**One-time setup:**

1. Create a free project at **supabase.com** → **Project Settings → API** → copy the
   **Project URL** and the **anon public** key.
2. Paste both into the CONFIG block near the top of `index.html`
   (`const SUPABASE_URL = "…";` / `const SUPABASE_ANON = "…";`). Both are safe to
   commit — the anon key is designed to live in browsers. **Never** paste the
   `service_role` / secret key.
3. **Turn OFF email confirmation** — Supabase **Authentication → Providers → Email**,
   uncheck **"Confirm email"**. This is what makes "Create an account" work
   instantly: sign-up returns a usable session with no email round-trip. (Leave it
   on and students get stuck at "check your email" — the part that needs SMTP.)
4. Set **Authentication → URL Configuration → Site URL** to your Pages URL
   (`https://<org>.github.io/<repo>/`) so password-reset links come back to the app.
5. `git push`. The start screen now offers **Sign in**, **Create an account**, and
   **Forgot password?**, plus a one-time email code as a fallback.

**Password reset needs working email.** "Forgot password?" sends a reset link, which
only arrives if email delivery works. Supabase's built-in mailer sends a few per
hour (fine for the odd reset); for reliability set **Authentication → Emails → SMTP**
to a free tier (Resend / SendGrid / Amazon SES) or your university server. For a
15-person class you can also reset a password by hand in the Supabase dashboard
(Authentication → Users → ⋯ → "Send recovery" or set a new password).

### Restrict who can register

Two layers, because a browser-side check alone can be bypassed by calling the API
directly.

**Layer 1 — domain (already on).** `ALLOWED_EMAIL_DOMAINS` at the top of `index.html`
is set to `huskers.unl.edu` / `unl.edu`. Anyone whose email isn't one of those is
turned away before sign-up. Safe to commit — a domain isn't sensitive. Set it to
`[]` to allow any domain.

**Layer 2 — your exact class roster (the CSV).** This is the real lock, and the
student emails live **only in Supabase, never in this repo** (a public repo must
never hold the roster). One-time:

1. **SQL Editor**, run:
   ```sql
   create table allowed_emails (email text primary key);
   alter table allowed_emails enable row level security;   -- no policy = private

   -- lets the app ask "is THIS email allowed?" without exposing the whole list
   create or replace function is_email_allowed(addr text)
   returns boolean language sql security definer stable as $$
     select exists (select 1 from allowed_emails where email = lower(addr));
   $$;
   grant execute on function is_email_allowed(text) to anon;
   ```
2. **Import your CSV**: Table Editor → `allowed_emails` → Insert → *Import data from
   CSV*. Give the CSV a single `email` column (one address per row, lowercase).
3. In `index.html` set `const ROSTER_ENFORCED = true;` and push. The app now tells a
   non-rostered student "that email isn't on the class list" *before* it tries to
   register them.
4. **Enforce it server-side** (so it can't be bypassed) — pick one:
   - *Simplest:* turn OFF self-signup (Authentication → Sign-ups) and pre-create the
     accounts from your CSV (Authentication → Users → Add user, or a one-off admin
     script). Only rostered emails then exist, and students just sign in / reset.
   - *Self-service + enforced:* add a **Before-User-Created** auth hook (Authentication
     → Hooks) that rejects an email not in `allowed_emails`. The hook function's exact
     signature changes between Supabase versions — follow their current "Before User
     Created hook" doc, checking `allowed_emails` the same way `is_email_allowed` does.

Layer 1 is instant. Layer 2 step 3 gives the friendly message; step 4 is what makes
it unbypassable.

**If the sign-in service can't load** (a blocked CDN, no connection), the app now
says so and asks the student to refresh — it no longer quietly drops to name-entry
where their work wouldn't reach the gradebook.

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

-- students may READ, INSERT, and UPDATE only their own rows — but NOT DELETE.
-- (Separate policies, not one "for all", so there is no delete path: a student
--  can't wipe their own scores, and the row survives to be exported.)
create policy "read own"   on submissions for select
  using  (auth.jwt()->>'email' = email);
create policy "insert own" on submissions for insert
  with check (auth.jwt()->>'email' = email);
create policy "update own" on submissions for update
  using  (auth.jwt()->>'email' = email)
  with check (auth.jwt()->>'email' = email);

-- instructor(s) can read everything (add each admin email)
create policy "admin read all" on submissions
  for select
  using (auth.jwt()->>'email' = any (array['jyesselm@unl.edu']));
```

If you already ran the earlier `"own rows"` version, replace it:
`drop policy "own rows" on submissions;` then run the three policies above.

Now each student submit records a row (their email, assignment, score), and your
admin login shows the live gradebook. Row-Level Security guarantees a student can
only ever see their own row — never the keys or another student's work — and with
no DELETE policy, can't erase their scores.

**Export + back up.** The gradebook tab has an **Export CSV** button (one row per
student, one column per assignment, with totals). Grades live in one free-tier
table, so export periodically — that CSV is your off-Supabase backup.

**Honest limit:** grading is still client-side (viability mode ships the answer
keys to the browser), so a determined student could submit an inflated score for
their own row. The no-DELETE lockdown stops erasure, not fabrication; making scores
tamper-proof needs the server-side grader (a separate project). For formative
homework against in-class quizzes, deterrence — not integrity — is the bar.

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
