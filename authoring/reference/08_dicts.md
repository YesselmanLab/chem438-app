# Dictionaries
unit: 8

## A dict is a lookup table

```python
scores = {"Ana": 88, "Ben": 72, "Cleo": 95}
print(scores["Ben"])
# 72
```

You looked up `"Ben"` and got back `72`. That's the whole idea. A **dictionary** (a **dict**) stores pairs: a **key** you look things up by, and a **value** you get back.

Read the code out loud as "the score for Ben." That's how a dict reads — you ask by name, not by position.

A list makes you know *where* something is:

```python
names = ["Ana", "Ben", "Cleo"]
score_list = [88, 72, 95]
print(score_list[1])
# 72
```

That works, but you had to know Ben was at index `1`, and you had to keep two lists lined up forever. Add one name to the wrong list and every answer after it is silently wrong. The dict keeps the pair together, so it can't drift apart.

**Use a dict when you want to look something up by a name instead of by a position.**

- phone book: name -> number
- receipt: item -> price
- tally: word -> how many times you saw it
- settings: option -> chosen value

## Making a dict

Curly braces, then `key: value` pairs separated by commas.

```python
prices = {"apple": 50, "banana": 25, "cherry": 300}
print(prices)
# {'apple': 50, 'banana': 25, 'cherry': 300}
```

An empty dict is just empty braces. You fill it in later:

```python
seats = {}
print(seats)
print(len(seats))
# {}
# 0
```

Values can be anything — numbers, strings, booleans, even lists:

```python
song = {"title": "Clocks", "artist": "Coldplay", "minutes": 5, "favorite": True}
print(song["artist"])
print(song["favorite"])
# Coldplay
# True
```

Keys are usually strings, but numbers work too:

```python
seat_owner = {12: "Ana", 13: "Ben", 14: "Cleo"}
print(seat_owner[13])
# Ben
```

> **Careful: `seat_owner[13]` is a KEY, not a position.** It looks exactly like a list index, but it isn't one. There is no seat `0`, `1`, or `2` here — asking for `seat_owner[0]` is asking for the key `0`, which doesn't exist, and that's a `KeyError`. A dict has no order-based access at all.

## Looking up a value with `d[key]`

Square brackets with the key inside:

```python
song = {"title": "Clocks", "artist": "Coldplay", "minutes": 5, "favorite": True}
print(song["title"])
print(song["minutes"])
# Clocks
# 5
```

The key can come from a variable, which is where dicts start to earn their keep:

```python
scores = {"Ana": 88, "Ben": 72, "Cleo": 95}
who = "Cleo"
print(scores[who])
# 95
```

The value that comes out is an ordinary value — do math on it, print it, pass it to a function:

```python
scores = {"Ana": 88, "Ben": 72, "Cleo": 95}
print(scores["Ana"] + 5)
print(scores["Ana"] > scores["Ben"])
# 93
# True
```

## KeyError: asking for a key that isn't there

This is the error you will meet most. Ask for a key the dict doesn't have and Python stops:

```python
scores = {"Ana": 88, "Ben": 72, "Cleo": 95}
print(scores["Dana"])

# KeyError: 'Dana'
```

> **Misconception: "a missing key just gives me nothing / zero / `None`."** It doesn't. It **crashes**. There's no silent fallback, no empty answer — your program stops right there. Proof:

```python
scores = {"Ana": 88, "Ben": 72, "Cleo": 95}
print("before")
print(scores["Dana"])
print("after")

# before
# KeyError: 'Dana'
```

`"after"` never printed. The `KeyError` ended the program on the line above it. Python tells you exactly which key it couldn't find — that quoted name in the message is the key you asked for.

Keys are exact. Capitalization counts, and so does a stray space:

```python
scores = {"Ana": 88, "Ben": 72, "Cleo": 95}
print(scores["ana"])

# KeyError: 'ana'
```

`"ana"` and `"Ana"` are different strings, so they are different keys. When a `KeyError` surprises you, print the dict and look at the key you actually asked for — nine times out of ten it's a typo, a case difference, or a number where you meant a string.

```python
ages = {1: "one", 2: "two"}
print(ages[1])
print(ages["1"])

# one
# KeyError: '1'
```

