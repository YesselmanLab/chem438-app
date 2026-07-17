# If / else
unit: 5

## Why you need `if`

Programs that only ever do the same thing every time aren't very useful. You want code that reacts: check something, then decide what to do. That's what `if` is for.

```python
password = "hunter2"

if password == "hunter2":
    print("Access granted")
# Access granted
```

The line `password == "hunter2"` is a comparison — it's either `True` or `False`. If it's `True`, the line below runs. If it's `False`, nothing happens at all:

```python
password = "wrong-guess"

if password == "hunter2":
    print("Access granted")

# (nothing is printed)
```

Nothing crashes, nothing prints. The `if` block was simply skipped.

## The `if` statement: condition, colon, indented body

Every `if` statement has three parts, always in this order:

1. the word `if`
2. a **condition** — an expression that's `True` or `False`
3. a **colon**, then one or more **indented** lines underneath — the body

```python
temperature = 75

if temperature > 70:
    print("It's warm")
# It's warm
```

- `if temperature > 70` — the condition
- `:` — required, marks the start of the body
- `    print("It's warm")` — the body, indented under the `if`

Leave off the colon and Python refuses to run the code at all:

```python
temperature = 75

if temperature > 70
    print("It's warm")

# SyntaxError: expected ':'
```

> **Common mistake: writing `if x = 5` instead of `if x == 5`.** A single `=` assigns a value; it doesn't compare anything. Python catches this for you:
> ```python
> x = 5
>
> if x = 5:
>     print("five")
>
> # SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
> ```
> Two equals signs (`==`) compare. One equals sign (`=`) assigns. Python's error message even tells you what it thinks you meant.

## Indentation defines the block

This is the rule that trips up almost everyone coming from another language: in Python, **indentation is not decoration — it is the syntax**. The indented lines under an `if` *are* the block that runs when the condition is `True`. There are no curly braces, no `begin`/`end`. Whitespace is the only thing that says "these lines belong together."

```python
score = 85

if score >= 60:
    print("You passed")
    print("Nice work")

print("Grading complete")
# You passed
# Nice work
# Grading complete
```

Both `print` lines are indented the same amount under `if`, so both belong to the `if` block — both run when the condition is `True`. The last `print` is *not* indented, so it's outside the `if` block entirely: it always runs, condition or no condition.

Now remove the indentation and see what happens:

```python
if 5 > 3:
print("yes")

# IndentationError: expected an indented block after 'if' statement on line 1
```

Python is telling you exactly what's missing: it expected an indented block right after the `if` on line 1, and didn't find one. The fix is to indent:

```python
if 5 > 3:
    print("yes")
# yes
```

> **Common mistake: mixing tabs and spaces.** If some of your indentation is tab characters and some is spaces — even if they *look* aligned in your editor — Python cannot tell how deeply a line is nested and refuses to guess. You'll see `TabError: inconsistent use of tabs and spaces in indentation`. The fix: pick spaces (the standard in Python) and use them everywhere. Almost every code editor can be set to insert spaces automatically when you press Tab — turn that setting on and this error disappears for good.

How much you indent doesn't matter as much as being **consistent** — 4 spaces is the standard everyone uses, so use 4 spaces.

## `else`: the catch-all

`else` runs when the `if` condition is `False`. It needs no condition of its own — it means "otherwise, do this":

```python
age = 15

if age >= 18:
    print("You can vote")
else:
    print("Not old enough yet")
# Not old enough yet
```

`else` always pairs with the `if` directly above it at the same indentation level, and it always ends in a colon with its own indented body.

> **Common mistake: thinking `else` needs a condition.** It doesn't — that's the whole point of `else`, it's the leftover case.
> ```python
> grade = 55
>
> if grade >= 60:
>     print("Pass")
> else grade < 60:
>     print("Fail")
>
> # SyntaxError: expected ':'
> ```
> Python expected a colon right after `else` and found `grade` instead. Drop the condition and it works:
> ```python
> grade = 55
>
> if grade >= 60:
>     print("Pass")
> else:
>     print("Fail")
> # Fail
> ```

> **Common mistake: writing `else if` (from other languages).** Python's keyword is one word: `elif`.
> ```python
> grade = 55
>
> if grade >= 60:
>     print("Pass")
> else if grade < 60:
>     print("Fail")
>
> # SyntaxError: expected ':'
> ```

## `elif`: choosing one of many

What if there are more than two possibilities? You could stack separate `if` statements — but that has a serious problem. Watch what happens with three separate `if`s:

```python
score = 95

if score >= 90:
    print("A")
if score >= 80:
    print("B")
if score >= 70:
    print("C")

# A
# B
# C
```

All three printed! That's because these are three *independent* `if` statements — Python checks each one on its own, and `95` really is `>= 90`, `>= 80`, and `>= 70` all at once. This is almost never what you want for a grading scale.

> **Misconception: "the first matching branch runs, then Python stops."** That's only true for `if`/`elif`/`else` chains. Plain, separate `if` statements have no relationship to each other at all — Python checks every single one, and every one whose condition is `True` runs its body.

