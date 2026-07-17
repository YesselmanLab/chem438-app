# Strings — building & methods

Build strings with `*`, `+`, and f-strings, and clean them up with the string methods.

---

## loading_bar
kind: code_fn
title: Draw a loading bar
tags: strings, functions, language_fundamentals
see: 02_strings#repeating-strings-with
difficulty: starter
entry: loading_bar

### prompt
A progress bar is just a row of repeated characters. Write a function
`loading_bar(n)` that returns a string made of exactly `n` equals signs.

Examples

    loading_bar(3) → "==="
    loading_bar(6) → "======"
    loading_bar(1) → "="

Notes

- The `*` operator repeats a string a whole number of times.
- `loading_bar(0)` is an empty string.
- Don't forget to return the result.

### starter
```python
def loading_bar(n):
    
```

### solution
```python
def loading_bar(n):
    return "=" * n
```

### check
loading_bar(3) == "==="
loading_bar(6) == "======"
loading_bar(1) == "="
loading_bar(0) == ""
loading_bar(30) == "=============================="

---

## trim_username
kind: code_fn
title: Tidy up the username
tags: strings, functions, validation
see: 02_strings#cleaning-up-user-input
difficulty: starter
entry: clean_username

### prompt
Usernames are stored in one standard form: no spaces around the outside, and all
lowercase. Write a function `clean_username(raw)` that returns the name with the
surrounding spaces removed AND every letter lowercased.

Examples

    clean_username("  Ada  ") → "ada"
    clean_username("GRACE ") → "grace"
    clean_username("linus") → "linus"

Notes

- Spaces in the middle of the text stay exactly where they are.
- Two steps, both needed — doing only one of them is the usual mistake.
- Don't forget to return the result.

### walkthrough
There are two jobs here, and each has its own method. `.strip()` removes the spaces
on the ends. `.lower()` turns every letter lowercase. Neither one does the other's
job, so you need both.

The natural first attempt is to do them one at a time:

    trimmed = raw.strip()
    return trimmed.lower()

That is correct, and there is nothing wrong with writing it that way. But you can
also chain the calls. `raw.strip()` hands back a string, and you can call a method
straight onto that returned string:

    return raw.strip().lower()

Read it left to right: take `raw`, strip it, lowercase the result. That is the same
two steps on one line.

Here is the mistake to name. Because strings are immutable, this does nothing:

    raw.strip()
    raw.lower()
    return raw

Each of those calls builds a new string and then throws it away, because you never
caught the result. `raw` itself is untouched, so you return exactly what you were
given. A method call whose result you don't keep is a wasted line.

### starter
```python
def clean_username(raw):
    
```

### solution
```python
def clean_username(raw):
    return raw.strip().lower()
```

### check
clean_username("  Ada  ") == "ada"
clean_username("GRACE ") == "grace"
clean_username("linus") == "linus"
clean_username("   ") == ""
clean_username("  Ada Lovelace  ") == "ada lovelace"

---

## playlist_title
kind: code_fn
title: Fix the playlist title
tags: strings, functions, formatting
see: 02_strings#changing-case
difficulty: starter
entry: fix_title

### prompt
Song titles typed in a hurry come out all lowercase. Write a function
`fix_title(name)` that returns the title with the first letter of every word
capitalized.

Examples

    fix_title("road trip mix") → "Road Trip Mix"
    fix_title("summer") → "Summer"
    fix_title("late night study") → "Late Night Study"

Notes

- Python has a string method that does exactly this in one step.
- An empty title should come back as an empty string.

### starter
```python
def fix_title(name):
    
```

### solution
```python
def fix_title(name):
    return name.title()
```

### check
fix_title("road trip mix") == "Road Trip Mix"
fix_title("summer") == "Summer"
fix_title("late night study") == "Late Night Study"
fix_title("") == ""
fix_title("a b c") == "A B C"

---

## crowd_chant
kind: code_fn
title: Start the chant
tags: strings, functions, language_fundamentals
see: 02_strings#repeating-strings-with
difficulty: easy
entry: chant

### prompt
Write a function `chant(word, times)` that returns the word followed by an
exclamation mark and a space, repeated `times` times.

Examples

    chant("go", 3) → "go! go! go! "
    chant("hey", 1) → "hey! "
    chant("win", 2) → "win! win! "

Notes

- Every repetition ends with a space, including the last one.
- If `times` is 0, the result is an empty string.