The key `1` (a number) and the key `"1"` (a string) are not the same key.

## `.get()` — a safe lookup with a default

`.get()` asks the same question, but it never crashes. Missing key? You get `None` back:

```python
scores = {"Ana": 88, "Ben": 72, "Cleo": 95}
print(scores.get("Ana"))
print(scores.get("Dana"))
# 88
# None
```

Better: give `.get()` a second argument, the value to use when the key is missing.

```python
scores = {"Ana": 88, "Ben": 72, "Cleo": 95}
print(scores.get("Ana", 0))
print(scores.get("Dana", 0))
# 88
# 0
```

Now a missing student scores `0` instead of blowing up. That second argument is called the **default**.

The contrast, side by side. The wrong version:

```python
scores = {"Ana": 88, "Ben": 72, "Cleo": 95}

def report(name):
    return name + " scored " + str(scores[name])

print(report("Ben"))
print(report("Dana"))

# Ben scored 72
# KeyError: 'Dana'
```

The right version:

```python
scores = {"Ana": 88, "Ben": 72, "Cleo": 95}

def report(name):
    return name + " scored " + str(scores.get(name, 0))

print(report("Ben"))
print(report("Dana"))
# Ben scored 72
# Dana scored 0
```

`.get()` does not change the dict — it just answers. The dict still has three keys:

```python
scores = {"Ana": 88, "Ben": 72, "Cleo": 95}
scores.get("Dana", 0)
print(scores)
# {'Ana': 88, 'Ben': 72, 'Cleo': 95}
```

**When to use which:** use `d[key]` when the key *must* be there and a crash is the correct, loud response to it missing. Use `d.get(key, default)` when a missing key is a normal thing that can happen and you have a sensible fallback.

## Adding and changing keys

Assign to a key. If the key is new, it's added. If it already exists, its value is replaced.

```python
seats = {}
seats["12A"] = "Ana"
seats["12B"] = "Ben"
print(seats)
# {'12A': 'Ana', '12B': 'Ben'}
```

```python
seats["12B"] = "Cleo"
print(seats)
# {'12A': 'Ana', '12B': 'Cleo'}
```

Same syntax for both. Python doesn't ask whether you meant "add" or "change" — it looks at whether the key is already there and does the right one. Ben is simply gone; nothing warned you.

> **Misconception: "dicts can't change once you make them."** Strings can't change — a dict absolutely can. It is built to be changed. Add keys, replace values, delete keys, all in place.

```python
d = {"a": 1}
d["b"] = 2
d["a"] = 99
print(d)
# {'a': 99, 'b': 2}
```

Notice there's no `d = d.something(...)` there. Unlike `"abc".upper()`, which hands you a **new** string and leaves the old one alone, changing a dict changes the dict you already have. No reassignment needed.

Values update from their own old value, too — that's the heart of counting:

```python
counts = {"red": 1}
counts["red"] = counts["red"] + 1
counts["red"] += 1
print(counts)
# {'red': 3}
```

## Removing a key with `del`

```python
seats = {"12A": "Ana", "12B": "Ben", "12C": "Cleo"}
del seats["12B"]
print(seats)
print(len(seats))
# {'12A': 'Ana', '12C': 'Cleo'}
# 2
```

`del` on a key that isn't there is a `KeyError`, same as looking it up:

```python
seats = {"12A": "Ana", "12C": "Cleo"}
del seats["99Z"]

# KeyError: '99Z'
```

Check first if you're not sure:

```python
seats = {"12A": "Ana", "12C": "Cleo"}
if "99Z" in seats:
    del seats["99Z"]
print(seats)
# {'12A': 'Ana', '12C': 'Cleo'}
```

Or use `.pop()`, which removes a key *and* hands you the value, with a default if it's missing:

```python
seats = {"12A": "Ana", "12C": "Cleo"}
gone = seats.pop("12A")
print(gone)
print(seats.pop("99Z", "nobody"))
print(seats)
# Ana
# nobody
# {'12C': 'Cleo'}
```

## `in` tests keys, not values

