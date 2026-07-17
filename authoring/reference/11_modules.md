# Modules & imports
unit: 10

## What a module is

Everything you have written so far, you wrote yourself. That does not scale. Square roots, random numbers, averages, plotting, spreadsheets — thousands of people have already written that code, tested it for years, and left it lying around for you to use.

A **module** is exactly that: a file of someone else's Python code that you can pull into your own program. You don't copy it, you don't retype it, and you don't need to understand how it works inside. You just ask for it by name and start using it.

The keyword that asks is `import`.

```python
import math
print(math.sqrt(16))   # 4.0
```

Two lines. The first one hands you every function in Python's math library. The second one uses one of them. You did not write `sqrt`, you will never see its code, and it works.

This page is the bridge. Up to now you have been living in "base Python" — the handful of things available with no setup at all. From here on, essentially every useful thing in this course arrives through an `import` line.

## Importing a module: `import math`

`import math` means: find the module named `math`, load it, and give me a variable called `math` that holds everything in it.

After that line, `math` is a name in your program, just like any variable you make with `=`. The difference is what's inside it — not one value, but a whole collection of functions and constants, which you reach with a dot.

```python
import math

print(math.sqrt(25))   # 5.0
print(math.pi)         # 3.141592653589793
print(math.floor(3.9)) # 3
print(math.ceil(3.1))  # 4
```

Read `math.sqrt` out loud as "math's sqrt" or "the sqrt that lives in math." The dot means "look inside." It is the same dot you already met in `"hello".upper()` — reach into something and grab a piece of it.

`math` is part of Python's **standard library**: about 200 modules that ship with Python itself. You never install them. They're already on your machine, sitting there unloaded until you ask.

## Dot notation is not optional

Here is the misconception that costs beginners the most time.

> **Common mistake:** thinking `import math` makes `sqrt()` available as a bare name. It does not. `import math` gives you exactly one new name — `math`. Everything else is *inside* it, and you have to go through the dot to get there.

Proof:

```python
import math
print(sqrt(16))
```

```
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
NameError: name 'sqrt' is not defined
```

The import worked perfectly. `math` is loaded and ready. But `sqrt` on its own is not a name your program knows, so Python does exactly what it does for any variable you never created — `NameError: name 'sqrt' is not defined`.

The fix is the dot:

```python
import math
print(math.sqrt(16))   # 4.0
```

If you see `NameError` on something you're sure you imported, this is almost always why. You imported the module but called the function as if it were bare.

## Why `math.sqrt(x)` beats `x ** 0.5`

You already know `x ** 0.5` computes a square root. So why import anything?

For the easy cases, they agree exactly:

```python
import math
print(math.sqrt(16))   # 4.0
print(16 ** 0.5)       # 4.0
print(math.sqrt(2))    # 1.4142135623730951
print(2 ** 0.5)        # 1.4142135623730951
```

Identical. The difference shows up when something goes wrong. Ask for the square root of a negative number:

```python
import math
math.sqrt(-4)
```

```
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
ValueError: math domain error
```

`math.sqrt` refuses. It knows real square roots of negatives don't exist and stops your program right at the line that made the mistake. Now the same thing with `**`:

```python
print((-4) ** 0.5)   # (1.2246467991473532e-16+2j)
```

No error. It quietly hands back a **complex number** — that `2j` on the end — and your program keeps running, carrying a value that is not a number in any sense you meant. Every calculation downstream is now wrong, and nothing told you.

That is the real argument. A crash you can find in ten seconds beats a silently wrong answer you find in a week, or never.

There's a plainer reason too: `math.sqrt(area)` says *square root* to anyone reading it. `area ** 0.5` makes the reader stop and decode. Use the named function.

## `from math import sqrt`

There's a second form of import that pulls one specific name straight into your program, skipping the dot.

```python
from math import sqrt
print(sqrt(16))   # 4.0
```

Read it as a sentence: "from math, import sqrt." Now `sqrt` *is* a bare name you can call, because you explicitly asked for it by name.

You can grab several at once:

