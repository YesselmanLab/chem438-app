# Functions
unit: 3

## Why bother with functions?

Look at this. Three receipts, same math, typed three times.

```python
bill1 = 42
print(bill1 + 2)     # 44

bill2 = 18
print(bill2 + 2)     # 20

bill3 = 100
print(bill3 + 2)     # 102
```

Every line repeats the same idea: take a bill, add a flat $2 service fee. If the fee ever
changes to $3, you have to find and fix every copy. Miss one and your program is quietly wrong.

A function lets you write that idea once, give it a name, and reuse it as many times as you
want.

```python
def total_with_fee(bill):
    return bill + 2

print(total_with_fee(42))    # 44
print(total_with_fee(18))    # 20
print(total_with_fee(100))   # 102
```

Same answers, one place to fix things. That is the whole point of a function: name a chunk of
work so you can reuse it instead of retyping it.

## Anatomy of a function

Here is the function from above, labeled piece by piece.

```python
def greet(name):
    return "Hello, " + name + "!"
```

- `def` — the keyword that starts every function definition. Nothing fancy, it just means
  "I'm about to define a function."
- `greet` — the name you are giving this function. You call it later by this name.
- `(name)` — the parentheses hold the **parameters**, the placeholders this function needs to
  do its job. This one needs a single value, which it will call `name` inside the function.
- `:` — the colon ends the header line. Python expects an indented block next.
- the indented lines below — the **body**. Everything indented the same amount belongs to this
  function. As soon as a line goes back to the left margin, it is no longer part of `greet`.

Indentation is not decoration in Python — it is how Python knows where the function starts and
stops. Four spaces is the standard amount, and every line in the body must line up.

> **Common mistake:** mismatched indentation. If one line in the body is indented differently
> from the others, Python raises `IndentationError: unexpected indent` or
> `IndentationError: unindent does not match any outer indentation level`. Keep every line in a
> block indented by the exact same amount.

## Calling a function

Defining a function does not run it. Nothing happens until you **call** it — write its name
followed by parentheses, with the values it needs inside.

```python
def shout():
    print("I only run when called")

print("before the call")
shout()
print("after the call")
```

```
before the call
I only run when called
after the call
```

Read that trace carefully. Python runs `print("before the call")` first. Then it hits
`shout()` and jumps into the function body, which prints its line. Then it comes back out and
runs `print("after the call")`. The function's code did not run when Python read the `def`
line — only when `shout()` was actually called.

> **Common mistake:** thinking a function runs the moment you define it. It does not — Python
> just reads the definition and remembers it. Watch:
>
> ```python
> def boom():
>     print(1 / 0)
>
> print("no error yet")
> ```
>
> ```
> no error yet
> ```
>
> `1 / 0` would crash the program — but only if `boom()` is actually called. It never is here,
> so the body never runs, and there is no error. Defining a function is like writing a recipe
> card. Writing the card doesn't cook anything.

## return vs. print — the most important distinction in this course

This is where almost every beginner gets stuck. Get comfortable with it now and everything
later goes smoother.

`print` shows something on the screen. `return` hands a value back to whoever called the
function, so it can be stored, compared, or used in more math. They are not the same thing,
and mixing them up is the single most common bug in beginner code.

Look at two functions that seem to do the same thing:

```python
def show_double(x):
    print(x * 2)      # displays the value — nothing goes back to the caller

def double(x):
    return x * 2      # hands the value back to the caller

show_double(5)         # 10           <- printed by the function itself, while it runs
answer = double(5)
print(answer)           # 10           <- printed by us, using the value double() gave back
```

Both put `10` on your screen. But only `double` gave you something you can use. Watch what
happens when you try to grab the result of `show_double`:

```python
def show_double(x):
    print(x * 2)

result = show_double(5)   # this line prints 10, while it runs
print(result)              # None
```

Before you run this in your head — what do you think `print(result)` shows? It is **not**
`10`. `show_double` never has a `return` statement, so it hands back nothing at all. In
Python, a function with no `return` hands back a special value called `None`. `result` holds
`None`, not `10`. The `10` you saw was only ever drawn on the screen; it was never delivered
to the caller.

> **Common mistake:** believing `print` and `return` are interchangeable. They are not.
> `print` is for humans looking at the screen. `return` is for the program itself — it is how
> one part of your code hands a value to another part. A function that only prints has, as far
> as the rest of your program is concerned, produced nothing.