```python
scores = {"Ana": 88, "Ben": 72, "Cleo": 95}
print("Ben" in scores)
print("Dana" in scores)
# True
# False
```

Predict this one before you read on: what does `72 in scores` print?

```python
scores = {"Ana": 88, "Ben": 72, "Cleo": 95}
print(72 in scores)
# False
```

`False` — even though `72` is right there in the dict. It's a **value**, and `in` on a dict only ever looks at the **keys**.

> **Misconception: "`in` searches the whole dict."** It searches the keys and nothing else. This is the quiet bug: `72 in scores` is `False`, no error, no warning — just a wrong answer you might not notice for an hour.

```python
scores = {"Ana": 88, "Ben": 72, "Cleo": 95}
print("Ana" in scores)
print(88 in scores)
# True
# False
```

`"Ana"` is a key, so `True`. `88` is only a value, so `False`. If you really want to search the values, say so with `.values()`:

```python
scores = {"Ana": 88, "Ben": 72, "Cleo": 95}
print(88 in scores.values())
print(88 in scores.keys())
# True
# False
```

This is also the safe way to avoid a `KeyError`:

```python
scores = {"Ana": 88, "Ben": 72, "Cleo": 95}
name = "Dana"
if name in scores:
    print(scores[name])
else:
    print(name + " is not on the list")
# Dana is not on the list
```

`not in` works exactly as you'd expect:

```python
scores = {"Ana": 88, "Ben": 72, "Cleo": 95}
print("Dana" not in scores)
# True
```

## `len()` — how many pairs

`len()` counts the keys, which is the same as counting the pairs.

```python
scores = {"Ana": 88, "Ben": 72, "Cleo": 95}
print(len(scores))
print(len({}))
# 3
# 0
```

An empty dict is falsy, so you can test it directly:

```python
basket = {}
if not basket:
    print("basket is empty")
# basket is empty
```

## Keys must be unique

A dict cannot hold the same key twice. Write a key twice in one literal and the **last one silently wins**:

```python
prices = {"apple": 50, "banana": 25, "apple": 70}
print(prices)
print(len(prices))
# {'apple': 70, 'banana': 25}
# 2
```

> **Misconception: "a repeated key adds a second entry."** There is no second entry, and there is no error. The later value overwrites the earlier one, quietly. `len()` is `2`, not `3` — and notice `"apple"` stayed in its **original** position while taking the **new** value.

```python
votes = {"Ana": "yes", "Ben": "no", "Ana": "no"}
print(votes)
print(len(votes))
# {'Ana': 'no', 'Ben': 'no'}
# 2
```

Ana's `"yes"` is gone forever. If you meant "Ana voted twice," a dict of single values is the wrong shape for your data — you'd want the key to hold a list, or you'd want to count.

The same thing happens when you assign in a loop over data with repeats — usually a real bug:

```python
rows = [("Ana", 88), ("Ben", 72), ("Ana", 95)]

best = {}
for name, score in rows:
    best[name] = score

print(best)
# {'Ana': 95, 'Ben': 72}
```

Ana's `88` was overwritten by her `95`. If you wanted her *highest* score that's a lucky accident; if you wanted her *first*, you got the wrong answer. Say what you mean:

```python
rows = [("Ana", 88), ("Ben", 72), ("Ana", 95)]

best = {}
for name, score in rows:
    if name not in best or score > best[name]:
        best[name] = score

print(best)
# {'Ana': 95, 'Ben': 72}
```

Values, unlike keys, can repeat as much as they like:

```python
grades = {"Ana": "A", "Ben": "A", "Cleo": "A"}
print(grades)
print(len(grades))
# {'Ana': 'A', 'Ben': 'A', 'Cleo': 'A'}
# 3
```

## `.keys()`, `.values()`, `.items()`

Three views of the same dict:

```python
scores = {"Ana": 88, "Ben": 72, "Cleo": 95}
print(scores.keys())
print(scores.values())
print(scores.items())
# dict_keys(['Ana', 'Ben', 'Cleo'])
# dict_values([88, 72, 95])
# dict_items([('Ana', 88), ('Ben', 72), ('Cleo', 95)])
```