```python
from math import sqrt, pi, floor
print(sqrt(81))    # 9.0
print(pi)          # 3.141592653589793
print(floor(2.9))  # 2
```

Notice what you did **not** get:

```python
from math import sqrt
print(ceil(3.2))
```

```
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
NameError: name 'ceil' is not defined
```

`from math import sqrt` brings in `sqrt` and nothing else. Not `ceil`, not `pi`, and not `math` itself. You asked for one thing; you got one thing.

So which form should you use? Prefer plain `import math`. The dot tells the reader where a function came from, and it keeps module names from colliding with your own variables. `from math import sqrt` is fine when you use one function constantly and the name is unambiguous. You will see both everywhere, so recognize both.

## Renaming with `as`

You can give an imported module a different, shorter name using `as`:

```python
import math as m
print(m.sqrt(49))   # 7.0
print(m.pi)         # 3.141592653589793
```

`import math as m` means "load math, but call it `m` in my program." The module didn't change; only your nickname for it did. `m.sqrt` and `math.sqrt` are the same function.

This looks like a pointless typing shortcut until you meet the libraries the rest of this course runs on. There, the nickname is a **convention** — a name essentially every Python programmer on earth uses for that library:

```
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```

Those three lines open almost every scientific Python file ever written. `np.mean(...)`, `pd.read_csv(...)`, `plt.plot(...)` — when you see `np.` in someone's code, you know instantly that it's numpy. Nobody writes `import numpy as tofu`. It would work, and every reader would hate you.