Now watch what happens when you try to do math with a function that only prints:

```python
def bad_double(x):
    print(x * 2)     # shows it, but hands nothing back

print(bad_double(5) + 1)
```

Before you look — what happens? Trace it in order. Python first has to evaluate
`bad_double(5)` to know what to add `1` to. Calling `bad_double(5)` runs its body, which
prints `10` to the screen as a side effect. Then the call finishes and hands back its return
value — which is `None`, because there is no `return` statement. So Python is now trying to
compute `None + 1`, and that fails:

```
10
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
```

Notice the `10` still appears — the `print` inside `bad_double` already ran before the crash.
Then Python hits the addition, discovers it cannot add `None` and `1`, and stops the program
with a `TypeError`. Read that error type by type: `NoneType` is the type of `None`, `int` is
the type of `1`, and `+` does not know how to combine them. Whenever you see
`unsupported operand type(s) for +: 'NoneType' and ...`, the fix is almost always the same:
some function you called forgot to `return` a value.

> **Common mistake:** thinking that whatever a function prints is automatically available to
> use afterward. It is not. If you need to use a value later, the function must `return` it,
> and you must catch it in a variable or use it directly, like `total = double(5)`.

Here is the rule of thumb for the rest of this course: if you need the function's answer for
anything besides looking at it right now, use `return`. Save `print` for the very last step —
showing a final result to a human — or for debugging while you build something.

One more misconception, about code placed after `return`:

```python
def status(score):
    if score >= 60:
        return "pass"
        print("checking...")   # never runs

    return "fail"

print(status(75))   # pass
print(status(40))   # fail
```

Predict `status(75)` before reading on. It is `"pass"`, not `"pass"` followed by
`"checking..."`. The moment Python executes a `return` statement, the function ends
immediately — right there, mid-body. Any code written after it, even on the very next line,
never runs. It is not a mistake in this example (the line is dead on purpose, to make the
point), but writing unreachable code by accident is a real bug worth knowing to look for.

> **Common mistake:** assuming a function keeps running until it reaches the last line.
> `return` exits **immediately**, wherever it appears — even the first line of the body, even
> inside a loop, even inside an `if`.

## Tracing a call step by step

Let's slow one call all the way down.

```python
def total_with_fee(bill):
    return bill + 2

result = total_with_fee(42)
print(result)   # 44
```

1. Python reaches `total_with_fee(42)` and jumps into the function.
2. The parameter `bill` is created fresh, right now, and set to `42` — the argument you passed.
3. Python runs the body: it computes `bill + 2`, which is `44`.
4. `return` sends `44` back out, exactly to the spot the function was called from.
5. That spot is `result = total_with_fee(42)`, so `result` now holds `44`. The function call
   itself has been **replaced** by its return value, as if you had typed `result = 44`.
6. `print(result)` shows `44`.

That is the whole mechanism. A function call is not magic — it is a detour. Python leaves the
main flow of your program, runs the function's body somewhere else, and comes back with
whatever `return` handed it, dropping that value exactly where the call was written.

## Parameters vs. arguments

These two words get used loosely, but they mean different things, and it helps to keep them
straight.

```python
def greet(name):        # name is a PARAMETER — a placeholder in the definition
    return "Hi, " + name + "!"

print(greet("Sam"))      # "Sam" is an ARGUMENT — the actual value you supply
```

A **parameter** is the name written in the function's own parentheses, in the `def` line — it
exists only to describe what the function expects. An **argument** is the real value you hand
over when you call the function. `name` is a parameter. `"Sam"` is an argument.

> **Common mistake:** thinking you need to create a variable with the same name as a parameter
> before you can call the function. You do not — the parameter is created automatically, right
> when the function is called, from whatever argument you pass.
>
> ```python
> def greet(name):
>     return "Hi, " + name + "!"
>
> print(greet(name))
> ```
>
> ```
> Traceback (most recent call last):
>   File "<stdin>", line 1, in <module>
> NameError: name 'name' is not defined
> ```
>
> This fails because `name` was typed as if it were an already-existing variable in the
> calling code. It isn't — `name` only exists *inside* `greet`, once the function is running.
> Pass an actual value instead: `greet("Sam")`.

## Multiple parameters and argument order