Those `dict_keys(...)` wrappers look odd. They're not lists — they're live views onto the dict. You can loop over them, use `in` on them, and `len()` them. If you want a real list, say `list(...)`:

```python
scores = {"Ana": 88, "Ben": 72, "Cleo": 95}
print(list(scores.keys()))
print(list(scores.values()))
print(list(scores.items()))
# ['Ana', 'Ben', 'Cleo']
# [88, 72, 95]
# [('Ana', 88), ('Ben', 72), ('Cleo', 95)]
```

Each item from `.items()` is a **pair** — the key and the value together:

```python
scores = {"Ana": 88, "Ben": 72, "Cleo": 95}
pairs = list(scores.items())
print(pairs[0])
print(pairs[0][0])
print(pairs[0][1])
# ('Ana', 88)
# Ana
# 88
```

Now the useful bits. `.values()` lets you total or compare values, since a dict itself won't:

```python
scores = {"Ana": 88, "Ben": 72, "Cleo": 95}
print(sum(scores.values()))
print(max(scores.values()))
print(min(scores.values()))
print(sum(scores.values()) / len(scores))
# 255
# 95
# 72
# 85.0
```

And `sorted()` on a dict gives you the keys, sorted:

```python
scores = {"Cleo": 95, "Ana": 88, "Ben": 72}
print(sorted(scores))
# ['Ana', 'Ben', 'Cleo']
```

## Looping with `.items()`

Loop the dict directly and you get **keys**, one at a time:

```python
scores = {"Ana": 88, "Ben": 72, "Cleo": 95}
for name in scores:
    print(name)
# Ana
# Ben
# Cleo
```

Just the names — no scores. That surprises people. To get both, loop `.items()` and unpack into two variables:

```python
scores = {"Ana": 88, "Ben": 72, "Cleo": 95}
for name, score in scores.items():
    print(name + ": " + str(score))
# Ana: 88
# Ben: 72
# Cleo: 95
```

`for name, score in scores.items():` reads as "for each name-and-score pair in the dict." The two names on the left are yours to choose — `for k, v in ...` works identically, just less readably.

This is the standard way to walk a dict. An f-string makes it neater:

```python
prices = {"apple": 50, "banana": 25, "cherry": 300}
for item, cents in prices.items():
    print(f"{item:8} {cents:4} cents")
# apple      50 cents
# banana     25 cents
# cherry    300 cents
```

Loops read as well as write:

```python
scores = {"Ana": 88, "Ben": 72, "Cleo": 95}

passing = 0
for name, score in scores.items():
    if score >= 80:
        passing += 1

print(passing)
# 2
```

Dicts remember the order you inserted keys in, so loops come out in that order every time — not sorted, **insertion** order. Want alphabetical? Ask for it:

```python
scores = {"Cleo": 95, "Ana": 88, "Ben": 72}
for name in sorted(scores):
    print(name, scores[name])
# Ana 88
# Ben 72
# Cleo 95
```

> **Watch out: don't add or delete keys while looping over the dict.** Python refuses, because the thing you're walking changed underneath you.

```python
scores = {"Ana": 88, "Ben": 72, "Cleo": 95}
for name in scores:
    if scores[name] < 80:
        del scores[name]

# RuntimeError: dictionary changed size during iteration
```

Loop over a snapshot instead. `list(scores)` copies the keys out first, so deleting from the dict can't disturb the loop:

```python
scores = {"Ana": 88, "Ben": 72, "Cleo": 95}
for name in list(scores):
    if scores[name] < 80:
        del scores[name]
print(scores)
# {'Ana': 88, 'Cleo': 95}
```

## Counting with a dict: the tally pattern

This is the single most useful thing dicts do. Learn it cold — you will write it for the rest of your life.

**The problem:** you have a pile of things and you want to know how many of each.

```python
votes = ["red", "blue", "red", "green", "red", "blue"]

tally = {}
for color in votes:
    if color in tally:
        tally[color] += 1
    else:
        tally[color] = 1

print(tally)
# {'red': 3, 'blue': 2, 'green': 1}
```

Walk it through. `tally` starts empty. For each color:

1. If we've seen it before, its key already exists — add one to it.
2. If we haven't, there's no key to add one *to*, so start it at `1`.

