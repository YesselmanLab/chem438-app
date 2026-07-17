# Dictionaries — more practice

Extra drills on dicts: building them, looking things up safely, the difference
between keys and values, and counting with the tally pattern.

---

## p_ages_lookup
kind: mcq
title: How old is Milo?
tags: dicts, predict
difficulty: easy
answer: 1

### prompt
A dict maps each pet's name to its age. What does this print?

    pet_age = {"rex": 4, "milo": 7}
    print(pet_age["milo"])

### code
pet_age = {"rex": 4, "milo": 7}
print(pet_age["milo"])

### choices
- 7
- 4
- milo
- rex

---

## p_dict_len_three
kind: mcq
title: How full is the backpack?
tags: dicts, predict
difficulty: easy
answer: 1

### prompt
What does this print?

    backpack = {"potion": 5, "sword": 2, "shield": 9}
    print(len(backpack))

### code
backpack = {"potion": 5, "sword": 2, "shield": 9}
print(len(backpack))

### choices
- 3
- 16
- 6
- 9

---

## p_get_missing_zero
kind: mcq
title: Texts from someone who never texts
tags: dicts, predict
difficulty: easy
answer: 1

### prompt
`unread` counts unread texts per friend. Ana isn't in it. What does this print?

    unread = {"bo": 5}
    print(unread.get("ana", 0))

### code
unread = {"bo": 5}
print(unread.get("ana", 0))

### choices
- 0
- 5
- None
- ana

---

## p_get_present_value
kind: mcq
title: Ana's score, safely
tags: dicts, predict
difficulty: easy
answer: 1

### prompt
`points` maps each player to their score. What does this print?

    points = {"ana": 7}
    print(points.get("ana", 0))

### code
points = {"ana": 7}
print(points.get("ana", 0))

### choices
- 7
- 0
- ana
- None

---

## p_in_key_true
kind: mcq
title: Is latte on the menu?
tags: dicts, predict
difficulty: easy
answer: 1

### prompt
The dict maps each drink to its price. What does this print?

    print("latte" in {"latte": 4, "mocha": 5})

### code
print("latte" in {"latte": 4, "mocha": 5})

### choices
- True
- False
- 4
- latte

---

## p_in_value_false
kind: mcq
title: Is there anything that costs 4?
tags: dicts, predict
difficulty: medium
answer: 1

### prompt
Watch closely: `in` checks the KEYS, and 4 is a price (a value), not a drink.

    print(4 in {"latte": 4, "mocha": 5})

### code
print(4 in {"latte": 4, "mocha": 5})

### choices
- False
- True
- latte
- 4

---

## p_add_key_show
kind: mcq
title: A new player joins
tags: dicts, predict
difficulty: medium
answer: 1

### prompt
What does this print?

    lives = {"ana": 1}
    lives["bo"] = 2
    print(lives)

### code
lives = {"ana": 1}
lives["bo"] = 2
print(lives)

### choices
- {'ana': 1, 'bo': 2}
- {'ana': 1}
- {'bo': 2}
- {'ana': 1, 'bo': 1}

---

## p_loop_over_keys
kind: mcq
title: Looping the scoreboard
tags: dicts, predict
difficulty: medium
answer: 1

### prompt
Looping a dict directly walks its KEYS. What does this print?

    for player in {"ana": 1, "bo": 2}:
        print(player)

### code
for player in {"ana": 1, "bo": 2}:
    print(player)

### choices
- ana\nbo
- 1\n2
- ana 1\nbo 2
- {'ana': 1, 'bo': 2}

---

## p_dup_key_wins
kind: mcq
title: The same key, written twice
tags: dicts, predict
difficulty: medium
answer: 1

### prompt
Watch closely: "potion" is written twice, so the LAST value wins.

    stock = {"potion": 5, "potion": 9}
    print(stock["potion"])

### code
stock = {"potion": 5, "potion": 9}
print(stock["potion"])

### choices
- 9
- 5
- 14
- potion

---

