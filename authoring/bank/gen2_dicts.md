# Dictionaries — more practice

Extra drills on dicts: building them, looking things up safely, the difference
between keys and values, and counting with the tally pattern.

---

## p_ages_lookup
kind: mcq
title: Predict — look up by key
tags: dicts, predict
see: 08_dicts#looking-up-a-value-with-dkey
difficulty: easy
answer: 1

### prompt
What does this print?

    ages = {"ana": 20, "bo": 22}
    print(ages["bo"])

### code
ages = {"ana": 20, "bo": 22}
print(ages["bo"])

### choices
- 22
- 20
- bo
- ana

---

## p_dict_len_three
kind: mcq
title: Predict — how many pairs
tags: dicts, predict
see: 08_dicts#len-how-many-pairs
difficulty: easy
answer: 1

### prompt
What does this print?

    inventory = {"pen": 5, "cup": 2, "hat": 9}
    print(len(inventory))

### code
inventory = {"pen": 5, "cup": 2, "hat": 9}
print(len(inventory))

### choices
- 3
- 16
- 6
- 9

---

## p_get_missing_zero
kind: mcq
title: Predict — .get() with a missing key
tags: dicts, predict
see: 08_dicts#get-a-safe-lookup-with-a-default
difficulty: easy
answer: 1

### prompt
What does this print?

    d = {"x": 5}
    print(d.get("y", 0))

### code
d = {"x": 5}
print(d.get("y", 0))

### choices
- 0
- 5
- None
- y

---

## p_get_present_value
kind: mcq
title: Predict — .get() when the key is there
tags: dicts, predict
see: 08_dicts#get-a-safe-lookup-with-a-default
difficulty: easy
answer: 1

### prompt
What does this print?

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
title: Predict — in finds a key
tags: dicts, predict
see: 08_dicts#in-tests-keys-not-values
difficulty: easy
answer: 1

### prompt
What does this print?

    print("apple" in {"apple": 3, "pear": 5})

### code
print("apple" in {"apple": 3, "pear": 5})

### choices
- True
- False
- 3
- apple

---

## p_in_value_false
kind: mcq
title: Predict — in does NOT find a value
tags: dicts, predict
see: 08_dicts#in-tests-keys-not-values
difficulty: medium
answer: 1

### prompt
What does this print?

    print(3 in {"apple": 3, "pear": 5})

### code
print(3 in {"apple": 3, "pear": 5})

### choices
- False
- True
- apple
- 3

---

## p_add_key_show
kind: mcq
title: Predict — add a key then print the dict
tags: dicts, predict
see: 08_dicts#adding-and-changing-keys
difficulty: medium
answer: 1

### prompt
What does this print?

    d = {"a": 1}
    d["b"] = 2
    print(d)

### code
d = {"a": 1}
d["b"] = 2
print(d)

### choices
- {'a': 1, 'b': 2}
- {'a': 1}
- {'b': 2}
- {'a': 1, 'b': 1}

---

## p_loop_over_keys
kind: mcq
title: Predict — looping over a dict
tags: dicts, predict
see: 08_dicts#looping-with-items
difficulty: medium
answer: 1

### prompt
What does this print?

    for k in {"x": 1, "y": 2}:
        print(k)

### code
for k in {"x": 1, "y": 2}:
    print(k)

### choices
- x\ny
- 1\n2
- x 1\ny 2
- {'x': 1, 'y': 2}

---

## p_dup_key_wins
kind: mcq
title: Predict — the same key written twice
tags: dicts, predict
see: 08_dicts#keys-must-be-unique
difficulty: medium
answer: 1

### prompt
What does this print?

    stock = {"pen": 5, "pen": 9}
    print(stock["pen"])

### code
stock = {"pen": 5, "pen": 9}
print(stock["pen"])

### choices
- 9
- 5
- 14
- pen

---

## p_items_print
kind: mcq
title: Predict — looping with .items()
tags: dicts, predict
see: 08_dicts#looping-with-items
difficulty: medium
answer: 1

### prompt
What does this print?

    for k, v in {"tea": 3}.items():
        print(k, v)

### code
for k, v in {"tea": 3}.items():
    print(k, v)

### choices
- tea 3
- tea
- 3
- ('tea', 3)