Step 2 is the part everyone forgets. Skip it and you get a `KeyError` on the very first color:

```python
votes = ["red", "blue", "red"]

tally = {}
for color in votes:
    tally[color] += 1

# KeyError: 'red'
```

Read that line as `tally["red"] = tally["red"] + 1`. To add one to `tally["red"]`, Python must first *read* `tally["red"]` — and on the first loop that key does not exist yet. There is nothing to add one to.

**The shorter version, using `.get()`:**

```python
votes = ["red", "blue", "red", "green", "red", "blue"]

tally = {}
for color in votes:
    tally[color] = tally.get(color, 0) + 1

print(tally)
# {'red': 3, 'blue': 2, 'green': 1}
```

One line instead of four, and no `if` at all. `tally.get(color, 0)` means "the count so far, or `0` if this is the first time." Then add one and store it back. The first sighting of `"red"` computes `0 + 1`; the second computes `1 + 1`. That `0` default is exactly the "start it at 1" case, folded in.

**This is the pattern. Memorize this shape:**

```python
counts = {}
for thing in ["a", "b", "a", "a"]:
    counts[thing] = counts.get(thing, 0) + 1
print(counts)
# {'a': 3, 'b': 1}
```

It works on anything you can loop over. Letters in a word:

```python
word = "mississippi"

letters = {}
for ch in word:
    letters[ch] = letters.get(ch, 0) + 1

print(letters)
# {'m': 1, 'i': 4, 's': 4, 'p': 2}
```

Words in a sentence:

```python
sentence = "the cat sat on the mat the end"

words = {}
for w in sentence.split():
    words[w] = words.get(w, 0) + 1

print(words)
print(words["the"])
# {'the': 3, 'cat': 1, 'sat': 1, 'on': 1, 'mat': 1, 'end': 1}
# 3
```

Dice rolls:

```python
rolls = [3, 6, 1, 3, 3, 6, 2]

seen = {}
for r in rolls:
    seen[r] = seen.get(r, 0) + 1

print(seen)
print(seen.get(5, 0))
# {3: 3, 6: 2, 1: 1, 2: 1}
# 0
```

Same six lines every time. Only the thing being counted changes.

Once you have a tally, the questions get easy:

```python
rolls = [3, 6, 1, 3, 3, 6, 2]

seen = {}
for r in rolls:
    seen[r] = seen.get(r, 0) + 1

print(len(seen))
print(sum(seen.values()))
print(max(seen, key=seen.get))
# 4
# 7
# 3
```

- `len(seen)` — how many **different** values showed up.
- `sum(seen.values())` — how many rolls in total.
- `max(seen, key=seen.get)` — the key with the biggest count. Read it as "the largest key, judged by its count." This is how you get "the winner."

Tallies aren't only for counting by ones. Swap `+ 1` for any amount and you're summing:

```python
sales = [("Ana", 30), ("Ben", 12), ("Ana", 5), ("Cleo", 8), ("Ben", 20)]

totals = {}
for name, amount in sales:
    totals[name] = totals.get(name, 0) + amount

print(totals)
print(max(totals, key=totals.get))
# {'Ana': 35, 'Ben': 32, 'Cleo': 8}
# Ana
```

## A dict as a lookup table

Here's an if/elif chain that does nothing but match a key to a value:

```python
def points_slow(grade):
    if grade == "A":
        return 4
    elif grade == "B":
        return 3
    elif grade == "C":
        return 2
    elif grade == "D":
        return 1
    else:
        return 0

print(points_slow("B"))
# 3
```

Eleven lines. Every branch has the same shape. Adding a grade means adding two more lines and hoping you didn't fat-finger one. That's what a dict is for:

```python
POINTS = {"A": 4, "B": 3, "C": 2, "D": 1, "F": 0}

def points(grade):
    return POINTS.get(grade, 0)

print(points("B"))
print(points("A"))
print(points("Z"))
# 3
# 4
# 0
```

Two lines of logic. The data lives in one obvious place, adding a grade is one comma, and `.get()` handles the unknown case that `else` used to.