### walkthrough
The piece you want repeated is not just `word` — it's the whole chunk `word` plus
`"! "`. So first build that chunk, then repeat it:

    chunk = word + "! "
    return chunk * times

You can do it on one line, but here is the trap. Python runs `*` before `+`, the
same way it does with numbers. So this:

    return word + "! " * times

does NOT repeat the whole chunk. It repeats only `"! "`, and then glues the word
on the front once: `chant("go", 3)` gives `"go! ! ! "`. Read it out loud as
"word, plus (bang-space three times)" and the bug is obvious.

Parentheses force the addition to happen first:

    return (word + "! ") * times

Now the thing being repeated is `"go! "`, and you get `"go! go! go! "`.

### starter
```python
def chant(word, times):
    
```

### solution
```python
def chant(word, times):
    return (word + "! ") * times
```

### check
chant("go", 3) == "go! go! go! "
chant("hey", 1) == "hey! "
chant("win", 2) == "win! win! "
chant("go", 0) == ""

---

## cart_line
kind: code_fn
title: Print a cart line
tags: strings, formatting, functions
see: 02_strings#f-strings-building-strings-with-variables
difficulty: easy
entry: cart_line

### prompt
Write a function `cart_line(item, qty, price)` that returns one receipt line
showing the quantity, the item name, and the total cost for that line (quantity
times price).

Examples

    cart_line("mug", 3, 7) → "3 x mug = $21"
    cart_line("pen", 2, 5) → "2 x pen = $10"
    cart_line("hat", 1, 12) → "1 x hat = $12"

Notes

- `price` is the price of ONE item, so you have to do the multiplication yourself.
- The dollar sign goes right before the total, with no space after it.

### walkthrough
An f-string lets you drop a value into the middle of text by putting it in curly
braces:

    return f"{qty} x {item} = $..."

The part students get stuck on is the total. It's tempting to think braces can
only hold a plain variable name, so you compute the total on its own line first.
That works fine:

    total = qty * price
    return f"{qty} x {item} = ${total}"

But braces can hold any expression, so you can also write the math directly
inside them:

    return f"{qty} x {item} = ${qty * price}"

One thing to watch: the `$` sits OUTSIDE the braces. If you write `{$qty * price}`
Python has no idea what `$` means and you get a syntax error. Everything outside
the braces is just literal text; everything inside is Python.

### starter
```python
def cart_line(item, qty, price):
    
```

### solution
```python
def cart_line(item, qty, price):
    return f"{qty} x {item} = ${qty * price}"
```

### check
cart_line("mug", 3, 7) == "3 x mug = $21"
cart_line("pen", 2, 5) == "2 x pen = $10"
cart_line("hat", 1, 12) == "1 x hat = $12"
cart_line("sticker", 0, 4) == "0 x sticker = $0"

---

## fix_remove_dashes
kind: code_fn
title: The dashes won't go away
tags: strings, bugs, functions
see: 02_strings#strings-are-immutable
difficulty: easy
entry: strip_dashes

### prompt
This function is supposed to return a phone number with every dash removed, but it
hands back the number completely unchanged. Find the bug and fix it.

Examples

    strip_dashes("402-555-0199") → "4025550199"
    strip_dashes("1-2") → "12"
    strip_dashes("5551234") → "5551234"

Notes

- `.replace()` hands you back a brand-new string — it never edits the original.
- Don't forget to return the result.

### walkthrough
Run the code in your head. Line one calls `phone.replace("-", "")`. That call does
build the string `"4025550199"` — but then the line ends, nobody catches the
result, and Python throws it away. Line two returns `phone`, which is still the
original with all its dashes.

The reason is that strings in Python are immutable: nothing can change a string
once it exists. Methods like `.replace()`, `.strip()`, `.upper()` and `.title()`
never modify the string you called them on. They return a NEW string and leave the
old one alone.

So a bare method call on its own line is always useless. You have to either catch
the result in a variable:

    cleaned = phone.replace("-", "")
    return cleaned

or return it directly:

    return phone.replace("-", "")

If you ever find yourself writing `phone.strip()` on a line by itself and
wondering why nothing changed, this is why.

### starter
```python
def strip_dashes(phone):
    phone.replace("-", "")
    return phone
```

### solution
```python
def strip_dashes(phone):
    return phone.replace("-", "")
```

### check
strip_dashes("402-555-0199") == "4025550199"
strip_dashes("1-2") == "12"
strip_dashes("5551234") == "5551234"
strip_dashes("-") == ""

---