---

## p_values_print
kind: mcq
title: Predict — looping over .values()
tags: dicts, predict
see: 08_dicts#keys-values-items
difficulty: medium
answer: 1

### prompt
What does this print?

    for v in {"a": 1, "b": 2}.values():
        print(v)

### code
for v in {"a": 1, "b": 2}.values():
    print(v)

### choices
- 1\n2
- a\nb
- 1 2
- a 1\nb 2

---

## p_update_same_key
kind: mcq
title: Predict — update a value using itself
tags: dicts, predict
see: 08_dicts#adding-and-changing-keys
difficulty: medium
answer: 1

### prompt
What does this print?

    d = {"n": 4}
    d["n"] = d["n"] + 3
    print(d["n"])

### code
d = {"n": 4}
d["n"] = d["n"] + 3
print(d["n"])

### choices
- 7
- 4
- 3
- 43

---

## p_tally_build
kind: mcq
title: Predict — building a tally
tags: dicts, predict
see: 08_dicts#counting-with-a-dict-the-tally-pattern
difficulty: hard
answer: 1

### prompt
What does this print?

    counts = {}
    for c in "abba":
        counts[c] = counts.get(c, 0) + 1
    print(counts)

### code
counts = {}
for c in "abba":
    counts[c] = counts.get(c, 0) + 1
print(counts)

### choices
- {'a': 2, 'b': 2}
- {'a': 1, 'b': 1}
- {'a': 4, 'b': 4}
- {'b': 2, 'a': 2}

---

## fix_color_lookup
kind: code_fn
title: Fix the marble counter
tags: dicts, bugs
see: 08_dicts#get-a-safe-lookup-with-a-default
difficulty: easy
entry: color_count

### prompt
The `bag` dict maps each marble color to how many of that color are in the bag.
This function should return the count for a given `color`, or 0 if that color
isn't in the bag. Right now it crashes when the color is missing. Fix it.

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
title: Fix the price total
tags: dicts, bugs
see: 08_dicts#keys-values-items
difficulty: medium
entry: total

### prompt
The `prices` dict maps each item to its price. This function should add up all
the prices and return the total. It crashes instead. Fix it.

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

## fix_tally_init
kind: code_fn
title: Fix the word counter
tags: dicts, bugs
see: 08_dicts#counting-with-a-dict-the-tally-pattern
difficulty: medium
entry: word_count

### prompt
This function should count how many times each word appears in a list and return
a dict mapping each word to its count. It crashes on the very first word. Fix it.

Examples

    word_count(["a", "b", "a"]) → {"a": 2, "b": 1}
    word_count([]) → {}
    word_count(["hi", "hi", "hi"]) → {"hi": 3}

Notes

- The first time you see a word, `counts[w]` doesn't exist yet, so reading it
  raises a KeyError.
- `counts.get(w, 0)` gives you 0 for a word you haven't seen before.

### starter
```python
def word_count(words):
    counts = {}
    for w in words:
        counts[w] = counts[w] + 1
    return counts
```

### solution
```python
def word_count(words):
    counts = {}
    for w in words:
        counts[w] = counts.get(w, 0) + 1
    return counts
```

### check
word_count(["a", "b", "a"]) == {"a": 2, "b": 1}
word_count([]) == {}
word_count(["x"]) == {"x": 1}
word_count(["hi", "hi", "hi"]) == {"hi": 3}
word_count(["a", "b", "c"]) == {"a": 1, "b": 1, "c": 1}

---

## fix_seat_map
kind: code_fn
title: Fix the guest list
tags: dicts, bugs
see: 08_dicts#keys-values-items
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
title: What's wrong — missing key
tags: dicts, bugs
see: 08_dicts#keyerror-asking-for-a-key-that-isnt-there
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
title: What's wrong — in checks the wrong side
tags: dicts, bugs
see: 08_dicts#in-tests-keys-not-values
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
title: What's wrong — equals inside a dict
tags: dicts, bugs
see: 08_dicts#making-a-dict
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
title: What's wrong — appending to a missing key
tags: dicts, bugs
see: 08_dicts#keyerror-asking-for-a-key-that-isnt-there
difficulty: medium
answer: 1