`elif` (short for "else if") links the checks together into one chain. Python checks them top to bottom and **stops at the first one that's `True`** — the rest are skipped, even if they'd also be `True`:

```python
score = 95

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")
# A
```

Only `"A"` prints. Python checked `score >= 90`, found it `True`, ran that body, and skipped every other branch in the chain — it never even looked at `score >= 80`.

```python
score = 72

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")
# C   <- the FIRST true branch wins, the rest are skipped
```

`else` at the end catches anything that matched none of the conditions above it — it needs no condition, same as before.

## Order matters — a classic bug

Because Python stops at the *first* `True` branch in an `elif` chain, **the order you write your conditions in changes the result.** This is one of the most common real bugs beginners write, and it fails silently — no error, just wrong answers.

Here's a grading function with the branches in the wrong order:

```python
def grade(score):
    if score >= 70:
        return "C"
    elif score >= 80:
        return "B"
    elif score >= 90:
        return "A"
    else:
        return "F"

print(grade(95))
print(grade(85))
print(grade(72))
print(grade(50))

# C
# C
# C
# F
```

Every passing score comes back `"C"`. Why? `score >= 70` is checked *first*. A score of `95` is `>= 70`, so Python returns `"C"` immediately and never even reaches the `>= 80` or `>= 90` checks — they're unreachable for any score that also satisfies `>= 70`, which is all of them.

The fix: check the most specific / highest condition first, and work down.

```python
def grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "F"

print(grade(95))
print(grade(85))
print(grade(72))
print(grade(50))

# A
# B
# C
# F
```

The rule: **read your `elif` chain top to bottom exactly like Python does, and ask whether an earlier condition could ever "steal" a case meant for a later one.** When ranges overlap (like `>= 70` and `>= 90` both being true for a 95), broadest-last, narrowest-first is almost always what you want.

## Tracing an `elif` chain

Practice reading a chain the way Python does — one condition at a time, top to bottom, stopping at the first `True`.

```python
def describe_temp(temp):
    if temp < 32:
        return "freezing"
    elif temp < 65:
        return "cold"
    elif temp < 80:
        return "mild"
    else:
        return "hot"
```

Before reading on, predict what `describe_temp(75)` returns.

Walk it through: is `75 < 32`? No. Is `75 < 65`? No. Is `75 < 80`? Yes — return `"mild"`. Python never checks `else` because it already found a `True` branch.

```python
print(describe_temp(20))
print(describe_temp(50))
print(describe_temp(75))
print(describe_temp(90))

# freezing
# cold
# mild
# hot
```

- `20`: `20 < 32` is `True` right away — `"freezing"`.
- `50`: `50 < 32` is `False`, `50 < 65` is `True` — `"cold"`.
- `75`: `75 < 32` is `False`, `75 < 65` is `False`, `75 < 80` is `True` — `"mild"`.
- `90`: all three conditions are `False`, so `else` runs — `"hot"`.

Notice each condition only needs to rule out the temperatures *already checked above it* — that's why `elif temp < 65` alone (without also checking `temp >= 32`) correctly means "cold, and not freezing," since freezing was already handled and skipped.

## Nesting — and why to avoid it

You can put an `if` inside another `if`. This is called **nesting**:

```python
age = 25
has_ticket = True

if has_ticket:
    if age >= 18:
        print("Welcome, adult with a ticket")
    else:
        print("Welcome, minor with a ticket")
else:
    print("No entry without a ticket")
# Welcome, adult with a ticket
```

This works, but it's hard to read once you're two or three levels deep, and it's easy to indent something at the wrong level by mistake. Often you can flatten nested conditions using `and` / `or` instead:

```python
age = 25
has_ticket = True

if has_ticket and age >= 18:
    print("Welcome, adult with a ticket")
elif has_ticket and age < 18:
    print("Welcome, minor with a ticket")
else:
    print("No entry without a ticket")
# Welcome, adult with a ticket
```

Same result, one level of indentation instead of two. As a rule of thumb: if you find yourself nesting more than two levels deep, stop and ask whether combining conditions with `and`/`or`, or returning early (next section), would flatten things out.

## Early return from a function

Inside a function, `return` exits immediately — nothing after it in that function runs. This lets you handle special cases up front and get out, instead of nesting everything in `else` blocks:

```python
def price_of_ticket(age):
    if age < 5:
        return 0
    if age < 18:
        return 8
    return 12

print(price_of_ticket(3))
print(price_of_ticket(10))
print(price_of_ticket(30))
# 0
# 8
# 12
```

Notice there's no `else` anywhere, and it still works correctly. Once `age < 5` is `True`, `return 0` runs and the function is *over* — Python never even looks at the lines below it. For `age = 30`, both `if`s are `False`, so execution falls all the way through to the final `return 12`. Early returns like this are usually easier to read than deeply nested `if`/`else`.

## Combining conditions with `and` / `or`

You can put more than one condition into a single `if` using `and` (both must be `True`) or `or` (at least one must be `True`):

```python
username = "admin"
password = "1234"

if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Login failed")
# Login successful
```

```python
day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print("It's the weekend")
else:
    print("It's a weekday")
# It's the weekend
```

