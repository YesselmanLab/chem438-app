# Syntax basics
unit: 1

Python has a handful of rigid rules about *how* you type code — where the spaces go, which characters come in pairs, what has to end with a colon. Break one and Python stops before it runs anything and shows you a `SyntaxError` or an `IndentationError`. The rules are few and they never change, so once they're in your fingers you stop tripping over them.

This page is the rules themselves — the right way to type each one, and what breaks when you don't. A companion page, **Reading errors**, teaches how to decode the message Python prints when you break one; read that too. Two habits will save you more time than anything else here: **always check the parentheses, and always check the indentation.**

## Indentation — the spaces at the front of a line

This is Python's most surprising rule, and the one that catches every beginner. In Python, the spaces at the front of a line are **not decoration** — they are how Python knows which lines belong together.

Look at an `if`. The line that runs *when the condition is true* is pushed to the right:

```python
temperature = 72
if temperature > 60:
    print("nice out")
    print("wear a light jacket")
print("done deciding")
# nice out
# wear a light jacket
# done deciding
```

The two indented lines belong to the `if` — they run only when the condition is true. The last line isn't indented, so it's outside the `if` and always runs. Many languages use curly braces `{ }` to mark that grouping; Python uses the indentation itself. The spaces *are* the punctuation.

> **Misconception: the indentation is just to make it look neat.** It isn't cosmetic — it changes what the code *does*. Un-indent a line and you've moved it out of the `if`. The layout and the meaning are the same thing.

The same rule holds for `for`, `while`, `def`, and every other block:

```python
def greet(name):
    message = "hi " + name
    return message

for letter in "cat":
    print(letter)
# c
# a
# t
```

Everything indented under `def greet(name):` is the body of the function. Everything indented under the `for` runs once per letter.

### Use 4 spaces, and be consistent

The standard is **4 spaces** per level. You don't have to count them by hand — pressing **Tab** in the editor inserts them for you. What matters is that lines you mean to group together are indented **the same amount**.

If Python expects an indented line and doesn't get one, you get an `IndentationError`:

```
if 5 > 3:
print("yes")

IndentationError: expected an indented block after 'if' statement on line 1
```

That message is almost a to-do list: it wants an indented block, after the `if`, on line 1. The fix is to push the line in:

```python
if 5 > 3:
    print("yes")
# yes
```

The opposite mistake — indenting a line when nothing above it opened a block:

```
songs = 0
    songs = songs + 1

IndentationError: unexpected indent
```

"Unexpected indent" means: this line is pushed to the right, but nothing above it asked for a block. Nothing here should be indented, so line the two up:

```python
songs = 0
songs = songs + 1
print(songs)
# 1
```

### Never mix tabs and spaces

A tab and four spaces can look **identical** on screen and be completely different characters underneath. If you indent one line with spaces and the next with a tab, Python can't tell how they line up, and you get a `TabError`:

```
if True:
    print("a")
	print("b")

TabError: inconsistent use of tabs and spaces in indentation
```

Those two `print` lines look equally indented, but the first used spaces and the second a tab. This is a miserable bug to spot by eye, because the lines *look* identical — so don't rely on your eyes. Set your editor to turn tabs into spaces (most do by default; if you ever see a `TabError`, that setting is off).

> **Habit to build: when a block errors, check the indentation first.** A huge share of beginner errors are one line indented a little too far or not far enough. Line up the lines that belong together and look again.

## The colon `:`

Every line that opens a block ends with a colon. That means `if`, `elif`, `else`, `for`, `while`, and `def` — all of them:

```python
score = 90
if score > 60:
    print("pass")
else:
    print("try again")
# pass
```

The colon is Python's way of saying "an indented block comes next." Forget it and Python tells you exactly what it wanted:

```
score = 90
if score > 60
    print("pass")

SyntaxError: expected ':'
```

`expected ':'` — it's naming the exact character that's missing. Add it and it runs:

```python
score = 90
if score > 60:
    print("pass")
# pass
```

A `def` needs one just the same — `def add(a, b)` without a `:` gives the identical `expected ':'`. The pattern to memorize: **if a line starts a block, it ends with a colon.** When you type `if`, `for`, `while`, or `def`, put the `:` on before you even fill in the body.

## Matching brackets, parentheses, and quotes

Every opener needs its partner. Every `(` needs a `)`, every `[` needs a `]`, every `{` needs a `}`, and every quote needs a matching quote. They come in pairs, always.

Here's correct code with several pairs, all closed:

```python
prices = [2.50, 1.25, 4.00]
total = sum(prices)
print("Total:", round(total, 2))
# Total: 7.75
```

Count them: `[ ]` around the list, `( )` around `sum(...)`, `( )` around `print(...)`, `"..."` around the text. Four pairs, all matched.

The classic mistake is an unclosed `(`. And here's the surprising part — **the error often points at the *next* line**, not the one with the missing bracket:

```
prices = [2.50, 1.25]
total = sum(prices
print("Total:", total)

SyntaxError: '(' was never closed
```

Your eye goes to the `print` line, because that's where things "look" broken. But Python names the line with `sum(` — and it's right. That parenthesis opened and nobody closed it; Python kept reading, looking for the `)`, and only gave up later. `'(' was never closed` even tells you which bracket type to hunt for. Close it:

```python
prices = [2.50, 1.25]
total = sum(prices)
print("Total:", total)
# Total: 3.75
```

Square brackets and curly braces give the same message with their own symbol — `'[' was never closed`, `'{' was never closed`. And one closing bracket **too many** gets its own message, `SyntaxError: unmatched ')'`.

### Quotes are pairs too

Open a quote and never close it, and Python complains that the string is "unterminated":

```
label = "Score:
print(label)

SyntaxError: unterminated string literal (detected at line 1)
```

"Unterminated" means: you opened a quote and it never closed. The fix is the missing `"`:

```python
label = "Score:"
print(label)
# Score:
```

This one catches everyone — an apostrophe inside single quotes:

```
message = 'It's fine'

SyntaxError: unterminated string literal (detected at line 1)
```

Python reads `'It'` as a complete string, then trips over the leftover `s fine'`. The apostrophe *closed* the string early. The fix is to use double quotes on the outside, so the apostrophe is just an ordinary character inside:

```python
message = "It's fine"
print(message)
# It's fine
```

The same trick works the other way — single quotes on the outside when you need double quotes inside, and an **f-string** (a string with an `f` in front that lets you drop variables in with `{ }`) plays by the same pairing rules:

```python
name = "Sam"
print('She said "stop"')
print(f"hello {name}")
# She said "stop"
# hello Sam
```

## Commas

Commas separate items — the values in a list, the arguments to a function. Leave one out and the two items collide into something Python can't read:

```
nums = [1 2 3]

SyntaxError: invalid syntax. Perhaps you forgot a comma?
```

Python even guesses the cause for you: "Perhaps you forgot a comma?" The fix is the missing commas:

```python
nums = [1, 2, 3]
print(nums)
print(len(nums))
# [1, 2, 3]
# 3
```

The same holds when you pass several things to a function — each is separated by a comma:

```python
print("a", "b", "c")
print(max(4, 9, 1))
# a b c
# 9
```

> **Watch out — a missing comma between two strings does *not* always error.** `print("a" "b")` runs and prints `ab`, because Python quietly glues adjacent strings together. That's a silent wrong answer, not a crash — exactly the kind of bug that's hardest to find. When a list of text looks one item short, count your commas.

## Capitalization and spelling

Python is **case-sensitive**: `Score` and `score` are two different names, and `Print` is not `print`. The capital letters have to match exactly.

Three special values are always capitalized — `True`, `False`, and `None`:

```python
raining = True
sunny = False
nothing_yet = None
print(raining)
print(sunny)
print(nothing_yet)
# True
# False
# None
```

Type them in lowercase and Python doesn't recognize them. It thinks `true` is a variable name you never created, and raises a `NameError`:

```
x = true

NameError: name 'true' is not defined
```

The same happens when you capitalize a built-in that should be lowercase: `Print("hello")` gives `NameError: name 'Print' is not defined`, because `print` is lowercase and `Print` is a name Python has never heard of. Keywords like `if`, `for`, `while`, `def`, `return`, and `else` are **all lowercase**, always. When something you're sure exists gives a `NameError`, suspect the capitalization first — compare it letter by letter against the name you meant.

> **Misconception: Python fixes small typos or capitalization for you.** It never guesses. `Print`, `PRINT`, and `print` are three different words to Python, and only one of them is the function. Exact spelling, exact case.

## `=` versus `==`

These look almost the same and do completely different jobs:

- **one** `=` **assigns** — it puts a value in a variable. `x = 5` means "put 5 in the box called x."
- **two** `==` **compares** — it asks a question. `x == 5` means "is x equal to 5?" and gives back `True` or `False`.

```python
x = 5
print(x == 5)
print(x == 6)
# True
# False
```