## mcq_count_ana
kind: mcq
title: Predict — "banana".count("ana")
tags: strings, predict, concept
see: 02_strings#finding-and-counting
difficulty: easy
answer: 2

### prompt
What does this code print?

    print("banana".count("ana"))

### walkthrough
Your eye finds two "ana"s in "banana": one at position 1 and one at position 3.
They overlap — they share the same "a" in the middle. But `.count()` does not see
it that way.

`.count()` scans left to right and counts NON-OVERLAPPING matches. It finds "ana"
starting at index 1, consuming positions 1, 2 and 3. Then it resumes the search at
index 4 — past everything it just used. The second "ana" starts at index 3, which
is already behind the scan, so it is never found. The answer is 1.

This is the standard trap with `.count()`, and `.replace()` and `.split()` behave
the same way. Whenever the thing you're counting can overlap itself ("aa" in
"aaa", "ana" in "banana"), expect a lower number than you counted by eye.

### choices
- 0
- 1
- 2
- 3

---

## censor_word
kind: code_fn
title: Bleep out the word
tags: strings, functions, algorithms
see: 02_strings#finding-and-counting
difficulty: medium
entry: censor

### prompt
Write a function `censor(message, word)` that replaces every appearance of `word`
with a run of asterisks the same length as that word.

Examples

    censor("that mule is a mule", "mule") → "that **** is a ****"
    censor("no bad words here", "bad") → "no *** words here"
    censor("all clear", "danger") → "all clear"

Notes

- The replacement must have exactly as many asterisks as the word has letters.
- If the word never appears, return the message unchanged.

### walkthrough
Two tools you already have, snapped together. `.replace(old, new)` swaps every
occurrence of `old` for `new`. So the shape of the answer is:

    return message.replace(word, ???)

The only question is what to put in for `???`. It's a string of asterisks — and
you can't hard-code `"****"`, because the word's length changes every call. Build
it instead: `len(word)` tells you how many you need, and `*` repeats a string that
many times:

    stars = "*" * len(word)
    return message.replace(word, stars)

The mistake to avoid is `"*" * word`, which asks Python to repeat a string a
string number of times and raises a TypeError. It's `len(word)` — a count — that
goes on the right of the `*`.

Notice you never wrote a loop. `.replace()` already handles every occurrence, and
if the word isn't there it quietly returns the message untouched.

### starter
```python
def censor(message, word):
    
```

### solution
```python
def censor(message, word):
    return message.replace(word, "*" * len(word))
```

### check
censor("that mule is a mule", "mule") == "that **** is a ****"
censor("no bad words here", "bad") == "no *** words here"
censor("all clear", "danger") == "all clear"
censor("a", "a") == "*"

---

## same_signup_name
kind: code_fn
title: Is that the same person?
tags: strings, logic, validation
see: 04_booleans#a-comparison-is-already-a-value
difficulty: medium
entry: same_person

### prompt
Two people typed their name into a signup form. Write a function `same_person(a, b)`
that returns True if the two names match once you ignore surrounding spaces and
capitalization, and False otherwise.

Examples

    same_person("  Ada ", "ada") → True
    same_person("Grace", "GRACE") → True
    same_person("ada", "linus") → False

Notes

- Spaces in the middle of a name still matter — "ada lovelace" is not "adalovelace".
- Return the boolean True or False, not a string.

### walkthrough
The temptation is to write a pile of ifs. Don't. The trick is to clean up BOTH
strings the same way first, then compare the cleaned versions with a single `==`.

Cleaning means two steps. `.strip()` removes the spaces on the ends, and `.lower()`
makes every letter lowercase so "Ada", "ADA" and "ada" all become the same text.
You can chain them, because `.strip()` returns a string and you can immediately
call `.lower()` on that string:

    return a.strip().lower() == b.strip().lower()

Two things to watch. First, you must clean BOTH sides — cleaning only `a` and
comparing it to a raw `b` fails the moment `b` has a capital. Second, don't write
`if ... : return True else: return False`. The expression `a.strip().lower() ==
b.strip().lower()` is ALREADY True or False, so returning it directly is shorter
and says exactly the same thing.

### starter
```python
def same_person(a, b):
    
```

### solution
```python
def same_person(a, b):
    return a.strip().lower() == b.strip().lower()
```

### check
same_person("  Ada ", "ada") is True
same_person("Grace", "GRACE") is True
same_person("ada", "linus") is False
same_person("ada lovelace", "adalovelace") is False
same_person("", "   ") is True
