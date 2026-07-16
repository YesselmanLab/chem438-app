# Booleans & comparisons
unit: 4

Every question you can ask about your data — is this bigger, does this match,
is this list empty — comes down to one of two answers: True or False. This page
covers how Python represents those answers, how to build them with comparisons,
and how to combine them. The next reference page uses everything here to make
decisions with if/else, but you will be surprised how much you can already do
with booleans alone, no if/else required.

## True and False

```python
print(True)            # True
print(False)             # False
print(type(True))          # <class 'bool'>
```

`True` and `False` are capitalized, and there are exactly two of them. Not
`"true"`, not `"TRUE"`, not the strings `"True"` or `"False"` — the real thing,
with no quotes at all.

> **Common mistake:** thinking `True` and `"True"` are the same value. One is a boolean, the other is a three-character string, and Python treats them as completely different things.

```python
print(type(True))         # <class 'bool'>
print(type("True"))         # <class 'str'>
print(True == "True")         # False
```

## Comparison operators

Six operators ask a yes/no question about two values:

- `==` — equal to
- `!=` — not equal to
- `<` — less than
- `>` — greater than
- `<=` — less than or equal to
- `>=` — greater than or equal to

```python
x = 7
print(x == 7)      # True
print(x != 7)        # False
print(x > 5)           # True
print(x < 5)             # False
print(x >= 7)              # True
print(x <= 6)                 # False
```

Each line asks a question and Python answers with `True` or `False`. Nothing
gets stored here — it just prints and is gone. That changes in the next section.

Predict each of these for yourself before reading the comment:

```python
score = 82
print(score > 90)       # False
print(score >= 82)        # True
print(score != 82)          # False
```

## A comparison is already a value

This is the single most useful fact on this whole page: a comparison does not
just get printed and vanish. It produces a real value, `True` or `False`, and
you can store it, pass it to a function, or hand it back as a `return` value,
exactly like a number or a string.

```python
age = 20
is_adult = age >= 18
print(is_adult)               # True
print(type(is_adult))           # <class 'bool'>

can_vote = age >= 18
print(is_adult == can_vote)       # True   <- just two booleans, compared like anything else
```

`is_adult` is not special. It is a plain value sitting in a variable. You will
lean on this constantly: whenever you're about to write `if <something>: return
True`, ask whether `<something>` is already the answer you want to return.

## Assignment vs. question: `=` and `==`

One equals sign **stores** a value. Two equals signs **ask** whether two values
are the same. Mixing them up is probably the most common beginner slip in
Python — and the good news is Python usually stops you before it runs.

```python
age = 20            # stores: age now holds 20
print(age)             # 20

print(age == 20)          # asks: is age 20?  -> True
print(age == 21)            # asks: is age 21?  -> False
```

> **Common mistake:** typing `=` when you mean `==`. Python parses `=` as "store this," and refuses to run when it finds a bare `=` somewhere that expects a yes/no question instead.

```python
age = 20
if age = 21:
    print("birthday!")

# SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
```

if/else itself is the topic of the next reference page — all that matters here
is that `=` means "store," everywhere, including inside a condition, and Python
catches the mistake instead of silently doing the wrong thing. Read that error
message closely: it is telling you exactly what to change.

- `=` stores. The left side must be a variable name.
- `==` asks. Either side can be any value or expression.
- If you ever see `SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?`, you typed `=` where Python wanted a question.

## You almost never need if/else for this

Because a comparison is already `True` or `False`, you rarely need to spell out
the obvious with if/else. Compare these two ways of writing the same function.

```python
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
```

```python
def is_even(n):
    return n % 2 == 0

print(is_even(4))       # True
print(is_even(7))         # False
```

`n % 2 == 0` is already `True` or `False`. The first version takes that answer
and returns... the exact same answer, four lines later. Whenever you catch
yourself writing `if <condition>: return True` / `else: return False`, delete
the scaffolding and `return` the condition itself.

> **Common mistake:** believing a function that returns True or False must use if/else. You only need if/else when the two branches genuinely do different things — computing a boolean directly is not one of those cases.

```python
def can_vote(age):
    return age >= 18

print(can_vote(20))       # True
print(can_vote(15))         # False
```

## Comparing different types

`==` never crashes when the types differ. It just tells you honestly that they
are not equal.

```python
print(2 == "2")        # False
print(2 == 2)             # True
print("2" == "2")           # True
print(2 == 2.0)               # True   <- int and float do compare equal
```

> **Common mistake:** expecting `2 == "2"` to be True because "they look the same." A number and a string are different types, and `==` never converts one into the other just to make the comparison work.

```python
print(2 == "2")     # False
```

Equality is always safe, but **ordering** (`<`, `>`, `<=`, `>=`) between
incompatible types is not. Python has no rule for "is a number less than some
text," so it refuses outright:

```python
print(2 < "2")

