# Strings
unit: 2

## What Is a String?

A string is just text, wrapped in quotes so Python knows it's text and not code.

```python
greeting = "hello"
print(greeting)          # hello
print(type(greeting))    # <class 'str'>
```

`type()` tells you what kind of thing a variable holds. `str` is short for "string."

Anything inside quotes is a string, even if it's just numbers or symbols.

```python
zip_code = "12345"
print(type(zip_code))    # <class 'str'>
```

`zip_code` looks like a number, but the quotes make it text. We'll come back to why that matters.

## Quotes: Single or Double?

Python is happy with either single quotes or double quotes. Pick one and be consistent.

```python
a = 'hello'
b = "hello"
print(a == b)    # True
```

The quote type matters when your text contains a quote character. If your text has an apostrophe, wrap it in double quotes:

```python
message = "Alice's coffee is ready"
print(message)    # Alice's coffee is ready
```

If your text has double quotes inside it, wrap it in single quotes:

```python
message = 'She said "stop"'
print(message)    # She said "stop"
```

If you need both kinds of quotes inside the same string, put a backslash before the one that matches your outer quotes. The backslash tells Python "this quote is part of the text, not the end of the string."

```python
message = "She said \"stop\""
print(message)    # She said "stop"
```

> **Watch out:** if your outer quotes match a quote *inside* the text, and you don't escape it, Python thinks the string ends early and the rest of the line turns into broken code. If you ever see a wall of red text after typing a sentence with an apostrophe, check your quotes first.

## Strings Are Not Numbers

`"5"` and `5` look similar but they are completely different things to Python.

```python
print("5" == 5)    # False
```

They're never equal, even though a human reads them the same way. One is text, one is a number.

> **Common mistake:** beginners assume `"5" + 5` will give `6`. It does not. Adding a string and a number is not allowed, because Python doesn't know if you mean "put these two things next to each other" or "do math."

```python
print("5" + 5)
# TypeError: can only concatenate str (not "int") to str
```

Read that error slowly: it's telling you it tried to *concatenate* (join) a string with something that isn't a string, and it refused.

To combine a string and a number, you have to convert one of them first — the "Converting Between Strings and Numbers" section below covers exactly how. For now, just remember: **quotes mean text, no quotes means number.**

## Joining Strings with +

`+` glues strings together. This is called concatenation.

```python
first = "Jane"
last = "Doe"
full = first + last
print(full)    # JaneDoe
```

Notice there's no space between "Jane" and "Doe." `+` does exactly what you tell it and nothing more — it doesn't guess that you wanted a space.

```python
full = first + " " + last
print(full)    # Jane Doe
```

> **Watch out:** the missing-space trap catches everyone at least once. If your output looks like `JaneDoe` instead of `Jane Doe`, you forgot to add `" "` between the pieces.

## Repeating Strings with *

`*` repeats a string a given number of times.

```python
laugh = "ha" * 3
print(laugh)    # hahaha
```

```python
divider = "=" * 10
print(divider)    # ==========
```

This is handy for building separators or simple visual output without typing the same character over and over.

**Predict the output before you run this:**

```python
border = "-*" * 4
print(border)
```

It prints `-*-*-*-*` — the whole two-character chunk `"-*"` repeats four times, not just the dash.

## Length: len()

`len()` tells you how many characters are in a string.

```python
word = "python"
print(len(word))    # 6
```

Spaces count as characters too.

```python
sentence = "I love pizza"
print(len(sentence))    # 12
```

## Counting From Zero

This is the single biggest thing to get right about strings: Python counts positions starting at **0**, not 1. The first character is at position 0, the second is at position 1, and so on.

Here's `"python"` laid out with its positions marked, counting from the front and from the back:

```python
word = "python"
# chr: p   y   t   h   o   n
# pos: 0   1   2   3   4   5
# neg: -6  -5  -4  -3  -2  -1
```

Negative positions count backward from the end. `-1` is always the last character, no matter how long the string is.

> **Common mistake:** thinking the first letter is at position 1. It's not. Position 1 is the *second* letter. `word[0]` is `"p"`, not `word[1]`.

## Indexing: Grabbing One Character

Use square brackets and a position number to pull out a single character. This is called indexing.

```python
word = "python"
print(word[0])     # p    <- the first character
print(word[2])     # t    <- the third character
print(word[-1])    # n    <- the last character
print(word[-2])    # o    <- the second-to-last character
```

If you ask for a position that doesn't exist, Python tells you so — loudly.

```python
word = "python"
print(word[6])
# IndexError: string index out of range
```

`"python"` has 6 characters, at positions 0 through 5. Position 6 doesn't exist. `IndexError` means you asked for a spot outside the string.

**Predict the output before you run this:**

```python
name = "study group"
print(name[0])
print(name[-1])
```