A function can take as many parameters as it needs, separated by commas. By default, Python
matches arguments to parameters **by position** — first argument to first parameter, second to
second, and so on.

```python
def full_name(first, last):
    return first + " " + last

print(full_name("Ada", "Lovelace"))     # Ada Lovelace
print(full_name("Lovelace", "Ada"))     # Lovelace Ada   <- order matters!
```

Same two strings, same function, different order, different answer. Position is not a
formality — it is how Python decides which value means what.

You can override that by naming the parameter you're supplying, called a **keyword argument**.
Order stops mattering once you do this:

```python
def full_name(first, last):
    return first + " " + last

print(full_name(last="Lovelace", first="Ada"))   # Ada Lovelace
```

If you don't supply enough arguments, Python tells you exactly what is missing:

```python
def full_name(first, last):
    return first + " " + last

print(full_name("Ada"))
```

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: full_name() missing 1 required positional argument: 'last'
```

Read errors like this left to right: which function, how many arguments it's missing, and
which parameter's name it needed. This one is telling you plainly — `full_name` needed a
second value called `last`, and you never gave it one.

## A function that returns nothing gives you None

You already saw this above with `show_double`, but it is worth pinning down as its own rule,
because it applies to *every* function with no `return` statement — not just the ones written
to be confusing.

```python
def log_event(message):
    print("LOG:", message)

result = log_event("server started")   # LOG: server started
print(result)                           # None
```

`log_event` is a perfectly reasonable function — its whole job is to display something. But
because it never runs `return`, calling it always gives you `None` back, no matter what you
pass in. That is fine, as long as you never expect `result` to hold anything useful. The bug
only shows up when you *do* expect that — when you write `result + 1` or `result.upper()` and
Python tells you `None` cannot do that.

> **Watch out:** an easy way to check whether you meant to `return` something is to ask "will
> anyone need this function's answer later?" If yes, it must `return` it. If the function's
> entire job is to display a message and nothing more, printing with no `return` is correct.

## Multiple returns and early return

A function is not limited to one `return` statement. It can have several, and the first one
that actually runs ends the function right there.

```python
def grade(score):
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    return "F"

print(grade(95))   # A
print(grade(82))   # B
print(grade(71))   # C
print(grade(50))   # F
```

Trace `grade(82)`: the first check, `score >= 90`, is `False`, so that `return` is skipped
entirely — never runs. The second check, `score >= 80`, is `True`, so `return "B"` fires, and
the function ends immediately. It never even looks at the third check or the final line. Only
one `return` ever executes per call; the rest are just never reached.

This pattern — checking a special case first and returning immediately — is called an **early
return**, and it is one of the most useful tools you have for keeping functions readable.

```python
def safe_divide(a, b):
    if b == 0:
        return "cannot divide by zero"
    return a / b

print(safe_divide(10, 2))   # 5.0
print(safe_divide(10, 0))   # cannot divide by zero
```

Handle the special, dangerous case first and get out. Everything below the early return can
then assume the dangerous case is already ruled out — `b` is guaranteed not to be `0` by the
time Python reaches `a / b`.

## Default arguments

You can give a parameter a fallback value in the `def` line. If the caller doesn't supply that
argument, Python uses the default instead.

```python
def greet(name, greeting="Hello"):
    return greeting + ", " + name + "!"

print(greet("Sam"))                 # Hello, Sam!
print(greet("Sam", "Hey"))          # Hey, Sam!
print(greet("Sam", greeting="Yo"))  # Yo, Sam!
```

`greeting="Hello"` in the header means "if nobody says otherwise, use `Hello`." Leave it out
and you get the default. Supply it, positionally or by keyword, and you override it.

Default parameters must come **after** required ones. Python enforces this at the moment it
reads your code, before anything even runs:

```python
def greet(greeting="Hello", name):
    return greeting + ", " + name + "!"
```

```
SyntaxError: non-default argument follows default argument
```

The reasoning: if `greeting` could be skipped but `name` couldn't, Python would have no way to
tell, from a call like `greet("Sam")`, whether `"Sam"` was meant to fill `greeting` or `name`.
Required parameters first, defaults last — no exceptions.

## Calling one function from another

Functions can call other functions. This is how you build something complicated out of small,
already-tested pieces instead of writing one giant block of code.

```python
def square(x):
    return x * x