This is often clearer than nesting two separate `if` statements, and it says exactly what you mean: "both of these" or "either of these."

## One-line conditional expression

For simple cases — pick one of two values based on a condition — Python has a compact form you'll see often in other people's code:

```python
age = 20
status = "adult" if age >= 18 else "minor"
print(status)
# adult
```

Read it as: `status` is `"adult"` **if** `age >= 18` is `True`, **else** it's `"minor"`. It's the same idea as a full `if`/`else`, just squeezed onto one line and used as a value rather than a statement:

```python
temperature = 55
print("wear a coat" if temperature < 60 else "no coat needed")
# wear a coat
```

Reach for the one-liner only when both branches are short and simple. If either branch needs more than one line, use a full `if`/`else` instead — cramming logic onto one line to be clever makes it harder to read, not easier.

## Summary

- `if condition:` runs its indented body only when `condition` is `True`; the colon and the indentation are both required.
- Indentation is not style — it is what tells Python which lines belong to which block. Mixed tabs/spaces or missing indentation are real errors (`IndentationError`, `TabError`), not warnings.
- `else` catches whatever didn't match — it takes no condition of its own.
- `elif` chains multiple checks together and stops at the **first** `True` branch; separate `if` statements have no such relationship and can *all* run.
- Order inside an `elif` chain matters — put the most specific / narrowest conditions first, broadest last, or an early condition can silently swallow cases meant for a later one.
- Prefer flattening nested `if`s with `and`/`or`, or exiting early with `return`, over stacking several levels of indentation.
- `x if condition else y` is a compact way to pick between two values inline.

## Practice: predict before you run

For each, decide what prints before checking the logic against the code above.

```python
level = 3

if level == 1:
    print("Beginner")
elif level == 2:
    print("Intermediate")
elif level >= 3:
    print("Advanced")
else:
    print("Unknown")
```

```python
x = 10
y = 20

if x > y:
    print("x wins")
elif x < y:
    print("y wins")
else:
    print("tie")
```

```python
def shipping_cost(weight):
    if weight <= 1:
        return 5
    elif weight <= 5:
        return 10
    else:
        return 20

print(shipping_cost(1))
print(shipping_cost(5))
print(shipping_cost(6))
```

## Quick reference — what's available

### The shape

- `if condition:` — run the indented body only when `condition` is `True`
- `elif condition:` — checked only if every branch above it was `False`; use as many as you need
- `else:` — takes no condition of its own; runs when nothing above it matched
- `if` on its own is fine — `elif` and `else` are optional extras
- A chain stops at the **first** `True` branch; separate `if` statements are independent and can all run
- Order the branches narrowest-first, broadest-last, or an early one steals a later one's cases

### The colon and indentation rule

- Every `if` / `elif` / `else` line **must end in a colon** — no colon, `SyntaxError: expected ':'`
- The body is the **indented** lines under that colon — 4 spaces, the same amount on every line
- Un-indented lines below are outside the block and always run
- `elif` / `else` line up at the same indentation as their `if`
- No indented body at all — `IndentationError: expected an indented block after 'if' statement`
- Tabs mixed with spaces — `TabError: inconsistent use of tabs and spaces in indentation`; use spaces only
- `if x = 5:` — `SyntaxError`; `=` assigns, `==` compares
- `else if` — `SyntaxError`; Python's word is `elif`

### Early return

- `return value` inside a function exits it **immediately** — nothing below it in that function runs
- Handle the special cases with `if` + `return` at the top, then `return` the normal case last
- No `else` needed: if the `if` returned, the lines below were never reached
- Reach for it (or `and`/`or`) instead of stacking three levels of nested `if`

### Combining conditions

- `A and B` — `True` only when both are `True`
- `A or B` — `True` when at least one is `True`
- `not A` — flips `True` to `False` and back
- `==` `!=` `<` `<=` `>` `>=` — the comparisons that produce the `True`/`False` in the first place
- `if a and b:` often replaces an `if` nested inside an `if`

### The one-liner

- `a if condition else b` — a **value**, not a statement: it evaluates to `a` when the condition is `True`, otherwise `b`
- Assign it (`x = a if cond else b`) or drop it straight into a `print`
- Both branches must be single short expressions — anything longer belongs in a full `if`/`else`

### All together

```python
def entry_fee(age, member):
    if age < 0:
        return "invalid age"
    if member:
        return 0
    if age < 5 or age >= 65:
        return 4
    if age < 18:
        return 8
    return 12

print(entry_fee(-2, False))
print(entry_fee(40, True))
print(entry_fee(70, False))
print(entry_fee(15, False))
print(entry_fee(40, False))
# invalid age
# 0
# 4
# 8
# 12
```

```python
visitor_age = 15
is_member = False

if is_member and visitor_age >= 18:
    kind = "adult member"
elif is_member:
    kind = "young member"
elif visitor_age >= 18:
    kind = "adult guest"
else:
    kind = "young guest"

print(kind)
print("pays" if entry_fee(visitor_age, is_member) > 0 else "free")
# young guest
# pays
```
