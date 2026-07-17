# Planning your code
unit: 9

## The blank editor is a planning problem

You know `if`. You know `for`. You know how to write a function and index a list. Then someone
says "write a program that reports who passed" and you sit there, cursor blinking, and nothing
comes out.

That is not a Python problem. Nothing on that screen is asking you about syntax. You are stuck
because you have a **task** and what you need is a **first step**, and nobody ever taught you
how to get from one to the other. This page is that: a way of working that turns a vague
sentence into code you can type.

> **Misconception: real programmers write it right the first time.** They do not. Nobody does.
> They write a wrong version fast, run it, look at what came out, and fix it — over and over,
> in tiny steps. What you see in a textbook is the **last** draft. You are comparing your first
> draft to somebody's twentieth and concluding you're bad at this. Your first draft is supposed
> to be bad. The skill is getting to a bad draft quickly and improving it in checked steps.

## The task

Here is the whole task, the way a real one arrives — vague. We'll plan it end to end, showing
every ugly intermediate stage, because the intermediate stages are the actual lesson.

```
Given a list of names and a list of scores, report who passed.
```

## Say it in English first

Do not write Python. Write comments — what the program has to do, in your own plain words, one
step per line.

```python
# take a list of names and a list of scores
# look at each student, one at a time
# decide whether that student passed
# collect the names of the ones who passed
# hand back the collected names
print("no code yet, and that is fine")   # no code yet, and that is fine
```

That runs. It does nothing, but it runs — comments are invisible to Python. And look what you
have: five steps, every one small enough that you already know how to do it. "Look at each
student one at a time" is a `for` loop. "Decide whether that student passed" is an `if`.
"Collect the names" is `.append()` onto a list. That's the trick — you didn't solve the task,
you **cut it up** until the pieces were things you already know. And those comments don't get
deleted; they're the skeleton you fill in.

## Do it by hand first

Before you write any code, do the task on paper with one small example. If you can't do it by
hand, you cannot code it — coding it means explaining the steps to a machine far stupider than
you.

```
names:  ["Ana", "Ben", "Cy"]
scores: [88, 52, 71]

Ana   88   is 88 >= 60?   yes   -> keep Ana
Ben   52   is 52 >= 60?   no    -> skip
Cy    71   is 71 >= 60?   yes   -> keep Cy

answer: ["Ana", "Cy"]
```

That just answered three questions you didn't know you had. What does "passed" mean? You had to
pick a number: 60. How do names and scores line up? By **position** — Ana is first in both
lists. What does "report" hand back? A list of names. None of that was in the task; you found
it by trying one example. This is why "I don't know where to start" is so often really "I don't
actually know what I'm being asked for yet."

> **Misconception: planning is wasted time — I could have been coding.** Those five minutes on
> paper are what stop you writing forty lines against the wrong idea of the problem and
> throwing them away. Nobody counts the hours lost to that, because it doesn't look like being
> stuck. It looks like typing.

## Write the signature first

You know what goes in (two lists) and what comes out (a list of names). Write exactly that, and
nothing else.

```python
def passing_students(names, scores):
    return []

print(passing_students(["Ana", "Ben", "Cy"], [88, 52, 71]))   # []
```

That answer is **wrong**, and the function is done in the only sense that matters right now: it
runs, it takes what it should take, and it gives back the right *kind* of thing. You now have
something to improve instead of a blank screen. Every version from here on will run.

## Start with the simplest input that could work

Don't start with three students. Start with **one** — the smallest version of this problem that
is still the problem.

```python
def passing_students(names, scores):
    if scores[0] >= 60:
        return [names[0]]
    return []

print(passing_students(["Ana"], [88]))   # ['Ana']
print(passing_students(["Ben"], [52]))   # []
```

It works! For one student. It's hopeless for two. That's fine — it's real, running code that
proves the `>= 60` check and the "put the name in a list" step both do what you thought. Those
two things are now **known**, so when the three-student version breaks later, you already know
it isn't those.

## Build it one piece at a time and run it every time

Now grow the working thing. One student becomes every student: a loop around the code you
already trust.