def sum_of_squares(a, b):
    return square(a) + square(b)

print(sum_of_squares(3, 4))   # 25
```

`sum_of_squares` doesn't know or care how `square` computes its answer — it just trusts that
calling `square(a)` gives back the right number, and uses that value like any other. This is
one of the biggest payoffs of writing functions in the first place: once `square` is written
and works, you never have to think about *how* it works again. You just use it.

## Local variables: why names don't leak out

A variable created inside a function only exists inside that function. It is called a **local
variable**, and it disappears the moment the function finishes.

```python
def compute_total(price, quantity):
    total = price * quantity
    return total

print(compute_total(4, 3))   # 12
print(total)
```

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'total' is not defined
```

`compute_total(4, 3)` works fine and prints `12` — `total` exists happily while the function is
running. But the moment the function returns, `total` is gone. Trying to use it outside the
function is exactly like using a variable you never created.

This is a feature, not a limitation. It means you can reuse the same variable name in
completely different functions without them interfering with each other at all:

```python
def area_of_square(side):
    total = side * side
    return total

def area_of_triangle(base, height):
    total = base * height / 2
    return total

print(area_of_square(4))         # 16
print(area_of_triangle(6, 4))    # 12.0
```

Both functions use a local variable called `total`, and they never collide — each `total`
lives only inside its own function call and vanishes afterward. If local variables leaked out
into the rest of your program, you'd have to invent a unique name for every temporary value in
every function you ever write. Because they don't, you're free to pick whatever local name
makes a function easy to read.

## Docstrings and good names

A **docstring** is a short description of what a function does, written as a string right at
the top of its body, before any code. Python stores it and you (or anyone using your function)
can read it back later.

```python
def total_with_fee(bill):
    """Return the bill plus a flat $2 service fee."""
    return bill + 2

print(total_with_fee.__doc__)
# Return the bill plus a flat $2 service fee.
```

A good docstring says what the function returns, in plain language, without restating the code.
Not every function you write in this course needs one, but any function whose purpose isn't
obvious from its name benefits from a one-line docstring.

Naming matters just as much as the docstring. Compare these two functions — they compute the
exact same thing:

```python
def f(x, y):
    return x * y + y

def order_total(price, quantity):
    return price * quantity + quantity

print(f(3, 4))               # 16
print(order_total(3, 4))     # 16
```

Both return `16`. But six months from now — or even six minutes from now, reading someone
else's code — `order_total(price, quantity)` tells you what it's for without opening the
function at all. `f(x, y)` tells you nothing. Prefer names that are verbs or verb phrases
describing what the function does (`compute_total`, `is_valid`, `find_max`), and parameter
names that describe what the value *is*, not just its type.

## Putting it together

Two worked examples that combine everything above: helper functions calling each other,
defaults, a running total, and an early return.

A shopping cart, priced item by item, with an optional discount:

```python
def line_total(price, qty):
    return price * qty

def apply_discount(total, discount=0.0):
    return total * (1 - discount)

def print_receipt(items, discount=0.0):
    subtotal = 0
    for price, qty in items:
        subtotal += line_total(price, qty)
    return apply_discount(subtotal, discount)

cart = [(4, 2), (12, 1), (3, 4)]
print(print_receipt(cart))          # 32.0
print(print_receipt(cart, 0.25))    # 24.0
```

`print_receipt` doesn't compute any prices itself — it calls `line_total` for each item and
`apply_discount` once at the end, and just adds things up in between. `discount` has a default
of `0.0`, so calling `print_receipt(cart)` with no discount at all still works.

A grade reporter that uses an early return to hide failing grades on request:

```python
def letter_for(score):
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    return "F"

def report(name, score, passing_only=False):
    letter = letter_for(score)
    if passing_only and letter == "F":
        return None
    return name + ": " + letter

print(report("Mia", 92))                     # Mia: A
print(report("Sam", 55))                     # Sam: F
print(report("Sam", 55, passing_only=True))  # None
```

`report` calls `letter_for` to do the grading, then makes its own decision on top of that
answer. When `passing_only` is `True` and the grade is an `F`, it returns `None` early — on
purpose, to signal "nothing to report" — rather than building a string. Every idea from this
page shows up here: parameters, a default argument, calling one function from another, an
early return, and a plain `return` handing the final answer back to whoever called `report`.