### prompt
This code crashes with a KeyError on the second line. What is wrong?

    groups = {}
    groups["A"].append("Ana")

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
see: 08_dicts#in-tests-keys-not-values
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
see: 08_dicts#get-a-safe-lookup-with-a-default
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
see: 08_dicts#keys-must-be-unique
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
see: 08_dicts#adding-and-changing-keys
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
see: 08_dicts#making-a-dict
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
see: 08_dicts#len-how-many-pairs
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

## make_capitals
kind: code_var
title: Build a capitals lookup
tags: dicts
see: 08_dicts#making-a-dict
difficulty: easy
entry: capitals

### prompt
Store, in a variable named `capitals`, a dict that maps each country to its
capital city:

- "France" → "Paris"
- "Japan" → "Tokyo"
- "Egypt" → "Cairo"

Notes

- A dict pair is written `key: value`, with a colon.
- Separate the pairs with commas, all inside curly braces.

### starter
```python
capitals =
```

### solution
```python
capitals = {"France": "Paris", "Japan": "Tokyo", "Egypt": "Cairo"}
```

### check
capitals == {"France": "Paris", "Japan": "Tokyo", "Egypt": "Cairo"}

---

## phone_lookup
kind: code_fn
title: Look up a phone number
tags: dicts, functions
see: 08_dicts#get-a-safe-lookup-with-a-default
difficulty: easy
entry: lookup

### prompt
Create a function that takes a `book` dict mapping names to phone numbers, plus a
`name`. Return that person's number, or the string "unknown" if the name isn't in
the book.

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

## count_letters
kind: code_fn
title: Count each letter
tags: dicts, strings
see: 08_dicts#counting-with-a-dict-the-tally-pattern
difficulty: medium
entry: count_letters

### prompt
Create a function that takes a string and returns a dict mapping each letter to
how many times it appears.

Examples

    count_letters("aba") → {"a": 2, "b": 1}
    count_letters("") → {}
    count_letters("x") → {"x": 1}

Notes

- Start with an empty dict and loop over the characters.
- `counts[c] = counts.get(c, 0) + 1` adds one, even the first time you see `c`.

### starter
```python
def count_letters(text):
    counts = {}
    
```

### solution
```python
def count_letters(text):
    counts = {}
    for c in text:
        counts[c] = counts.get(c, 0) + 1
    return counts
```

### check
count_letters("aba") == {"a": 2, "b": 1}
count_letters("") == {}
count_letters("x") == {"x": 1}
count_letters("mississippi") == {"m": 1, "i": 4, "s": 4, "p": 2}
count_letters("aaa") == {"a": 3}

---

## add_item
kind: code_fn
title: Add an item to the cart
tags: dicts, functions
see: 08_dicts#adding-and-changing-keys
difficulty: easy
entry: add_item

### prompt
Create a function that takes a `cart` dict mapping item names to quantities, plus
an `item` and a `qty`. Set that item's quantity to `qty` (adding the key if it's
new, replacing it if it already exists) and return the updated dict.

Examples

    add_item({}, "pen", 3) → {"pen": 3}
    add_item({"pen": 3}, "cup", 2) → {"pen": 3, "cup": 2}
    add_item({"pen": 3}, "pen", 5) → {"pen": 5}

Notes

- `cart[item] = qty` both adds a new key and overwrites an existing one.
- Don't forget to return the dict.

### starter
```python
def add_item(cart, item, qty):
    
```

### solution
```python
def add_item(cart, item, qty):
    cart[item] = qty
    return cart
```

### check
add_item({}, "pen", 3) == {"pen": 3}
add_item({"pen": 3}, "cup", 2) == {"pen": 3, "cup": 2}
add_item({"pen": 3}, "pen", 5) == {"pen": 5}
add_item({"a": 1, "b": 2}, "c", 9) == {"a": 1, "b": 2, "c": 9}
add_item({}, "x", 0) == {"x": 0}

---

## names_sorted
kind: code_fn
title: List the names in order
tags: dicts, functions
see: 08_dicts#keys-values-items
difficulty: easy
entry: names_sorted

### prompt
Create a function that takes a `scores` dict mapping names to scores, and returns
a list of just the names, sorted alphabetically.

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
see: 08_dicts#in-tests-keys-not-values
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