# TypeError: '<' not supported between instances of 'int' and 'str'
```

One more type quirk worth knowing: `True` and `False` are secretly numbers
underneath — `True` is `1`, `False` is `0`.

```python
print(True == 1)       # True
print(False == 0)         # True
print(True + True)          # 2
```

## Truthiness — what counts as True or False

Python can treat almost any value as if it were True or False, even outside a
comparison. This matters once you reach if/else and loops, so it is worth
seeing now while it is fresh. Some values act like False — they are "falsy" —
and everything else is "truthy."

```python
print(bool(""))            # False
print(bool("hello"))         # True
print(bool(0))                  # False
print(bool(5))                    # True
print(bool(-3))                     # True   <- any nonzero number is truthy, even negative
print(bool([]))                       # False
print(bool([1, 2, 3]))                  # True
```

- Falsy: `""` (empty string), `0`, `0.0`, `[]` (empty list), `None`.
- Truthy: almost everything else — non-empty strings, nonzero numbers, non-empty lists.

`bool()` is the function that reveals the truthy/falsy nature of any value. You
won't call it directly very often, but if/else and loops (both coming soon)
apply this rule automatically.

## Combining conditions: `and`, `or`, `not`

Real questions are rarely just one comparison. `and`, `or`, and `not` build
bigger questions out of smaller ones.

`not` flips a boolean:

```python
print(not True)        # False
print(not False)         # True
```

`and` is True only when **both** sides are True — here is every combination:

```python
print(True and True)         # True
print(True and False)          # False
print(False and True)            # False
print(False and False)             # False
```

`or` is True when **at least one** side is True:

```python
print(True or True)         # True
print(True or False)          # True
print(False or True)            # True
print(False or False)             # False
```

Predict this one before you check the comment:

```python
x = 3
print(x > 5 and x < 10)        # False   <- x > 5 is False, so the whole thing is False
print(x > 5 or x < 10)           # True    <- x < 10 is True, so the whole thing is True
```

## The `and` / `or` trap: write a complete comparison on both sides

This is the sneakiest bug on this whole page, and nearly everyone writes it at
least once.

> **Common mistake:** writing `a or b == 10` and reading it as "a or b is 10." Python does not read it that way. `==` binds tighter than `or`, so this is actually `a or (b == 10)`. If `a` happens to be truthy, Python hands back `a` itself, not True or False, and never even looks at `b`.

```python
a = 3
b = 10
print(a or b == 10)        # 3     <- NOT True! or returns a itself; b == 10 never runs
```

Compare that to the version that really asks "is a 10, or is b 10?" — a
complete comparison on **both** sides of `or`:

```python
a = 3
b = 10
print(a == 10 or b == 10)        # True
```

The same trap exists with `and`:

```python
n = 3
print(n == 3 and 5)        # 5     <- NOT True! and returns 5 itself, not a yes/no answer

print(n == 3 and n == 5)     # False
```

- Every side of `and` / `or` must already be a complete True/False question on its own.
- `a or b == 10` is wrong. `a == 10 or b == 10` is right.
- A variable that already **holds** True or False (a flag) is fine to use bare — it is a bare number or string that isn't already a comparison that causes the trap. `score >= 70 and passed_written` is fine if `passed_written` is already True or False.

## Membership: `in` and `not in`

`in` asks whether a value shows up inside another value — a list, or a string.

```python
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)        # True
print("mango" in fruits)           # False
```

On a string, `in` checks for a substring:

```python
print("an" in "banana")        # True    <- "banana" contains the letters "an"
print("xyz" in "banana")         # False
```

`not in` is the opposite:

```python
print("mango" not in fruits)        # True
print("banana" not in fruits)         # False
```

`in` on a list checks whole elements, not pieces of them — this trips people up
coming straight from the string example above:

```python
print("an" in fruits)        # False   <- "an" is not one of the three elements
```

## Chained comparisons

Python lets you chain comparisons the way you would on paper, instead of
writing `and` twice.

```python
x = 5
print(0 < x < 10)        # True    <- same as: 0 < x and x < 10
print(0 < x < 3)           # False
```

```python
temp = 72
print(65 <= temp <= 80)        # True    <- comfortable range
print(65 <= 95 <= 80)            # False
```

## Putting it together

Two examples that combine everything above — no if/else anywhere, because none
of it is needed.

```python
def valid_password(pw):
    return len(pw) >= 8 and pw != "password" and "123" not in pw

print(valid_password("hunter2"))          # False -- too short
print(valid_password("longenough"))         # True
print(valid_password("password"))             # False -- banned exactly
print(valid_password("abc123def"))               # False -- contains "123"
```

```python
def can_sit(row, occupied_rows, max_row):
    return row not in occupied_rows and 0 <= row <= max_row

occupied = [3, 4, 7]
print(can_sit(5, occupied, 10))         # True
print(can_sit(3, occupied, 10))           # False -- already taken
print(can_sit(15, occupied, 10))            # False -- past the last row
```

## Summary

- `True` and `False` are capitalized booleans, not strings — `True != "True"`.
- `==`, `!=`, `<`, `>`, `<=`, `>=` compare two values and produce True or False.
- `=` stores, `==` asks. Using `=` where Python expects a question raises `SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?`.
- A comparison is already a value — store it, print it, or `return` it. You rarely need if/else just to hand back True or False.
- `==` across different types is always safe and usually False; ordering (`<`, `>`, `<=`, `>=`) across incompatible types raises a `TypeError`.
- Empty strings, `0`, and empty lists are falsy; almost everything else is truthy.
- `and`, `or`, `not` combine booleans. Every side of `and` / `or` needs its own complete comparison — `a or b == 10` is not "a or b is 10."
- `in` / `not in` test membership: an element in a list, or a substring in a string.
- Chained comparisons like `0 < x < 10` read naturally and mean exactly what they look like.