**When an if/elif chain is really just a table, make it a table.** The tell: every branch compares the *same* variable to a constant with `==`, and every branch returns a constant.

More of the same idea:

```python
NAMES = {"N": "north", "S": "south", "E": "east", "W": "west"}
print(NAMES["N"])
print(NAMES.get("Q", "unknown direction"))
# north
# unknown direction
```

```python
ROMAN = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100}

total = 0
for ch in "XXVI":
    total += ROMAN[ch]

print(total)
# 26
```

A dict can even map to functions, but a table of values covers almost everything you'll meet:

```python
EMOJI_NAME = {":)": "smile", ":(": "frown", ":D": "grin"}

message = "hello :) goodbye :("
for token in message.split():
    if token in EMOJI_NAME:
        print(EMOJI_NAME[token])
# smile
# frown
```

## Don't use a list of pairs where a dict belongs

You *can* store pairs in a list. It's almost always worse.

```python
pairs = [["Ana", 88], ["Ben", 72], ["Cleo", 95]]

def find_score(pairs, name):
    for pair in pairs:
        if pair[0] == name:
            return pair[1]
    return None

print(find_score(pairs, "Cleo"))
# 95
```

Six lines and a loop to answer one question. The dict version:

```python
scores = {"Ana": 88, "Ben": 72, "Cleo": 95}
print(scores["Cleo"])
# 95
```

> **Misconception: "a list of pairs is basically a dict."** It isn't, and the differences bite.

- Looking something up takes a loop **you** have to write, and it checks every pair one by one. A dict jumps straight to the answer, however big it gets.
- Nothing stops duplicate names. Add `["Ana", 50]` and the list happily holds two Anas.
- Updating a score means hunting down the right pair and changing it. In a dict it's `scores["Ana"] = 50`.

```python
pairs = [["Ana", 88], ["Ben", 72], ["Ana", 50]]
print(find_score(pairs, "Ana"))
# 88
```

Two Anas, no complaint, and the `50` is invisible — `find_score` returned whichever it hit first, and nothing told you there was another. A dict makes that impossible by design: one key, one value.

Use a list when order and repeats are the point (a queue, a playlist, every roll of a die). Use a dict when "look this up by name" is the point.

## What can be a key

Keys have to be things that can't change: strings, numbers, booleans, tuples. A list can't be a key.

```python
d = {}
d[["a", "b"]] = 1

# TypeError: unhashable type: 'list'
```

"Unhashable" is Python's word for "this thing can change, so I can't file it away reliably." Use a tuple — a fixed, unchangeable sequence — instead:

```python
grid = {}
grid[(0, 0)] = "start"
grid[(1, 2)] = "treasure"
print(grid[(1, 2)])
print(grid)
# treasure
# {(0, 0): 'start', (1, 2): 'treasure'}
```

Values have no such rule — a value can be a list, another dict, anything:

```python
teams = {"red": ["Ana", "Ben"], "blue": ["Cleo"]}
teams["blue"].append("Dana")
print(teams)
print(len(teams["blue"]))
# {'red': ['Ana', 'Ben'], 'blue': ['Cleo', 'Dana']}
# 2
```

## Worked example: a shopping basket

Count the items, price them from a lookup table, print a total.

```python
PRICES = {"apple": 50, "banana": 25, "cherry": 300}

basket = ["apple", "banana", "apple", "cherry", "apple"]

counts = {}
for item in basket:
    counts[item] = counts.get(item, 0) + 1

total = 0
for item, n in counts.items():
    cost = PRICES[item] * n
    total += cost
    print(f"{item:8} x{n}  {cost:5} cents")

print(f"{'TOTAL':8}     {total:5} cents")
# apple    x3    150 cents
# banana   x1     25 cents
# cherry   x1    300 cents
# TOTAL          475 cents
```

Three dict ideas in nine lines: a tally to count the basket, a lookup table for prices, and `.items()` to walk the result. Notice `PRICES` and `counts` are both dicts doing completely different jobs — one is fixed reference data, one is built up as you go.

## Worked example: word frequency report