`name[0]` is `"s"` and `name[-1]` is `"p"` — the first and last characters, whatever they happen to be.

## Slicing: Grabbing a Chunk

Indexing gets one character. Slicing gets a range of characters, using `start:stop`.

```python
word = "python"
print(word[1:4])    # yth   <- positions 1, 2, and 3
```

Slicing includes the start position but stops *before* the stop position. `word[1:4]` gives you positions 1, 2, 3 — not 4.

> **Common mistake:** assuming `word[1:4]` includes position 4. It doesn't. The stop number is where slicing stops, not the last thing it grabs. Think of the numbers as pointing to the gaps *between* letters, not the letters themselves.

You can leave off either side of the colon:

```python
word = "python"
print(word[:3])     # pyt   <- everything from the start up to (not including) 3
print(word[3:])     # hon   <- everything from 3 to the end
```

Leaving off the start means "start from 0." Leaving off the stop means "go to the end."

A neat trick: use a step of `-1` to reverse a string.

```python
word = "python"
print(word[::-1])    # nohtyp
```

**Predict the output before you run this:**

```python
word = "python"
print(word[2:5])
```

It prints `tho` — positions 2, 3, and 4 (`t`, `h`, `o`). Position 5 is excluded because it's the stop index.

## Strings Are Immutable

Once a string exists, you cannot change individual characters inside it. This is called being **immutable**.

```python
word = "python"
word[0] = "P"
# TypeError: 'str' object does not support item assignment
```

You cannot reach into a string and swap out a letter. Instead, you build a *new* string out of the pieces you want.

```python
word = "python"
word = "P" + word[1:]
print(word)    # Python
```

Here we kept everything from position 1 onward (`"ython"`) and stuck a new `"P"` on the front. `word` now points to a brand-new string — the old one wasn't edited, it was replaced.

## Useful String Methods

A method is a function attached to a string, called with a dot: `string.method()`. Methods never change the original string — every single one of them **returns a new string** and leaves the original exactly as it was.

### Changing Case

```python
name = "Alice"
print(name.upper())    # ALICE
print(name)             # Alice
```

> **Common mistake:** thinking `.upper()` changes `name` itself. Look at the second `print(name)` above — it still says `"Alice"`. `.upper()` handed back a new, shouted version; it didn't touch the original. If you want to keep the change, you have to save it: `name = name.upper()`.

```python
shout = "STOP RUNNING"
print(shout.lower())    # stop running
```

### Cleaning Up

`.strip()` removes whitespace from the front and back of a string — handy for messy user input.

```python
messy = "   hello   "
print(len(messy))            # 11
print(len(messy.strip()))    # 5
```

The extra spaces are gone from the *result*, but `messy` itself is unchanged, same as every other method.

### Finding and Counting

`.replace()` swaps every occurrence of one piece of text for another.

```python
sentence = "I like cats"
print(sentence.replace("cats", "dogs"))    # I like dogs
print(sentence)                             # I like cats
```

> **Common mistake:** assuming `.replace()` edits `sentence` in place. It doesn't — same rule as `.upper()`. The original is untouched; `.replace()` gives you a new string with the swap made.

`.count()` tells you how many times something appears.

```python
word = "banana"
print(word.count("a"))    # 3
```

### Splitting and Joining

`.split()` breaks a string into a list of pieces, splitting on spaces by default.

```python
sentence = "the quick brown fox"
words = sentence.split()
print(words)    # ['the', 'quick', 'brown', 'fox']
```

You can split on something other than a space:

```python
csv_line = "apple,banana,cherry"
items = csv_line.split(",")
print(items)    # ['apple', 'banana', 'cherry']
```

`.join()` does the reverse: it glues a list of strings back together with something in between. It's called *on* the glue, not the list.

```python
words = ["I", "love", "pizza"]
sentence = " ".join(words)
print(sentence)    # I love pizza
```

### Checking the Start

`.startswith()` checks whether a string begins with certain text, and gives back `True` or `False`.

```python
filename = "report.txt"
print(filename.startswith("report"))    # True
print(filename.startswith("Report"))    # False
```

Methods that check text are case-sensitive by default — `"report"` and `"Report"` are not the same thing to Python.

## Checking Membership with in

`in` checks whether one piece of text appears inside another. It also gives back `True` or `False`.

```python
password = "sunshine123"
print("sun" in password)     # True
print("moon" in password)    # False
```

This is often used inside `if` statements:

```python
name = "Alice"
if "A" in name:
    print("found it")    # found it
```

## Converting Between Strings and Numbers

`str()` turns a number into a string. `int()` turns a string (that looks like a whole number) into a number.

```python
age = 25
message = "I am " + str(age) + " years old"
print(message)    # I am 25 years old
```

Without `str(age)`, this line would raise the same `TypeError` you saw earlier — you can't `+` a string and a number directly.

```python
text = "42"
number = int(text)
print(number + 8)    # 50
```