```python
def passing_students(names, scores):
    passed = []
    for i in range(len(names)):
        if scores[i] >= 60:
            passed.append(names[i])
    return passed

print(passing_students(["Ana", "Ben", "Cy"], [88, 52, 71]))   # ['Ana', 'Cy']
```

Compare that to the hand trace. Same answer. The `if scores[0] >= 60` became
`if scores[i] >= 60`, and `i` walks the positions. The one-student version wasn't wasted work —
it *became* the loop body.

> **Misconception: I should write the whole thing, then run it.** The most expensive habit a
> beginner can have. Write thirty lines, hit Run, get an error, and now you have thirty
> suspects and no idea which is guilty. Write three lines, run, and the bug can only be in the
> three you just typed. Same total typing, a tenth of the debugging. **Run after every small
> change** — especially one you're sure about.

## `print()` is your microscope

Now the data changes, the way real data does — the scores arrive as text:

```python
names = ["Ana", "Ben", "Cy"]
scores = ["88", "52", "71"]
print(passing_students(names, scores))
# TypeError: '>=' not supported between instances of 'str' and 'int'
```

Do not guess. Do not start retyping the `if`. Print the thing you're unsure about — and that's
`scores[i]`:

```python
names = ["Ana", "Ben", "Cy"]
scores = ["88", "52", "71"]

for i in range(len(names)):
    print(i, repr(names[i]), repr(scores[i]))
# 0 'Ana' '88'
# 1 'Ben' '52'
# 2 'Cy' '71'
```

There it is: `'88'`, with quotes. It's a string — `repr()` shows the quotes that plain `print()`
hides. Now the `TypeError` reads like a sentence instead of an accusation: of course Python
won't compare `'88'` to `60`; one is text.

```python
def passing_students(names, scores):
    passed = []
    for i in range(len(names)):
        if int(scores[i]) >= 60:
            passed.append(names[i])
    return passed

print(passing_students(["Ana", "Ben", "Cy"], ["88", "52", "71"]))   # ['Ana', 'Cy']
```

**Print the thing you're unsure about, the moment you're unsure about it.** A `print()` in the
middle of a loop is not a sign of failure — it's how you see. Delete them when the piece works.

## Name things for what they are

The same working function, with the names hollowed out:

```python
def check(a, b):
    r = []
    for i in range(len(a)):
        if int(b[i]) >= 60:
            r.append(a[i])
    return r

print(check(["Ana", "Ben", "Cy"], ["88", "52", "71"]))   # ['Ana', 'Cy']
```

Identical answer. But `check` — checks what? `a` and `b` — which is which? You have to read the
body to answer questions that `passing_students(names, scores)` answered in its first line.

Naming is not tidying up at the end. It is planning, done with words. When you can't think of a
name for a variable, that's usually not a vocabulary problem — it's a sign you don't yet know
what that variable is *for*, which is exactly what you were supposed to work out before you
typed it.

## Break the last piece down

The task said "report", not "give me a list". A report is something a human reads — a different
job from finding who passed, so it gets its own function:

```python
def did_pass(score, cutoff=60):
    return int(score) >= cutoff

def passing_students(names, scores, cutoff=60):
    passed = []
    for i in range(len(names)):
        if did_pass(scores[i], cutoff):
            passed.append(names[i])
    return passed

def report(names, scores, cutoff=60):
    passed = passing_students(names, scores, cutoff)
    return f"{len(passed)} of {len(names)} passed: {', '.join(passed)}"

print(report(["Ana", "Ben", "Cy"], ["88", "52", "71"]))
print(report(["Ana", "Ben", "Cy"], ["88", "52", "71"], cutoff=80))
# 2 of 3 passed: Ana, Cy
# 1 of 3 passed: Ana
```

Three functions, each of which fits in your head. `did_pass` knows the rule for one score.
`passing_students` knows how to walk a list. `report` knows how to talk to a human. The
`cutoff=60` default appeared because writing `did_pass` forced the question "passed *what*?"
into the open, where it could be an option instead of a number buried in a loop.

Look back at the comments you started with. They're still there — one per function, spelled in
code.

## The second time through, faster

That was one task, slowly. Here's a second, so you can see it's a **method** and not a story
about one function. Equally vague:

```
Given a sentence, find the word that shows up most often.
```

**English first**, one step per line:

```python
# split the sentence into words
# count how many times each word appears
# find the word with the biggest count
# hand back that word
print("still no code")   # still no code
```

**By hand**, on the smallest example that's still interesting:

```
"the cat the dog the cat"

split ->  ["the", "cat", "the", "dog", "the", "cat"]

walk the words, keeping a tally:
  the -> 1     cat -> 1     the -> 2     dog -> 1     the -> 3     cat -> 2

counts: the=3, cat=2, dog=1     biggest: the
```

The hand trace told you the shape: you need a **word -> count** pairing, walked one word at a
time. That's a dictionary. You didn't have to be clever — you just watched your own hand.

**Signature first, one piece only.** Not the whole function — just the counting, returned early
so you can see it:

```python
def most_common(sentence):
    words = sentence.split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts

print(most_common("the cat the dog the cat"))
# {'the': 3, 'cat': 2, 'dog': 1}
```

Wrong answer — it returns counts, not a word — but check it against the hand trace:
`the=3, cat=2, dog=1`. Matches. That piece is now **known**, and if the finished function is
ever wrong, it isn't this.

**Last piece** — biggest count wins:

```python
def most_common(sentence):
    words = sentence.split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1

    best_word = ""
    best_count = 0
    for word in counts:
        if counts[word] > best_count:
            best_word = word
            best_count = counts[word]
    return best_word

print(most_common("the cat the dog the cat"))   # the
print(most_common("hello"))                     # hello
```

Same method, five minutes instead of a page: say it in English, do one example by hand, write
the signature, build one piece at a time, run every time, check against the hand trace.

## When you're stuck: make it smaller, or make it concrete

Two moves. Between them they unstick almost everything.

**Make it smaller.** Whatever you're trying to do, do less of it. Three students is too many —
do one. The whole function won't come — write just the `if`. A version that handles one case
isn't a failure; it's the first working version, and the loop grows out of it.

**Make it concrete.** Stop thinking about "a list of scores" and pick `[88, 52, 71]`. Do what
you'd do with a pencil for `88`. Vague tasks are paralysing; specific ones are just work.

Still stuck after both? Then you've found something worth saying out loud, which beats "I don't
get it":

- **"I don't know what the answer should look like."** Then you're not ready to code. Go back
  to the hand trace and write down what you want out, exactly, for one input.
- **"I know what I want but not how to say it in Python."** Now that's a real, small,
  answerable question — and it's the *only* one of these that's actually about Python.
- **"It runs but the answer's wrong."** Print the thing you're unsure about and compare it
  against your hand trace, line by line. The first line where they disagree is your bug.

Two of those three aren't Python questions at all. That's the point of this whole page.

## Quick reference — what's available

### The method

1. **Say it in English.** Write the steps as `#` comments, one per line, before any code.
2. **Do it by hand.** One small example, on paper. If you can't, you can't code it yet.
3. **Break it down** until every step is something you already know how to do.
4. **Write the signature first** — what goes in, what comes out. Have it `return` a fake
   answer of the right kind so it runs.
5. **Start with the simplest input that could work** — one item, not the whole list.
6. **Grow it one piece at a time**, and **run it after every change**.
7. **Print the thing you're unsure about** the moment you're unsure about it.
8. **Name things for what they are.** No name means no plan.
9. **Compare against your hand trace.** The first difference is the bug.

### Moves when stuck

- **Make it smaller** — one item, one line, one case.
- **Make it concrete** — real values instead of "a list of numbers".
- **Say which kind of stuck you are** — don't know the answer / don't know the Python / wrong
  answer. Only the middle one is a Python question.

### What the habits look like in code

- `# step one` ... `# step two` — a comment skeleton. Runs, does nothing, costs nothing.
- `def name(inputs):` then `return []` — signature plus a placeholder answer, so it runs from
  minute one.
- `print(x)` / `print(type(x))` — see the value, see what kind of thing it is.
- `print(repr(x))` — see whether it's a string; the quotes give it away.
- `print(i, x)` inside a loop — watch the loop go round.

And the three lies to stop believing: that real programmers get it right the first time, that
writing thirty lines before running saves time, and that planning is time away from coding.
Planning **is** the coding — it's the part that stops you writing the wrong program well.