The place this bites is inside an `if`, which needs a *question*. Write it with one `=` and Python catches it:

```
x = 5
if x = 5:
    print("match")

SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
```

Python literally guesses your mistake: "Maybe you meant `==`". An `if` is asking whether something is true, so it needs the comparing `==`:

```python
x = 5
if x == 5:
    print("match")
# match
```

The rule: **assigning uses one `=`, asking uses two.** Any time you're comparing — in an `if`, in a `while` — you want `==`.

## Why the caret `^` points where it does

You've now seen it twice: the mistake is on one line, but Python names the line *after* it. This isn't Python being unhelpful — it's a clue about how it reads your code.

Python reads top to bottom, left to right, and stops at the first thing that **can't** make sense. When something is *missing* — a comma, a colon, a closing bracket — there's nothing to point *at*, because the mistake is a hole where a character should be. So Python points at the next thing it read, the thing that broke *because* of the hole.

Watch it happen. A comma is missing after the `8`:

```
seat_counts = [
    12,
    8
    15,
]

SyntaxError: invalid syntax. Perhaps you forgot a comma?
   8
   ^
```

Python names **the `8` line** and points the caret `^` right at the `8`. But look at that line alone: `8`. There is nothing wrong with `8` — it's a perfectly good number. The mistake lives in the *gap* between the `8` and the `15` below it, where a comma should be. Python could only point at the first thing that stopped making sense, which was the line after the hole. The fix is on the line the caret *didn't* mark:

```python
seat_counts = [
    12,
    8,
    15,
]
print(seat_counts)
# [12, 8, 15]
```

So here's the habit that turns these errors from baffling to easy: **read the line Python names, and the line right above it, as a pair.** A missing comma, colon, or bracket almost always lives at the end of the line *before* the one the caret points to.

## Before you panic, check these

Most syntax errors are one of a very short list. Before you change anything, walk down it:

1. **Parentheses and brackets** — does every `(`, `[`, and `{` have a partner? Count them left to right. An unclosed one usually points the error at the *next* line.
2. **Indentation** — do the lines that belong together start at the same column? Any tabs mixed in with spaces?
3. **The colon** — does every `if`, `for`, `while`, and `def` line end with `:`?
4. **Quotes** — is every `"` and `'` closed? Any stray apostrophe inside single quotes?
5. **Commas** — is anything missing a comma between items in a list or arguments to a function?
6. **`=` vs `==`** — inside an `if` or `while`, did you use `==` to compare?
7. **Spelling and case** — is it `print` not `Print`, `True` not `true`? Does the name match exactly what you defined?
8. **Read the flagged line *and the one above it*** — the real mistake is often on the line before the caret.

## Quick reference — the rules at a glance

### The rigid rules

- **Indentation groups code.** Use 4 spaces per level; lines that belong together share the same indent. Never mix tabs and spaces.
- **Block openers end with `:`** — `if`, `elif`, `else`, `for`, `while`, `def`.
- **Brackets and quotes come in pairs.** Every `(` `[` `{` and every `"` `'` needs its partner.
- **Commas separate items** — between list elements and between function arguments.
- **`True`, `False`, `None` are capitalized.** Keywords (`if`, `for`, `def`, ...) are lowercase.
- **Python is case-sensitive.** `Score` ≠ `score`; `Print` ≠ `print`.
- **One `=` assigns, two `==` compare.** An `if` needs `==`.

### The errors these cause

- `IndentationError: expected an indented block` — a block opener has nothing indented under it.
- `IndentationError: unexpected indent` — a line is indented but nothing opened a block.
- `TabError: inconsistent use of tabs and spaces` — you mixed tabs and spaces; switch to spaces only.
- `SyntaxError: expected ':'` — add a colon to the end of the `if`/`for`/`def` line.
- `SyntaxError: '(' was never closed` — an opener has no partner; count brackets, check the line it names.
- `SyntaxError: unmatched ')'` — one closing bracket too many.
- `SyntaxError: unterminated string literal` — a quote was opened and never closed.
- `SyntaxError: ... Perhaps you forgot a comma?` — a comma is missing; check the named line and the one above it.
- `SyntaxError: ... Maybe you meant '==' ... instead of '='?` — use `==` to compare inside an `if`.
- `NameError: name 'true' is not defined` — capitalize it (`True`), or check for a typo.

### The two habits worth the most

- **Always check the parentheses** — count openers and closers, and remember the error often points one line late.
- **Always check the indentation** — line up what belongs together, spaces only.
