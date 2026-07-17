# Reading errors
unit: 1

## An error is a message, not a scolding

```python
basket = ["apple", "bread"]
print(basket[5])
# IndexError: list index out of range
```

Python just told you, in plain English, that you asked for item 5 of a list that doesn't have an item 5. That's not punishment. That's a helpful coworker tapping you on the shoulder and saying "hey, this one line here — I can't do that."

Every error message has the same shape: **what went wrong**, and **where**. Learn to read those two things and most of your stuck-time disappears.

> **Misconception: red text means you broke something and you should panic.** Red text means Python stopped instead of quietly doing the wrong thing. That is the best possible outcome. Errors are the cheap failures — they happen instantly and they tell you exactly what's wrong. The expensive failures are the ones with **no** error, where your code runs happily and hands you a wrong answer.

Here's the proof. This code has a real bug and produces **no error at all**:

```python
prices = [10.00, 20.00, 30.00]
average = sum(prices) / 2
print(average)
# 30.0
```

Three prices, and it divided by `2`. The answer `30.0` is flat wrong — the real average is `20.0` — and Python printed it without a whisper of complaint. Nobody tapped you on the shoulder. That bug ships.

Now compare it to the version that errors:

```python
prices = [10.00, 20.00, 30.00]
average = sum(prices) / len(prices)
print(average)
# 20.0
```

The error was never your enemy. Silence is.

## The last line is the what

Every error message ends with the important line. It always looks like this:

```
ErrorType: a plain-English description
```

Two parts, split at the colon:

- **before the colon** — the **kind** of error (`NameError`, `TypeError`, `IndexError`, ...). This tells you what **category** of mistake you made.
- **after the colon** — a specific description of **this** mistake, usually naming the exact thing that went wrong.

```python
receipt = {"apple": 1.20}
print(receipt["milk"])
# KeyError: 'milk'
```

Read it: the **kind** is `KeyError` (you asked a dictionary for a key), and the **specific** thing is `'milk'` (that key). It even quotes the exact key back to you. Nine times out of ten, the last line alone is enough to fix the bug.

## Read the traceback from the bottom up

When the error happens inside a function, Python prints a **traceback** — a stack of lines showing how it got there. Here is a real one:

```
Traceback (most recent call last):
  File "report.py", line 7, in <module>
    print(report([80, 90, 100]))
          ^^^^^^^^^^^^^^^^^^^^^
  File "report.py", line 5, in report
    return "Average: " + average(scores)
           ~~~~~~~~~~~~^~~~~~~~~~~~~~~~~
TypeError: can only concatenate str (not "float") to str
```

That looks like a lot. It isn't. **Read it bottom-up:**

1. **Last line** — the **what**: `TypeError: can only concatenate str (not "float") to str`. Someone tried to `+` a string and a float.
2. **The block just above it** — the **where**: `File "report.py", line 5, in report`, and it even reprints the offending line, `return "Average: " + average(scores)`. That's the culprit.
3. **Everything above that** — the **how you got here**. Line 7 called `report()`, which is what led to line 5. That's context, and you usually don't need it.

So: `average(scores)` returns a float, and `"Average: " + a float` is not allowed. Here's that exact program, runnable:

```python
def average(nums):
    return sum(nums) / len(nums)

def report(scores):
    return "Average: " + average(scores)

print(report([80, 90, 100]))
# TypeError: can only concatenate str (not "float") to str
```

And fixed — wrap the number in `str()`:

```python
def average(nums):
    return sum(nums) / len(nums)

def report(scores):
    return "Average: " + str(average(scores))

print(report([80, 90, 100]))
# Average: 90.0
```

> **Misconception: you should read a traceback top-down, like normal text.** The top is the **least** useful part. It's where your program **started**, not where it broke. Beginners read `Traceback (most recent call last):` and their eyes glaze over before they ever reach the one line that names the problem. "Most recent call last" is Python literally telling you the important stuff is at the **bottom**.

Proof — the traceback below is five levels deep, but only the bottom two lines matter:

