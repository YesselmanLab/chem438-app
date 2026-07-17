# Variables & math
unit: 1

## Putting a value in a box: variables and `=`

```python
apples = 3
print(apples)
# 3
```

`apples` is a **variable** — a name that points to a value. The line `apples = 3` puts the value `3` into a box labeled `apples`. Read `=` out loud as "gets" or "is set to." Never read it as "equals."

> **Common mistake:** thinking `=` means "equals," like in algebra class. In Python, `x = 5` does not claim that x equals 5 forever — it's an instruction: "put 5 in the box called x, right now." The box can be emptied and refilled later.

Here's proof that `=` is not algebraic equality:

```python
x = 5
x = x + 1
print(x)
# 6
```

If `=` meant "equals," `x = x + 1` would say `5 = 6`, which is nonsense. But it's not an equation — it's two separate steps. Python reads the right side first (take the current value of `x`, which is 5, and add 1, getting 6), then stores that result back into `x`. The old value of `x` is gone the moment the new one is stored.

> Later you'll meet `==`, which really does check "are these equal?" (`5 == 5` gives `True`). That's a different tool for a different job — comparing, not storing. Keep `=` (assign) and `==` (compare) straight.

## Naming your variables

Rules Python enforces:

- names can contain letters, digits, and underscores (`_`)
- names cannot start with a digit
- names cannot contain spaces
- names are case-sensitive — `score` and `Score` are two different variables
- names cannot be one of Python's reserved words (`class`, `for`, `if`, `return`, `print` is fine to reuse but risky, and so on)

Style that makes code easier to read later:

- use lowercase words separated by underscores: `total_cost`, not `TotalCost` or `totalcost`
- use names that say what the value *is*: `tip_percent` beats `t`
- short names like `i`, `x`, `n` are fine for quick, throwaway calculations, but not for anything you'll reread

Case sensitivity in action:

```python
score = 10
Score = 20
print(score)
print(Score)
# 10
# 20
```

Two completely separate boxes, just because the capitalization differs. This trips people up constantly — pick one style and stick to it.

Now the invalid cases, with the real errors Python gives:

```python
2score = 5
# SyntaxError: invalid decimal literal
```

A name can't start with a digit — Python starts reading `2score` as a number and chokes on the letters that follow. Fix it by moving the digit, or dropping it:

```python
score2 = 5
print(score2)
# 5
```

Reserved words fail too:

```python
class = "Organic"
# SyntaxError: invalid syntax
```

`class` is a keyword Python uses for its own purposes (building classes), so you can't use it as a variable name.

## Two kinds of numbers: int and float

```python
count = 3
price = 3.0
print(count)
print(price)
print(type(count))
print(type(price))
# 3
# 3.0
# <class 'int'>
# <class 'float'>
```

An **int** is a whole number, no decimal point: `3`, `-12`, `0`. A **float** has a decimal point, even if it's `.0`: `3.0`, `-12.5`, `0.0`. Python tracks this difference automatically based on how you write the number, and it matters — some operators behave differently depending on which kind of number you're using, as you'll see below.

## The basic math operators

```python
a = 10
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b)
# 13
# 7
# 30
# 3.3333333333333335
```

`+` adds, `-` subtracts, `*` multiplies, `/` divides. Nothing surprising yet — except notice that last line. We'll come back to why `/` gave a long decimal instead of a clean fraction.

## Order of operations

Python follows the same order-of-operations rules you learned in math class: exponents first, then multiplication/division, then addition/subtraction, left to right, and parentheses override everything.

```python
print(2 + 3 * 4)
print((2 + 3) * 4)
# 14
# 20
```

Multiplication happens before addition unless you force otherwise with parentheses.

Predict the output of this line before you read on: `2 + 3 * 4 ** 2`

```python
print(2 + 3 * 4 ** 2)
# 50
```

Here's why: `**` (exponent) runs first, so `4 ** 2` becomes `16`. Then multiplication: `3 * 16` becomes `48`. Then addition: `2 + 48` gives `50`. When you're not sure how an expression will be grouped, add parentheses — it costs nothing and removes all doubt.

## Floor division and remainder: `//` and `%`

```python
x = 7
y = 2
print(x / y)
print(x // y)
print(x % y)
# 3.5
# 3
# 1
```

`/` is regular division. `//` is **floor division** — it divides and throws away everything after the decimal point, keeping only the whole number. `%` is the **remainder** — what's left over after floor division.

A concrete use: splitting pizza slices evenly.