## p_items_print
kind: mcq
title: One line off the menu
tags: dicts, predict
difficulty: medium
answer: 1

### prompt
What does this print?

    for item, price in {"pizza": 8}.items():
        print(item, price)

### code
for item, price in {"pizza": 8}.items():
    print(item, price)

### choices
- pizza 8
- pizza
- 8
- ('pizza', 8)

---

## p_values_print
kind: mcq
title: Just the prices, please
tags: dicts, predict
difficulty: medium
answer: 1

### prompt
What does this print?

    for price in {"tea": 2, "cocoa": 4}.values():
        print(price)

### code
for price in {"tea": 2, "cocoa": 4}.values():
    print(price)

### choices
- 2\n4
- tea\ncocoa
- 2 4
- tea 2\ncocoa 4

---

## p_update_same_key
kind: mcq
title: Ana earns some XP
tags: dicts, predict
difficulty: medium
answer: 1

### prompt
What does this print?

    xp = {"ana": 4}
    xp["ana"] = xp["ana"] + 3
    print(xp["ana"])

### code
xp = {"ana": 4}
xp["ana"] = xp["ana"] + 3
print(xp["ana"])

### choices
- 7
- 4
- 3
- 43

---

## p_tally_build
kind: mcq
title: Tallying the votes
tags: dicts, predict
difficulty: hard
answer: 1

### prompt
Each character is a vote. The tally pattern counts them. What does this print?

    counts = {}
    for vote in "yynn":
        counts[vote] = counts.get(vote, 0) + 1
    print(counts)

### code
counts = {}
for vote in "yynn":
    counts[vote] = counts.get(vote, 0) + 1
print(counts)

### choices
- {'y': 2, 'n': 2}
- {'y': 1, 'n': 1}
- {'y': 4, 'n': 4}
- {'n': 2, 'y': 2}

---

## fix_color_lookup
kind: code_fn
title: Fix the loot counter
tags: dicts, bugs
difficulty: easy
entry: color_count

### prompt
The `bag` dict maps each gem color to how many of that color you've looted. This
function should return the count for a given `color`, or 0 if you have none of
that color. Right now it crashes when the color is missing. Fix it.

Examples

    color_count({"red": 2, "blue": 1}, "red") → 2
    color_count({"red": 2}, "blue") → 0
    color_count({}, "red") → 0

Notes

- Square brackets on a missing key raise a KeyError.
- There is a dict method that lets you name a fallback value.

### starter
```python
def color_count(bag, color):
    return bag[color]
```

### solution
```python
def color_count(bag, color):
    return bag.get(color, 0)
```

### check
color_count({"red": 2, "blue": 1}, "red") == 2
color_count({"red": 2}, "blue") == 0
color_count({}, "red") == 0
color_count({"red": 2, "blue": 1}, "blue") == 1
color_count({"green": 7}, "green") == 7

---

## fix_sum_prices
kind: code_fn
title: Fix the cart total
tags: dicts, bugs
difficulty: medium
entry: total

### prompt
The `prices` dict maps each item in your cart to its price. This function should
add up all the prices and return the total. It crashes instead. Fix it.

Examples

    total({"a": 2, "b": 3}) → 5
    total({"a": 10}) → 10
    total({}) → 0

Notes

- Looping over a dict directly gives you its KEYS, which here are strings.
- To loop over the numbers, you need `.values()`.

### starter
```python
def total(prices):
    s = 0
    for p in prices:
        s += p
    return s
```

### solution
```python
def total(prices):
    s = 0
    for p in prices.values():
        s += p
    return s
```

### check
total({"a": 2, "b": 3}) == 5
total({"a": 10}) == 10
total({}) == 0
total({"x": 1, "y": 1, "z": 1}) == 3
total({"pen": 5, "cup": 4}) == 9

---

## fix_seat_map
kind: code_fn
title: Fix the concert lineup
tags: dicts, bugs
difficulty: medium
entry: guests