If the text doesn't actually look like a number, `int()` refuses:

```python
int("hello")
# ValueError: invalid literal for int() with base 10: 'hello'
```

`ValueError` means the *type* was right (it was a string) but the *value* inside it made no sense as a number.

## f-strings: Building Strings with Variables

An f-string lets you drop variables straight into a string, without any `+` gluing. Put an `f` right before the opening quote, and wrap each variable in curly braces.

```python
name = "Alice"
age = 25
print(f"{name} is {age} years old")    # Alice is 25 years old
```

Compare this to doing it with `+`:

```python
# Old way — clunky, and you must remember str()
print(name + " is " + str(age) + " years old")

# f-string way — cleaner, no str() needed
print(f"{name} is {age} years old")
```

Both print the same thing, but the f-string handles the number-to-string conversion for you and is much easier to read.

You can put whole expressions inside the braces, not just variable names:

```python
a = 4
b = 7
print(f"{a} + {b} = {a + b}")    # 4 + 7 = 11
```

You can also control number formatting. `:.2f` means "show two digits after the decimal point":

```python
price = 3.14159
print(f"{price:.2f}")    # 3.14
```

## Putting It Together: Worked Examples

### Cleaning Up User Input

People type messy things — extra spaces, wrong case. A common pattern is to `.strip()` and `.lower()` in one line:

```python
raw_input = "   ALICE@EMAIL.COM   "
clean = raw_input.strip().lower()
print(clean)    # alice@email.com
```

Reading this left to right: `.strip()` runs first on `raw_input` and returns a new string with no leading/trailing spaces. `.lower()` then runs on *that* result. Methods can be chained one after another like this because each one hands back a string the next method can work on.

### Pulling Initials Out of a Name

```python
full_name = "grace hopper"
first, last = full_name.split()
initials = first[0].upper() + last[0].upper()
print(initials)    # GH
```

Steps happening here:

1. `.split()` breaks `"grace hopper"` into `["grace", "hopper"]`.
2. `first, last = ...` unpacks the two list items into two variables.
3. `first[0]` and `last[0]` grab the first letter of each name.
4. `.upper()` capitalizes each letter, and `+` glues them together.

### A Tiny Receipt Line

```python
line = "coffee,4,2"
item, price, qty = line.split(",")
total = int(price) * int(qty)
print(f"You bought {qty} {item}(s) for ${total}")
# You bought 2 coffee(s) for $8
```

`line.split(",")` turns the raw text into three string pieces. `price` and `qty` are still strings at that point (`"4"` and `"2"`), so they need `int()` before you can multiply them. The f-string at the end pulls everything together into one readable line.

## Summary

- A string is text in quotes; `"5"` is text, `5` is a number, and they are never equal.
- Use single or double quotes consistently; use the other kind (or a backslash) when your text itself contains a quote.
- `+` joins strings but adds no spaces on its own; `*` repeats a string.
- `len()` counts characters, including spaces.
- Indexing (`word[0]`) counts from **0**; negative indexes count from the end, with `-1` as the last character.
- Slicing (`word[1:4]`) grabs a range, including the start and excluding the stop.
- Strings are immutable — no method or assignment changes the original string. Every method returns a **new** string.
- `.upper()`, `.lower()`, `.strip()`, `.replace()`, `.count()`, `.split()`, `.join()`, and `.startswith()` are the workhorse methods; none of them modify the original.
- `in` checks membership and returns `True` or `False`.
- `str()` and `int()` convert between text and numbers; conversions can fail with a `ValueError` if the text doesn't look like a number.
- f-strings (`f"{name}"`) are the cleanest way to build a string out of variables.

## Practice Problems

**Easy**

1. Make a variable `city = "boston"`. Print it in all uppercase without changing `city` itself.
2. Given `word = "keyboard"`, print the first character and the last character using indexing.
3. Given `full_name = "Ada Lovelace"`, use `len()` to print how many characters it contains.

**Medium**

4. Given `phrase = "  too much   space  "`, produce a clean version with no leading/trailing spaces, and count how many characters you removed.
5. Given `sentence = "red,green,blue,yellow"`, split it into a list of colors, then rejoin them with `" and "` between each one.
6. Write an f-string that prints `"3 x 4 = 12"` using variables `x = 3` and `y = 4` (don't hardcode the answer — let Python compute it).

**Challenge**

7. Given `email = "  Jane.Doe@EXAMPLE.com  "`, produce a cleaned-up, all-lowercase version with no extra spaces, in one line using chained methods.
8. Given `word = "level"`, write code that checks whether the string reversed is equal to the string itself (a palindrome check), using slicing.
9. Given `data = "name:Alice,age:30,city:Boston"`, split it into three separate `key:value` pairs, then split each pair on `:` to print just the three values (`Alice`, `30`, `Boston`).