```python
text = "the quick brown fox jumps over the lazy dog the fox naps"

counts = {}
for w in text.split():
    counts[w] = counts.get(w, 0) + 1

print(f"{len(text.split())} words, {len(counts)} different")
print(f"most common: {max(counts, key=counts.get)}")

for w in sorted(counts):
    if counts[w] > 1:
        print(f"{w:6} {counts[w]}")
# 12 words, 9 different
# most common: the
# fox    2
# the    3
```

`sorted(counts)` walks the keys alphabetically; `counts[w] > 1` keeps only the repeats. Swap `sorted(counts)` for plain `counts` and you'd get them in the order they first appeared instead.

## Predict before you run

Work each out on paper first, then run it.

```python
d = {"a": 1, "b": 2}
d["c"] = 3
d["a"] = 10
del d["b"]
print(d)
print(len(d))
```

```python
d = {"x": 1, "y": 2, "x": 3}
print(len(d))
print(d["x"])
print("z" in d)
print(2 in d)
```

```python
items = ["pen", "cup", "pen", "pen", "cup"]
c = {}
for i in items:
    c[i] = c.get(i, 0) + 1
print(c)
print(c.get("pen", 0))
print(c.get("hat", 0))
print(max(c, key=c.get))
```

## Quick reference — what's available

### Making and measuring

- `{}` — a new empty dict
- `{"a": 1, "b": 2}` — a dict with pairs already in it
- `dict(a=1, b=2)` — same thing, when keys are simple names
- `len(d)` — how many pairs
- `not d` — `True` when the dict is empty

### Getting a value out

- `d[key]` — the value for `key`; **`KeyError`** if it's missing
- `d.get(key)` — the value, or `None` if missing; never crashes
- `d.get(key, default)` — the value, or `default` if missing
- `d.setdefault(key, default)` — the value; inserts `default` first if the key is missing

### Adding, changing, removing

- `d[key] = value` — add the key, or replace its value if it's already there
- `d[key] += 1` — bump a value (the key must already exist)
- `del d[key]` — remove the pair; `KeyError` if missing
- `d.pop(key)` — remove it and hand back the value; `KeyError` if missing
- `d.pop(key, default)` — same, but `default` instead of crashing
- `d.update(other)` — copy another dict's pairs in, overwriting clashes
- `d.clear()` — remove everything
- `d.copy()` — a separate dict with the same pairs

### Looking around

- `key in d` / `key not in d` — tests **keys** only
- `value in d.values()` — how you test values
- `d.keys()` — a view of the keys
- `d.values()` — a view of the values
- `d.items()` — a view of `(key, value)` pairs
- `list(d)` — the keys, as a real list
- `sorted(d)` — the keys, sorted, as a list

### Looping

- `for key in d:` — keys, in insertion order
- `for key, value in d.items():` — both at once — the usual choice
- `for key in sorted(d):` — keys in alphabetical/numeric order
- `for key in list(d):` — a snapshot, safe to delete from `d` inside the loop

### Whole-dict answers

- `sum(d.values())` — total of the values
- `max(d.values())` / `min(d.values())` — biggest/smallest value
- `max(d, key=d.get)` — the key with the biggest value ("who won")
- `sorted(d.values())` — the values, sorted

### The one pattern to memorize

- `counts[thing] = counts.get(thing, 0) + 1` — the tally

Most of it at once:

```python
basket = ["pen", "cup", "pen", "pad", "pen", "cup"]
PRICE = {"pen": 2, "cup": 7, "pad": 4}

counts = {}
for item in basket:
    counts[item] = counts.get(item, 0) + 1

print(counts)
print(len(counts), "different items,", sum(counts.values()), "total")
print("most bought:", max(counts, key=counts.get))
print("pen" in counts, "mug" in counts)
print(counts.get("mug", 0))

for item in sorted(counts):
    print(f"{item:4} x{counts[item]} = {PRICE[item] * counts[item]:2}")

counts["mug"] = 1
del counts["pad"]
print(sorted(counts))
# {'pen': 3, 'cup': 2, 'pad': 1}
# 3 different items, 6 total
# most bought: pen
# True False
# 0
# cup  x2 = 14
# pad  x1 =  4
# pen  x3 =  6
# ['cup', 'mug', 'pen']
```