### prompt
The `seats` dict maps each seat number to the guest sitting there. This function
should return the list of guest NAMES, in order. Instead it returns the seat
numbers. Fix it.

Examples

    guests({1: "ana", 2: "bo"}) → ["ana", "bo"]
    guests({5: "cy"}) → ["cy"]
    guests({}) → []

Notes

- `.keys()` gives the seat numbers; you want the names.
- The names are the dict's values.

### starter
```python
def guests(seats):
    return list(seats.keys())
```

### solution
```python
def guests(seats):
    return list(seats.values())
```

### check
guests({1: "ana", 2: "bo"}) == ["ana", "bo"]
guests({5: "cy"}) == ["cy"]
guests({}) == []
guests({1: "zed", 2: "amy", 3: "cy"}) == ["zed", "amy", "cy"]
guests({7: "solo"}) == ["solo"]

---

## wrong_keyerror_bracket
kind: mcq
title: What's wrong — juice isn't on the menu
tags: dicts, bugs
difficulty: easy
answer: 1

### prompt
This code crashes with a KeyError. What is wrong?

    prices = {"tea": 2, "coffee": 3}
    print(prices["juice"])

### choices
- "juice" is not a key in the dict, so prices["juice"] raises a KeyError
- A dict cannot be printed
- The dict should use square brackets instead of curly braces
- The prices need to be strings

---

## wrong_in_finds_value
kind: mcq
title: What's wrong — hunting for a score
tags: dicts, bugs
difficulty: medium
answer: 1

### prompt
The programmer expected this to print `found` because 90 is one of the scores,
but nothing prints. What is wrong?

    scores = {"ana": 90, "bo": 85}
    if 90 in scores:
        print("found")

### choices
- `in` checks the dict's keys, and 90 is a value, not a key
- You cannot use numbers with `in`
- The dict is empty
- `if` does not work with dicts

---

## wrong_equals_in_dict
kind: mcq
title: What's wrong — building a profile
tags: dicts, bugs
difficulty: easy
answer: 1

### prompt
This line causes a SyntaxError. What is wrong?

    person = {"name" = "Ana", "age" = 20}

### choices
- Dict pairs use a colon, like {"name": "Ana"}, not an equals sign
- The keys must be numbers
- A dict can only hold one pair
- The curly braces should be square brackets

---

## wrong_append_missing_list
kind: mcq
title: What's wrong — adding to team A
tags: dicts, bugs
difficulty: medium
answer: 1

### prompt
This code crashes with a KeyError on the second line. What is wrong?

    teams = {}
    teams["A"].append("Ana")

### choices
- The key "A" doesn't exist yet, so there is no list there to append to
- You cannot append to anything inside a dict
- The dict should be a list instead
- "Ana" must be a number

---

## concept_in_keys
kind: mcq
title: What does `in` check on a dict?
tags: dicts, concept
difficulty: easy
answer: 1

### prompt
When you write `key in my_dict`, what does Python check?

### choices
- Whether `key` matches one of the dict's keys
- Whether `key` matches one of the dict's values
- Whether `key` matches either a key or a value
- Whether the dict is empty

---

## concept_get_vs_bracket
kind: mcq
title: d[k] versus d.get(k)
tags: dicts, concept
difficulty: medium
answer: 1

### prompt
When `k` is NOT a key in the dict, how do `d[k]` and `d.get(k)` differ?

### choices
- `d[k]` raises a KeyError; `d.get(k)` returns None instead of crashing
- They behave exactly the same
- `d.get(k)` raises a KeyError; `d[k]` returns None
- Both return 0

---

## concept_key_repeat
kind: mcq
title: Can a key appear twice?
tags: dicts, concept
difficulty: medium
answer: 1

### prompt
A dict is written with the same key twice: `{"a": 1, "a": 2}`. What happens?

### choices
- The dict keeps one "a", and the last value written (2) wins
- Python raises an error for the repeated key
- The dict keeps both, so its length is 2
- The first value (1) wins

---

## concept_dict_changeable
kind: mcq
title: Can you change a dict?
tags: dicts, concept
difficulty: easy
answer: 1