```python
slices = 17
people = 5
print(slices // people)
print(slices % people)
# 3
# 2
```

Each person gets 3 whole slices (`//`), and 2 slices are left over (`%`). Between them, `//` and `%` always account for every slice.

Predict before you check: what do `22 // 6` and `22 % 6` give?

```python
print(22 // 6)
print(22 % 6)
# 3
# 4
```

`6 * 3 = 18`, and `22 - 18 = 4` left over — matches.

## Exponents: `**`

```python
print(2 ** 3)
print(5 ** 2)
print(2 ** 0.5)
# 8
# 25
# 1.4142135623730951
```

`**` raises a number to a power. `2 ** 0.5` computes a square root (raising to the `0.5` power), which is why you get a long decimal — the square root of 2 isn't a clean number.

> **Common mistake:** using `^` for "to the power of," the way some calculators do. In Python, `^` is a completely different operator (bitwise XOR — a bit-level operation you won't need in this course). `2 ^ 3` runs without any error and quietly gives `1`, not `8`. That's worse than a crash: the code looks fine and gives a wrong answer with no warning. Always use `**` for exponents.

## Division always gives a float

```python
print(10 / 2)
print(4 / 2)
# 5.0
# 2.0
```

Both of those divide evenly, with no remainder — and Python still hands back a float, `5.0` and `2.0`, not `5` and `2`. In Python 3, `/` **always** produces a float, no matter what. Compare with `//`:

```python
print(10 // 2)
# 5
```

Same numbers, but `//` on two ints gives back an int.

> **Common mistake:** expecting `/` to give a whole number when the division happens to come out even. It never does. If your program needs a whole number, use `//`, or wrap the result in `int()` (see below).

## `int()` truncates, `round()` rounds

```python
print(int(3.9))
print(int(3.1))
# 3
# 3
```

> **Common mistake:** assuming `int()` rounds to the nearest whole number. It does not. `int()` **truncates** — it chops off everything after the decimal point, no matter how close that decimal was to rounding up. `int(3.9)` is `3`, not `4`, even though `3.9` is almost `4`.

Predict this one before you look: what does `int(-2.7)` give? (Hint: it's not `-3`.)

```python
print(int(-2.7))
# -2
```

`int()` truncates *toward zero*, not "down." For negative numbers, that means it rounds toward 0, so `-2.7` becomes `-2`, not `-3`.

If you actually want rounding, use `round()` instead:

```python
print(round(3.9))
print(round(3.1))
print(round(3.5))
# 4
# 3
# 4
```

> **Watch out:** Python rounds an exact `.5` to the nearest *even* number, not always up. `round(2.5)` gives `2`, not `3`.

```python
print(round(2.5))
# 2
```

This surprises almost everyone the first time. It rarely matters in day-to-day code, but if you ever get a rounding result that looks "wrong" by one, this is probably why.

## Handy math functions: `abs()`, `round()`, `min()`, `max()`

```python
print(abs(-7))
print(abs(7))
print(round(3.14159, 2))
print(min(4, 9, 1))
print(max(4, 9, 1))
# 7
# 7
# 3.14
# 1
# 9
```

`abs()` strips the sign off a number — always non-negative. `round()` with a second argument rounds to that many decimal places (`round(3.14159, 2)` keeps 2 digits after the point). `min()` and `max()` take any number of values and return the smallest or largest.

## Augmented assignment: shortcuts like `+=`

```python
score = 10
score += 5
print(score)
# 15
```

`score += 5` is shorthand for `score = score + 5`. It updates a variable using its own current value, in one step. All four basic operators have a shortcut version:

```python
score = 10
score += 5
print(score)

score -= 3
print(score)

score *= 2
print(score)

score /= 4
print(score)
# 15
# 12
# 24
# 6.0
```

Notice the last line: `score /= 4` uses `/`, so the result becomes a float (`6.0`), even though `score` started as an int.

## Reassignment: a variable only remembers its last value

```python
temp = 98.6
print(temp)
temp = 101.2
print(temp)
# 98.6
# 101.2
```

`temp` doesn't remember `98.6` once it's been reassigned. Each assignment completely overwrites what was in the box — the old value isn't stored anywhere unless you explicitly saved it somewhere else first.

> **Common mistake:** expecting a variable to keep a history of everything it's been set to. It doesn't — a variable is one box, and it only ever holds what you last put in it. If you need to keep the old value, assign it to a *different* variable before overwriting the original: `old_temp = temp` then `temp = 101.2`.

## `print()` versus the value itself

```python
5 + 3
print(5 + 3)
# 8
```

Only one line of output there, not two. If this were saved in a script file and run with `python3 file.py`, the first line computes `8` and immediately throws the result away — nothing appears on screen, because nothing told Python to display it. The second line uses `print()`, which explicitly puts text on the screen. The same is true for variables:

```python
price = 19.99
price
print(price)
# 19.99
```

The bare `price` on its own line computes nothing new and shows nothing in a script. If you want to see a value while your program runs, you must `print()` it.

## Errors you will meet (and what they mean)

```python
print(total)
# NameError: name 'total' is not defined
```

This means you tried to use a variable that doesn't exist yet — either you never created it, or you misspelled its name. Python does not guess what you meant; it only knows about variables that have already been assigned earlier in the program.

```python
name = "Sam"
age = 25
print(name + age)
# TypeError: can only concatenate str (not "int") to str
```

`+` between two strings glues them together. `+` between a string and a number is ambiguous — should it add, or paste text? Python refuses rather than guess. Fix it by converting the number to a string first:

```python
name = "Sam"
age = 25
print(name + " is " + str(age))
# Sam is 25
```

`str()` converts a value into its text form so `+` can glue it onto other text.

## Putting it all together

A receipt split between friends, using several ideas from this page at once:

```python
bill = 47.50
tip_percent = 18
people = 3

tip = bill * tip_percent / 100
total = bill + tip
per_person = total / people

print(round(tip, 2))
print(round(total, 2))
print(round(per_person, 2))
# 8.55
# 56.05
# 18.68
```

`bill * tip_percent / 100` runs left to right at the same precedence level: multiply first (`47.50 * 18 = 855.0`), then divide (`855.0 / 100 = 8.55`). Every result is rounded to 2 decimal places before printing, because raw float math can leave tiny leftover digits you don't want to show someone splitting a bill.

A countdown timer, using floor division and remainder together:

```python
total_seconds = 500
minutes = total_seconds // 60
seconds = total_seconds % 60
print(minutes, "minutes and", seconds, "seconds")
# 8 minutes and 20 seconds
```

`//` gives the whole minutes, `%` gives the seconds left over once those minutes are removed — the same pattern as splitting pizza slices, just with 60 instead of a group of people. This pairing, `//` for "how many whole groups" and `%` for "what's left over," shows up constantly once you start writing real programs.

## Quick reference — what's available

### Arithmetic operators

- `a + b` — add
- `a - b` — subtract
- `a * b` — multiply
- `a / b` — divide; **always** gives a float, even when it comes out even
- `a // b` — floor division: divide and keep only the whole part
- `a % b` — remainder left over after floor division
- `a ** b` — a to the power of b (`**`, never `^`)
- order: `**` first, then `* / // %`, then `+ -`, left to right; parentheses override everything

### int vs float

- `3` is an int — a whole number, no decimal point
- `3.0` is a float — has a decimal point, even when the part after it is zero
- int `+ - * // % **` int gives an int; `/` gives a float
- mix an int and a float in any operation and the result is a float
- `3 == 3.0` is `True` — same value, different type

### Number built-ins

- `abs(x)` — distance from zero; strips the sign
- `round(x)` — round to a whole number (exact `.5` goes to the nearest *even*)
- `round(x, n)` — round to `n` decimal places
- `min(a, b, ...)` — smallest of the values you give it
- `max(a, b, ...)` — largest of the values you give it
- `int(x)` — convert to an int by truncating *toward zero* (does not round)
- `float(x)` — convert to a float
- `str(x)` — convert to text, so `+` can glue it onto other text
- `type(x)` — tells you which kind of value you have
- `print(x)` — show a value on screen; without it, nothing is displayed

### Augmented assignment

- `x += 5` — same as `x = x + 5`
- `x -= 5`, `x *= 5`, `x /= 5`, `x //= 5`, `x %= 5`, `x **= 5` — same idea for the other operators
- `x /= 5` makes `x` a float, because `/` always does

Several of them together:

```python
n = -7.6
print(abs(n))
print(round(n))
print(round(n, 1))
print(int(n))
print(float(3))
print(type(3))
print(type(3.0))
print(min(4, 9, 1), max(4, 9, 1))
# 7.6
# -8
# -7.6
# -7
# 3.0
# <class 'int'>
# <class 'float'>
# 1 9
```

And the shortcuts, one after another:

```python
total = 0
total += 10
total //= 3
print(total)      # 3   <- 10 // 3 keeps only the whole part
print(3 == 3.0)   # True <- same value, even though one is int and one is float
```