(Those three aren't runnable on this page — they're big libraries that need a moment to load. You'll meet them in the lectures where they get used.)

> **Common mistake:** thinking `np` is a special Python word. It isn't. It is a nickname *you* create on the `import` line, and it exists only because you wrote `as np`. Skip that line and `np` means nothing:

```python
print(np.mean([1, 2, 3]))
```

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'np' is not defined
```

Same `NameError` as always. `np` is just a variable, and you never made it.

## Module name vs. the name you use

Keep two ideas apart:

- the **module name** — what the module is actually called on disk (`math`, `numpy`, `statistics`). This is what Python goes looking for.
- the **name you use** — what you type in your code afterward.

Usually they're the same. `as` makes them differ:

```python
import statistics as stats
print(stats.mean([2, 4, 6]))   # 4
```

Python searched for a module named `statistics`. If you'd written `import stats`, it would have gone looking for a file called `stats` and failed — no such module exists. The nickname is something you invent *after* the real module is found, never a substitute for its real name.

## `import` goes at the top of the file

Technically an `import` can sit anywhere. By convention it goes at the very top, above everything else:

```python
import math
import random

def circle_area(radius):
    return math.pi * radius ** 2

print(round(circle_area(3), 2))   # 28.27
```

Two reasons, both practical. First, anyone opening the file sees in one glance what it depends on. Second, a module must be imported *before* the line that uses it — Python reads top to bottom, and an import buried at line 80 does nothing for line 30. Run this as a fresh file, top to bottom:

```
print(math.sqrt(4))
import math
```

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'math' is not defined
```

The import is right there, one line later, and it doesn't help. When line 1 runs, `math` doesn't exist yet.

That example is shown as text rather than as a Run button on purpose, and the reason is worth knowing. This page already ran `import math` several sections ago, and once a module is loaded it **stays** loaded for the rest of the session — so pasting those two lines here would print `4.0` and prove nothing. The `NameError` above is what a genuinely fresh program does. Notebooks like Colab work the same way: a stray import you ran an hour ago in some other cell keeps your code working until you restart, and then it breaks for the next person. Imports at the top of the file, always, and you never think about this again.

## Importing runs the module once

An `import` isn't just a label. Python finds the file, **runs** it top to bottom, and stores the result. That's why the first import of a big library takes a moment.

The important part: it happens **once**. Import the same module ten times and Python does the work once and hands back the same loaded module every other time.

```python
import sys
import math
import math
import math
print("math" in sys.modules)   # True
```

`sys.modules` is Python's record of what it has already loaded. After the first `import math`, `math` is in there, and the next two imports are near-instant lookups — no re-running, no cost. So you never have to worry about "importing too much" or importing the same thing in two files. Say what you need and let Python handle it.

## `random` — and why you must seed it

The `random` module makes random values. It's also the module where you'll first hit a real problem: random output is different every run, so you can't check your answer against anything.

The fix is `random.seed(n)`. A computer's "random" numbers aren't truly random — they come from a formula, and the seed is that formula's starting point. Same seed, same sequence, every single time, on every machine.

```python
import random

random.seed(1)
print(random.randint(1, 6))   # 2
print(random.randint(1, 6))   # 5
print(random.randint(1, 6))   # 1
```

Run that a thousand times and you get 2, 5, 1 a thousand times. Delete the `seed(1)` line and you'd get three different numbers on every run — which is exactly what you want in a real dice game, and exactly what you don't want when you're trying to test your code or print a stable answer in a reference page.

**Seed when you need to reproduce a result. Don't seed when you want real unpredictability.** That's the whole rule.

`randint(a, b)` gives a whole number from `a` to `b`, and **both ends are included** — `randint(1, 6)` really can give 6. That's unusual for Python, where ranges normally exclude the endpoint, so it's worth remembering.

`choice` picks one item out of a list:

```python
import random

random.seed(1)
print(random.choice(["rock", "paper", "scissors"]))   # rock
```

`shuffle` reorders a list **in place** — it changes the list you hand it and returns `None`:

```python
import random

random.seed(1)
deck = [1, 2, 3, 4, 5]
random.shuffle(deck)
print(deck)   # [3, 4, 5, 1, 2]
```

> **Common mistake:** writing `deck = random.shuffle(deck)`. `shuffle` has no `return` statement — like any such function, it hands back `None`. So you'd throw away your shuffled list and set `deck` to `None`. Call it on its own line and read the list afterward.

```python
import random

random.seed(1)
deck = [1, 2, 3, 4, 5]
deck = random.shuffle(deck)
print(deck)   # None
```

Reseeding rewinds the sequence — proof that the seed really is the starting point and nothing else:

```python
import random

random.seed(1)
print(random.randint(1, 6))   # 2
random.seed(1)
print(random.randint(1, 6))   # 2
```

Same seed, same first number. The generator has no memory beyond where the seed put it.

## `statistics` — mean and median

For everyday averages, the `statistics` module beats writing the math yourself:

```python
import statistics

scores = [88, 92, 79, 95]
print(statistics.mean(scores))     # 88.5
print(statistics.median(scores))   # 90.0
```

`mean` is the average — add them up, divide by how many. `median` is the middle value once sorted (with an even count, the average of the middle two). They can disagree wildly, and that's the point of having both:

```python
import statistics

pay = [30, 32, 35, 33, 900]
print(statistics.mean(pay))     # 206
print(statistics.median(pay))   # 33
```

One huge value drags the mean to 206, a number describing nobody in the list. The median shrugs it off. When someone quotes an "average," this is why it matters which one they meant.

## When Python can't find it: `ModuleNotFoundError`

Ask for a module that doesn't exist and you get a distinct error:

```python
import mathh
```

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'mathh'
```

`ModuleNotFoundError` means one thing: Python looked everywhere it knows to look and found nothing by that name. It is almost never a mystery. It's one of:

- **a typo** — `mathh`, `randon`, `statisitcs`. Check the spelling first; this is most of them.
- **wrong capitalization** — module names are case-sensitive. `import Math` fails; it's `math`.
- **a library that isn't installed** — real for big outside libraries, never for standard-library modules like `math`.

> **Common mistake:** thinking you have to install `math` (or `random`, or `statistics`) before you can use it. You don't. They ship with Python. If `import math` raises `ModuleNotFoundError`, you have a typo — not a missing install.

Note the difference between the two errors on this page. `ModuleNotFoundError` means the *module* isn't there. `NameError` means the module is fine but the *name you used* isn't — usually a missing dot, or an import you forgot to write.

For libraries that genuinely don't ship with Python, you install them once with `pip` — and in Google Colab, where this course runs, numpy, pandas, and matplotlib are already installed, so you just `import` them and go.

## Putting it together

A quiz simulator using all three modules at once:

```python
import math
import random
import statistics

random.seed(1)

def random_scores(n):
    return [random.randint(50, 100) for _ in range(n)]

def summarize(scores):
    return {
        "mean": round(statistics.mean(scores), 1),
        "median": statistics.median(scores),
        "spread": max(scores) - min(scores),
        "rms": round(math.sqrt(statistics.mean([s ** 2 for s in scores])), 1),
    }

scores = random_scores(8)
print(scores)
print(summarize(scores))
# [58, 86, 98, 54, 66, 57, 81, 98]
# {'mean': 74.8, 'median': 73.5, 'spread': 44, 'rms': 76.7}
```

Three imports at the top. One seed, so the output is identical every run. `math.sqrt`, `random.randint`, and `statistics.mean` each reached through their module's dot. Every function in that code was written by someone else — you just assembled them.

## Quick reference — what's available

### The import forms

- `import math` — loads the module; use everything through the dot: `math.sqrt(x)`.
- `from math import sqrt` — brings `sqrt` in as a bare name. Nothing else comes with it.
- `from math import sqrt, pi, floor` — several names at once.
- `import math as m` — loads math, nicknames it `m`. Same module, shorter name.
- `import numpy as np` — the convention you'll see constantly. `np` exists only because of the `as np`.
- put every import at the **top** of the file, above all other code.
- importing runs the module once and caches it; repeat imports are free.

### `math`

- `math.sqrt(x)` — square root. Raises `ValueError: math domain error` on a negative, instead of quietly giving you a complex number the way `x ** 0.5` does.
- `math.pi` — 3.141592653589793. A value, not a function — no parentheses.
- `math.e` — 2.718281828459045.
- `math.floor(x)` — round **down** to a whole number. `floor(-2.7)` is `-3`.
- `math.ceil(x)` — round **up** to a whole number. `ceil(3.1)` is `4`.
- `math.log(x)` — natural log. `math.log(x, base)` for another base. `math.log10(x)` for base 10.
- `math.exp(x)` — e to the power of x.
- `math.factorial(n)` — n! for a whole number.
- `math.hypot(a, b)` — the hypotenuse, `sqrt(a**2 + b**2)`.
- `math.isclose(a, b)` — `True` when two floats are near-identical; the right way to compare floats.

### `random`

- `random.seed(n)` — pin the sequence so every run gives the same numbers. Use it whenever you need a reproducible result; skip it when you want genuine unpredictability.
- `random.randint(a, b)` — a whole number from `a` to `b`, **both included**.
- `random.choice(items)` — one item picked from a list.
- `random.shuffle(items)` — reorders the list **in place**; returns `None`, so never assign its result.
- `random.sample(items, k)` — a list of `k` different items, original untouched.
- `random.random()` — a float from 0.0 up to (not including) 1.0.
- `random.uniform(a, b)` — a float between `a` and `b`.

### `statistics`

- `statistics.mean(numbers)` — the average.
- `statistics.median(numbers)` — the middle value once sorted; ignores extreme outliers.
- `statistics.mode(numbers)` — the most common value.
- `statistics.stdev(numbers)` — the standard deviation.

### The two errors

- `ModuleNotFoundError: No module named 'mathh'` — the module doesn't exist. Check the spelling and the capitalization first. Standard-library modules never need installing.
- `NameError: name 'sqrt' is not defined` — the module loaded fine, but you used a bare name. You need `math.sqrt`, or a `from math import sqrt` line.

Most of it in one place:

```python
import math
import random
import statistics as stats

random.seed(1)
print(math.floor(3.9), math.ceil(3.1))   # 3 4
print(round(math.pi, 4))                  # 3.1416
print(random.randint(1, 100))             # 18
print(stats.mean([1, 2, 3, 4]))           # 2.5
print(stats.median([1, 2, 3, 4]))         # 2.5
```