### prompt
After you create a dict, what can you do to it?

### choices
- You can add new keys and change existing values at any time
- Nothing — a dict is frozen once it is created
- You can change values but can never add a new key
- You can add keys but can never change a value

---

## concept_which_is_dict
kind: mcq
title: Which one is a dict?
tags: dicts, concept
difficulty: easy
answer: 1

### prompt
Which of these is a dict?

### choices
- {"a": 1, "b": 2}
- ["a", "b"]
- ("a", "b")
- {"a", "b"}

---

## concept_len_counts_dict
kind: mcq
title: What does len(d) count?
tags: dicts, concept
difficulty: easy
answer: 1

### prompt
For a dict `d`, what does `len(d)` give you?

### choices
- The number of key-value pairs
- The total of all the values
- The number of keys plus the number of values
- The length of the longest key

---

## phone_lookup
kind: code_fn
title: Look up a contact
tags: dicts, functions
difficulty: easy
entry: lookup

### prompt
Create a function that takes a `book` dict mapping names to phone numbers, plus a
`name`. Return that person's number, or the string "unknown" if the name isn't in
your contacts.

Examples

    lookup({"ana": "123", "bo": "456"}, "ana") → "123"
    lookup({"ana": "123"}, "cy") → "unknown"
    lookup({}, "ana") → "unknown"

Notes

- `book[name]` crashes on a missing name. Use the safe lookup instead.
- The fallback value is the string "unknown".

### starter
```python
def lookup(book, name):
    
```

### solution
```python
def lookup(book, name):
    return book.get(name, "unknown")
```

### check
lookup({"ana": "123", "bo": "456"}, "ana") == "123"
lookup({"ana": "123"}, "cy") == "unknown"
lookup({}, "ana") == "unknown"
lookup({"ana": "123", "bo": "456"}, "bo") == "456"
lookup({"zed": "999"}, "zed") == "999"

---

## names_sorted
kind: code_fn
title: Leaderboard in alphabetical order
tags: dicts, functions
difficulty: easy
entry: names_sorted

### prompt
Create a function that takes a `scores` dict mapping players to scores, and returns
a list of just the player names, sorted alphabetically.

Examples

    names_sorted({"bo": 1, "ana": 2}) → ["ana", "bo"]
    names_sorted({}) → []
    names_sorted({"cy": 5}) → ["cy"]

Notes

- The keys of the dict are the names.
- `sorted(...)` returns a new list in order.

### starter
```python
def names_sorted(scores):
    
```

### solution
```python
def names_sorted(scores):
    return sorted(scores.keys())
```

### check
names_sorted({"bo": 1, "ana": 2}) == ["ana", "bo"]
names_sorted({}) == []
names_sorted({"cy": 5}) == ["cy"]
names_sorted({"zed": 1, "amy": 2, "bo": 3}) == ["amy", "bo", "zed"]
names_sorted({"m": 9, "a": 1}) == ["a", "m"]

---

## seat_taken
kind: code_fn
title: Is that seat taken?
tags: dicts, functions
difficulty: easy
entry: is_taken

### prompt
A `seats` dict maps each seat number to the guest sitting there. Create a function
that returns True if a given `seat` is taken — that is, if it's a key in the dict —
and False otherwise.

Examples

    is_taken({1: "ana", 2: "bo"}, 1) → True
    is_taken({1: "ana"}, 5) → False
    is_taken({}, 1) → False

Notes

- `seat in seats` checks the KEYS of the dict.
- A comparison is already True or False, so you can return it directly.

### starter
```python
def is_taken(seats, seat):
    
```

### solution
```python
def is_taken(seats, seat):
    return seat in seats
```

### check
is_taken({1: "ana", 2: "bo"}, 1) is True
is_taken({1: "ana"}, 5) is False
is_taken({}, 1) is False
is_taken({1: "ana", 2: "bo"}, 2) is True
is_taken({3: "cy"}, 3) is True