```python
def step_four(n):
    return n + "!"

def step_three(n):
    return step_four(n)

def step_two(n):
    return step_three(n)

def step_one(n):
    return step_two(n)

print(step_one(5))
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

Four function calls, one bug. The last line names it: something did `int + str`. Only `step_four` does any `+`, so that's your line. You never needed to read the top of the stack at all.

## The traceback names the line, you check its neighbours

The `line N` in a traceback is where Python **got confused** — which isn't always where you type the fix.

```python
seat_counts = [
    12,
    8
    15,
]
print(seat_counts)
# SyntaxError: invalid syntax. Perhaps you forgot a comma?
```

Python names **line 3** and puts the caret under `8`. But look at line 3 on its own: `8`. There is nothing wrong with `8`. It's a perfectly good number. The mistake only exists in the **relationship** between line 3 and line 4 — a missing comma at the end of line 3, which you can only see by reading both lines together.

```python
seat_counts = [
    12,
    8,
    15,
]
print(seat_counts)
# [12, 8, 15]
```

> **Misconception: the mistake is exactly at the spot the caret points to.** The caret marks where Python's reading broke down. Something **missing** — a comma, a colon, a closing bracket — is invisible, so Python can only point at the first thing that stopped making sense because of it. **Always read the named line and the line above it as a pair.**

Unclosed brackets are the classic case. Watch which line gets named:

```python
cart_prices = [2.50, 1.25]
cart_total = sum(cart_prices
print("Total:", cart_total)
print("Done")
# SyntaxError: '(' was never closed
```

Your instinct says line 3 is broken — it's the `print` that never ran. Python names **line 2**, and it's right: `sum(` opened a parenthesis and nobody closed it. Modern Python is good at this. Trust the line number, but read **around** it.

```python
cart_prices = [2.50, 1.25]
cart_total = sum(cart_prices)
print("Total:", cart_total)
print("Done")
# Total: 3.75
# Done
```

> **Misconception: when something errors, start changing things until it works.** Adding random parentheses, swapping `=` for `==`, retyping the line — this is the single biggest time-waster in beginner programming. You have a message that says exactly what's wrong, and guessing throws it away. Worse, random edits create **new** bugs on top of the old one, and now you're debugging two things.

Proof. Here's a broken line and a "just try stuff" fix:

```python
guest_count = "12"
print(guest_count + 1)
# TypeError: can only concatenate str (not "int") to str
```

The panicked fix — "the `+ 1` looks weird, delete it":

```python
guest_count = "12"
print(guest_count)
# 12
```

No error! And it's useless — you needed 13, and now the code doesn't even try to add. The error is gone; the bug is worse, because it's silent now. Read the message instead: **"can only concatenate str to str"** — `guest_count` is a **str**, and you want to do math. Convert it:

```python
guest_count = "12"
print(int(guest_count) + 1)
# 13
```

The message named the type (`str`), named the operation (`concatenate`), and named the fix (make them match). Guessing found none of that.

## SyntaxError — Python can't read your code

A `SyntaxError` is special: **nothing runs at all**, not even the correct lines above it. Python reads your whole file before executing a single line, and if it can't understand the shape of the code, it refuses to start.

```python
print("this line is perfect")
badly formed !! line
# SyntaxError: invalid syntax
```

Notice `"this line is perfect"` never printed — even though it's on line 1 and it's flawless. That's your tell: **if none of your prints appear, it's a SyntaxError.**

### Missing colon

```python
exam_score = 90
if exam_score > 60
    print("pass")
# SyntaxError: expected ':'
```

`expected ':'` — Python is naming the exact character it wanted. Every `if`, `else`, `elif`, `def`, and `for` line ends with a colon.

```python
exam_score = 90
if exam_score > 60:
    print("pass")
# pass
```

Same message from a `def`:

```python
def add_up(a, b)
    return a + b
# SyntaxError: expected ':'
```

### Missing quote

```python
label = "Score:
print(label)
# SyntaxError: unterminated string literal (detected at line 1)
```

"Unterminated" means: you opened a quote and never closed it. Quotes come in pairs, always.

```python
label = "Score:"
print(label)
# Score:
```

This one catches everybody — an apostrophe inside single quotes:

```python
message = 'It's fine'
print(message)
# SyntaxError: unterminated string literal (detected at line 1)
```

Python sees `'It'` as a complete string, then trips over `s fine'`. Use double quotes on the outside:

```python
message = "It's fine"
print(message)
# It's fine
```

### Missing parenthesis

```python
print("hello"
print("world")
# SyntaxError: '(' was never closed
```

`'(' was never closed` is one of the friendliest messages Python has — it tells you the bracket type **and** points at the line where it opened. Count your brackets on that line.

```python
print("hello")
print("world")
# hello
# world
```

Square brackets and curly braces give you the same message with their own symbol:

```python
pens = ["blue", "black"
print(pens)
# SyntaxError: '[' was never closed
```

And an **extra** closing bracket gets its own message:

```python
chairs = ["A1", "A2"]
print(len(chairs)))
# SyntaxError: unmatched ')'
```

### Assignment instead of comparison

```python
dice_roll = 6
if dice_roll = 6:
    print("you win")
# SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
```

Read that message — Python guessed what you meant and told you. `=` puts a value in a box. `==` asks a question. An `if` needs a question.

```python
dice_roll = 6
if dice_roll == 6:
    print("you win")
# you win
```

## IndentationError — the shape is wrong

Indentation is Python's punctuation, so getting it wrong is a real error, not a style complaint.

```python
if 5 > 3:
print("yes")
# IndentationError: expected an indented block after 'if' statement on line 1
```

That message is almost a fix-it instruction: it wants an indented block, after the `if`, on line 1.

```python
if 5 > 3:
    print("yes")
# yes
```

The opposite — indenting something that shouldn't be:

```python
songs_played = 0
    songs_played = songs_played + 1
print(songs_played)
# IndentationError: unexpected indent
```

"Unexpected indent" means: this line is pushed to the right, but nothing above it opened a block. Nothing asked for indentation here.

```python
songs_played = 0
songs_played = songs_played + 1
print(songs_played)
# 1
```

## NameError — Python doesn't know that word

`NameError` means you used a name Python has never seen assigned. There are three flavours, and the message tells you which.

### A name that doesn't exist

```python
print(shipping_fee)
# NameError: name 'shipping_fee' is not defined
```

You never created it. Either assign it first, or you're using it before the line that defines it — order matters, Python reads top to bottom.

```python
shipping_fee = 4.99
print(shipping_fee)
# 4.99
```

### A typo in a name

```python
playlist_length = 12
print(playlist_lenght)
# NameError: name 'playlist_lenght' is not defined
```

The trick here: **Python quotes back the exact name it couldn't find.** Don't read it as a word — read it character by character against the name you meant. `playlist_lenght` vs `playlist_length`. The `h` and the `t` are swapped. Your eye will happily skate over that ten times in a row; the quoted name in the message won't.

```python
playlist_length = 12
print(playlist_length)
# 12
```

> **Watch out:** when you run a Python **file** from a terminal, Python often adds a suggestion — `Did you mean: 'playlist_length'?` — and it's usually right. You won't see that extra hint here in the app, which only shows the core message. The quoted name is the part you can always rely on.

### Forgetting the quotes around text

This one is sneaky, because the code **looks** fine:

```python
print(Hello)
# NameError: name 'Hello' is not defined
```

Without quotes, `Hello` isn't text — it's a **variable name**, and Python goes looking for a box called `Hello`. There isn't one. Quotes are what turn a word into a string.

```python
print("Hello")
# Hello
```

> **Watch out:** `NameError` on something you're **sure** you defined usually means one of three things — a typo (compare the quoted name letter by letter), wrong capitalization (`Score` and `score` are different boxes), or you defined it **below** the line that uses it.

## TypeError — right idea, wrong kind of thing

`TypeError` means the operation is fine but the ingredients aren't. It always names the types involved — read them.

### A string plus a number

```python
guest_age = 25
print("Age: " + guest_age)
# TypeError: can only concatenate str (not "int") to str
```

`+` glues two strings, or adds two numbers. It refuses to mix, because it can't tell which one you meant. The message names both types: it has a `str`, and you handed it an `int`. Convert:

```python
guest_age = 25
print("Age: " + str(guest_age))
# Age: 25
```

The mirror image — text where a number belongs:

```python
tickets = "3"
print(tickets * "2")
# TypeError: can't multiply sequence by non-int of type 'str'
```

```python
tickets = "3"
print(int(tickets) * 2)
# 6
```

### Wrong number of arguments

```python
def make_greeting(name, greeting):
    return greeting + ", " + name

print(make_greeting("Sam"))
# TypeError: make_greeting() missing 1 required positional argument: 'greeting'
```

Python names the function, counts what's missing, and **names the missing parameter**: `'greeting'`. There is no guesswork left.

```python
def make_greeting(name, greeting):
    return greeting + ", " + name

print(make_greeting("Sam", "Hello"))
# Hello, Sam
```

Too many is just as clear:

```python
def shout(word):
    return word.upper()

print(shout("hi", "there"))
# TypeError: shout() takes 1 positional argument but 2 were given
```

### NoneType — a function that forgot to return

This is the one that confuses beginners most, so read it slowly.

```python
def double_it(n):
    result = n * 2

print(double_it(5) + 1)
# TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
```

`NoneType`?! You never wrote `None` anywhere. Here's what happened: `double_it` **calculates** `result` and then just... ends. It never `return`s it. A function that doesn't return anything gives back `None`. So `double_it(5)` is `None`, and `None + 1` is a `TypeError`.

**`NoneType` in an error message is almost always a missing `return`.** Add it:

```python
def double_it(n):
    result = n * 2
    return result

print(double_it(5) + 1)
# 11
```

You can see the `None` for yourself — printing it directly doesn't error, which is exactly why this bug hides:

```python
def no_return(n):
    answer = n * 2

print(no_return(5))
# None
```

## ValueError — right type, impossible value

`TypeError` is "wrong **kind** of thing." `ValueError` is "right kind of thing, but that particular value can't work."

```python
age_typed_in = "hello"
print(int(age_typed_in))
# ValueError: invalid literal for int() with base 10: 'hello'
```

`int()` is perfectly happy to take a string — `int("42")` works fine. That's why this isn't a `TypeError`. The problem is **this** string: `'hello'` isn't a number. Python even quotes the exact offending value back at you.

```python
age_typed_in = "42"
print(int(age_typed_in))
# 42
```

Predict this one before you read on — does `int("3.5")` work?

```python
print(int("3.5"))
# ValueError: invalid literal for int() with base 10: '3.5'
```

It doesn't. `int()` parses **whole numbers** from text, and `"3.5"` has a decimal point in it. Go via `float()`:

```python
print(int(float("3.5")))
# 3
```

`float()` has its own version of the message:

```python
print(float("12.5.6"))
# ValueError: could not convert string to float: '12.5.6'
```

## IndexError — that position doesn't exist

```python
top_scores = [90, 85, 77]
print(top_scores[3])
# IndexError: list index out of range
```

Three items, so the valid positions are `0`, `1`, `2`. There is no `3`. Counting from zero means **the last position is always `len(thing) - 1`**.

```python
top_scores = [90, 85, 77]
print(len(top_scores))
print(top_scores[2])
print(top_scores[-1])
# 3
# 77
# 77
```

`[-1]` is the safe way to say "the last one" — it works no matter how long the list is.

Strings get their own wording, which is a nice hint about what you indexed:

```python
pet = "cat"
print(pet[5])
# IndexError: string index out of range
```

And an empty list has **no** valid positions at all:

```python
waiting_list = []
print(waiting_list.pop())
# IndexError: pop from empty list
```

> **Watch out:** `IndexError: list index out of range` in a loop almost always means you counted one too far. If a list has 3 items, position `3` is already past the end.

## KeyError — that key isn't in the dictionary

```python
menu = {"coffee": 3.50, "tea": 2.75}
print(menu["cocoa"])
# KeyError: 'cocoa'
```

The whole message is the key you asked for. Nothing else needs saying: there is no `'cocoa'` in that dictionary. Usually it's a typo, a capitalization mismatch, or a key you assumed was there.

Check before you ask, with `in`:

```python
menu = {"coffee": 3.50, "tea": 2.75}
print("cocoa" in menu)
print("coffee" in menu)
# False
# True
```

Or use `.get()`, which returns `None` instead of exploding — and lets you supply a fallback:

```python
menu = {"coffee": 3.50, "tea": 2.75}
print(menu.get("cocoa"))
print(menu.get("cocoa", 0.00))
print(menu.get("coffee", 0.00))
# None
# 0.0
# 3.5
```

> **Watch out:** `KeyError` is about **keys**, `IndexError` is about **positions**. Which one you get tells you what kind of thing you were actually holding — useful when you thought you had a list and you really had a dictionary.

## ZeroDivisionError — the one with no clever fix

```python
pizza_slices = 12
people = 0
print(pizza_slices / people)
# ZeroDivisionError: division by zero
```

Nothing is wrong with your syntax or your types. Dividing by zero simply has no answer, so Python stops. This one is nearly always a **data** problem: some list was empty, or a counter never got incremented.

The fix is to check first:

```python
pizza_slices = 12
people = 0

if people == 0:
    print("nobody's here")
else:
    print(pizza_slices / people)
# nobody's here
```

`%` and `//` have the same limit, with slightly different wording:

```python
print(10 % 0)
# ZeroDivisionError: integer modulo by zero
```

The classic real-world version — averaging an empty list:

```python
def safe_average(nums):
    if len(nums) == 0:
        return 0
    return sum(nums) / len(nums)

print(safe_average([80, 90]))
print(safe_average([]))
# 85.0
# 0
```

## AttributeError — that thing can't do that

A `.something()` after a value is a **method** — an action that kind of value knows how to do. `AttributeError` means this kind of value doesn't know that action.

```python
room_number = 42
print(room_number.upper())
# AttributeError: 'int' object has no attribute 'upper'
```

`.upper()` is a **string** action. `42` is an `int`, and numbers have no uppercase. The message names the type (`'int'`) and the action (`'upper'`) — put those two words together and the sentence explains itself.

```python
room_number = 42
print(str(room_number).upper())
# 42
```

Typo a method name and you get the same shape of message — the type, then the exact method name it couldn't find:

```python
first_name = "sam"
print(first_name.uper())
# AttributeError: 'str' object has no attribute 'uper'
```

`'str'` is right, so `first_name` is fine — it's the **method** that's misspelled. `uper` is missing a `p`.

```python
first_name = "sam"
print(first_name.upper())
# SAM
```

A list is not a string, so string methods don't work on it:

```python
words = ["pen", "cup"]
print(words.upper())
# AttributeError: 'list' object has no attribute 'upper'
```

And the `NoneType` version, which — like the `TypeError` one — means a missing `return`:

```python
def build_name():
    text = "sam"

result = build_name()
print(result.upper())
# AttributeError: 'NoneType' object has no attribute 'upper'
```

> **Watch out:** `'NoneType' object has no attribute ...` and `unsupported operand type(s) for +: 'NoneType' and ...` are the same bug wearing two hats: **a function that's missing its `return`.** When you see `NoneType`, go look at the function you just called.

## When you're not sure, print it

Most debugging is one question: **what is actually in this variable?** Stop guessing and print it.

```python
mystery = "5"
print(mystery)
print(type(mystery))
# 5
# <class 'str'>
```

`print(mystery)` shows `5`, which looks exactly like a number and tells you nothing. `type()` gives it away: `<class 'str'>`. That's why `mystery + 1` would fail.

`repr()` is even better for this — it shows the value the way you'd **type** it, quotes and all:

```python
looks_like_a_number = "5"
really_a_number = 5
print(repr(looks_like_a_number))
print(repr(really_a_number))
# '5'
# 5
```

Quotes mean string. No quotes mean number. Now you can see the difference at a glance.

Print the length and the thing when you get an `IndexError`:

```python
queue = ["Ana", "Ben"]
print(queue)
print(len(queue))
# ['Ana', 'Ben']
# 2
```

Two items, so the only valid positions are `0` and `1`. Mystery solved before you even run the broken line.

## Catching an error on purpose

Sometimes you **expect** an error and want to handle it rather than crash. That's `try` / `except`:

```python
user_typed = "hello"

try:
    age = int(user_typed)
    print("You are", age)
except ValueError:
    print("That's not a number")
# That's not a number
```

Python runs the `try` block. If the named error happens, it jumps to `except` instead of stopping the program. If no error happens, `except` is skipped entirely:

```python
user_typed = "30"

try:
    age = int(user_typed)
    print("You are", age)
except ValueError:
    print("That's not a number")
# You are 30
```

You can read the message Python would have printed, using `as`:

```python
try:
    print(10 / 0)
except ZeroDivisionError as e:
    print("caught:", e)
# caught: division by zero
```

> **Watch out:** don't reach for `try`/`except` to silence an error you haven't read yet. That's the "change things randomly" mistake with extra steps — the bug is still there, just quieter. Use it only when the error is a **normal, expected** situation (a person typed nonsense, a file isn't there), not to paper over a mistake in your own code.

## The method: four steps, every time

When red text appears, do this — in this order — instead of anything else:

1. **Read the last line.** Kind of error, then the description. That alone usually names the fix.
2. **Find the line number.** In a traceback, it's the `File "...", line N` block **just above** the last line. Ignore the rest.
3. **Read that line and the one above it.** Something missing (a comma, a colon, a bracket) shows up as a complaint on the **next** thing Python read.
4. **Print the thing you're unsure about.** `print(x)` and `print(type(x))`. Nearly every `TypeError`, `AttributeError`, and `NoneType` mystery dies right here.

Only after those four do you change any code.

## Worked example: a receipt with two bugs

Here's a program with a real bug. Read the error before you read the explanation.

```python
cart = [("pen", "2.50"), ("cup", "8.00")]

def cart_total(items):
    total = 0
    for name, price in items:
        total = total + price
    return total

print(cart_total(cart))
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

Step 1, last line: `unsupported operand type(s) for +: 'int' and 'str'`. Something did `int + str`. Step 2, the line: it's the `total = total + price` line. Step 3: `total` starts at `0` (an `int`), so `price` must be the `str`. Step 4, print it to be sure:

```python
for name, price in cart:
    print(repr(price))
# '2.50'
# '8.00'
```

Quotes — they're strings. The prices were typed with quotes around them. Convert with `float()`:

```python
def cart_total(items):
    total = 0
    for name, price in items:
        total = total + float(price)
    return total

print(cart_total(cart))
# 10.5
```

Now a second bug appears in the same program:

```python
def receipt_line(items, position):
    name, price = items[position]
    return name + ": $" + price

print(receipt_line(cart, 2))
# IndexError: list index out of range
```

Last line: `IndexError: list index out of range`. `cart` has 2 items, so positions are `0` and `1`. Asking for `2` walks off the end:

```python
print(len(cart))
print(receipt_line(cart, 1))
# 2
# cup: $8.00
```

## Worked example: reading three errors in a row

Fixing one error often reveals the next. That's normal — it means you're making progress. Watch the whole chain.

Bug 1 — Python won't even start:

```python
def score_report(name, points)
    return name + " scored " + points
# SyntaxError: expected ':'
```

`expected ':'`. Add it:

```python
def score_report(name, points):
    return name + " scored " + points

print(score_report("Ana", 95))
# TypeError: can only concatenate str (not "int") to str
```

Bug 2 — a new error, which is **good news**: the syntax is fixed and the code actually ran. `can only concatenate str (not "int") to str` — `points` is `95`, an `int`. Wrap it:

```python
def score_report(name, points):
    return name + " scored " + str(points)

print(score_report("Ana", 95))
# Ana scored 95
```

Bug 3 — now call it the way a typo-ing human would:

```python
print(score_report("Ana"))
# TypeError: score_report() missing 1 required positional argument: 'points'
```

The message names the function **and** the missing parameter, `'points'`. Three errors, three messages, three fixes — and every single fix was written in the message. That's the whole skill.

```python
print(score_report("Ana", 88))
print(score_report("Ben", 74))
# Ana scored 88
# Ben scored 74
```

## Quick reference — what's available

### The errors you'll actually meet

- `SyntaxError` — Python can't read the code; **nothing runs at all**
- `IndentationError` — a line is indented wrong (a kind of `SyntaxError`)
- `NameError` — you used a name that was never assigned (typo, or not defined yet)
- `TypeError` — right operation, wrong kind of value (`str` + `int`, wrong arg count, `NoneType`)
- `ValueError` — right kind of value, impossible content (`int("hello")`)
- `IndexError` — that position doesn't exist in a list or string
- `KeyError` — that key isn't in the dictionary
- `ZeroDivisionError` — you divided by zero
- `AttributeError` — that type has no such method (`.upper()` on a number)
- `ModuleNotFoundError` — `import` couldn't find that module (check the spelling)

### Real messages, decoded

- `expected ':'` — add a colon at the end of the `if`/`def`/`for` line
- `'(' was never closed` — count brackets on the line it names
- `unmatched ')'` — you have one closing bracket too many
- `unterminated string literal` — a quote was opened and never closed
- `invalid syntax. Maybe you meant '==' or ':=' instead of '='?` — use `==` to compare
- `Perhaps you forgot a comma?` — read the named line **and** the one after it
- `expected an indented block after 'if' statement on line N` — indent the body
- `unexpected indent` — remove the indentation; nothing opened a block
- `name 'x' is not defined` — compare the quoted name to yours, character by character
- `'str' object has no attribute 'x'` — the type is fine; the method name is misspelled
- `Did you mean: 'x'?` — a bonus hint Python adds when you run a script file; usually right
- `can only concatenate str (not "int") to str` — wrap the number in `str()`
- `unsupported operand type(s) for +: 'NoneType' and 'int'` — a function is missing its `return`
- `'NoneType' object has no attribute ...` — same thing: a missing `return`
- `missing 1 required positional argument: 'x'` — you left out argument `x`
- `takes 1 positional argument but 2 were given` — you passed one too many
- `invalid literal for int() with base 10: 'x'` — that text isn't a whole number
- `list index out of range` — valid positions stop at `len(thing) - 1`

### Tools for figuring out what you've got

- `print(x)` — see the value
- `print(type(x))` — see what kind of thing it is, e.g. `<class 'str'>`
- `print(repr(x))` — see it as you'd type it; quotes mean it's a string
- `print(len(x))` — how many items/characters; the last position is `len(x) - 1`
- `isinstance(x, int)` — `True`/`False`, is it that type?
- `key in some_dict` — `True`/`False`, checked **before** you index and get a `KeyError`
- `some_dict.get(key)` — the value, or `None` instead of a `KeyError`
- `some_dict.get(key, fallback)` — the value, or your fallback

### Handling an error instead of crashing

- `try:` / `except SomeError:` — run the block; on that error, run the `except` instead
- `except SomeError as e:` — `e` holds the message Python would have printed
- Use it for **expected** situations (bad input), never to hide your own bug

Everything above, working together — a function that guards against every error this
page showed you:

```python
stock = {"pen": 4, "cup": 0}

def report(item, order_size):
    if item not in stock:
        return item + ": not stocked"
    on_hand = stock[item]
    if on_hand == 0:
        return item + ": out of stock"
    try:
        size = int(order_size)
    except ValueError:
        return item + ": " + repr(order_size) + " is not a number"
    if size == 0:
        return item + ": order size can't be zero"
    return item + ": " + str(on_hand // size) + " orders available"

print(report("pen", "2"))
print(report("cup", "2"))
print(report("hat", "2"))
print(report("pen", "lots"))
print(report("pen", "0"))
# pen: 2 orders available
# cup: out of stock
# hat: not stocked
# pen: 'lots' is not a number
# pen: order size can't be zero
```

Five different disasters — a missing key, an empty shelf, a bad conversion, a divide
by zero — and not one traceback. Every guard came straight from an error message this
page showed you.

And here is the honest part. The first draft of this example was missing the
`if size == 0` guard, and the text under it still bragged that the function "survives
whatever you throw at it". It didn't: `report("pen", "0")` crashed with
`ZeroDivisionError`. Nobody noticed, because the four examples printed underneath all
worked — the one input that broke it was the one nobody thought to try.

That is the real lesson of this page. Code that works on the inputs you happened to try
is not code that works. When you write a guard, ask what input would get past it.
