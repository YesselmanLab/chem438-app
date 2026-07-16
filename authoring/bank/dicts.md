# Dictionaries

Storing things by name instead of by position: building dicts, looking things up
safely with `.get()`, and looping over keys and values with `.items()`.

---

## vending_slots_dict
kind: mcq
title: Stock the vending machine
tags: dicts, language_fundamentals, types
difficulty: easy
answer: 3

### prompt
A vending machine has three slots. Slot "A1" holds chips, slot "A2" holds gum, and
slot "B1" holds candy. You want a dict named `slots` that maps each slot code to
the snack in it, so that this prints `gum`:

    print(slots["A2"])

Which line creates `slots` correctly?

### choices
- slots = {"chips": "A1", "gum": "A2", "candy": "B1"}
- slots = {"A1" = "chips", "A2" = "gum", "B1" = "candy"}
- slots = {"A1": "chips", "A2": "gum", "B1": "candy"}
- slots = {"A1", "chips", "A2", "gum", "B1", "candy"}

---

## menu_price_lookup
kind: code_fn
title: What does it cost?
tags: dicts, functions, validation
difficulty: easy
entry: price

### prompt
Create a function that takes a `menu` dict mapping item names to prices, plus an
`item` name. Return that item's price, or 0 if the item is not on the menu.

Examples

    price({"tea": 2, "coffee": 3}, "tea") → 2
    price({"tea": 2, "coffee": 3}, "juice") → 0
    price({}, "tea") → 0

Notes

- Reaching for a missing key with `menu[item]` crashes. There is a dict method
  that lets you name a fallback value instead.
- Don't forget to return the result.

### walkthrough
The instinct here is to write `menu[item]`, and for "tea" it works fine. Then the
customer asks for juice, `menu["juice"]` finds nothing, and Python raises a
KeyError — your program stops dead. Square brackets on a dict mean "this key had
better be there."

The fix is `.get()`, which takes the key and a fallback:

    def price(menu, item):
        return menu.get(item, 0)

`menu.get("tea", 0)` finds "tea" and hands back 2. `menu.get("juice", 0)` looks,
finds nothing, and calmly hands back 0 instead of crashing.

Watch that second argument. If you write `menu.get(item)` with no fallback, a
missing item gives you `None`, not 0 — and `None` is not a number, so the first
piece of code that tries to add it to a total will break in a confusing place far
away from the real mistake. Say what you want the default to be.

### starter
```python
def price(menu, item):
    
```

### solution
```python
def price(menu, item):
    return menu.get(item, 0)
```

### check
price({"tea": 2, "coffee": 3}, "tea") == 2
price({"tea": 2, "coffee": 3}, "coffee") == 3
price({"tea": 2, "coffee": 3}, "juice") == 0
price({}, "tea") == 0
price({"bagel": 1.5}, "bagel") == 1.5

---

## username_available
kind: code_fn
title: Is that username taken?
tags: dicts, logic, validation
difficulty: easy
entry: is_available

### prompt
A website stores its members in a `users` dict, where each key is a username.
Create a function that returns True if `name` is still available — that is, if it
is NOT already a key in `users` — and False otherwise.

Examples

    is_available({"ana": 1, "bo": 2}, "cy") → True
    is_available({"ana": 1, "bo": 2}, "ana") → False
    is_available({}, "ana") → True

Notes

- `key in some_dict` checks the dict's KEYS, never its values.
- A comparison is already True or False, so you can return it directly — no
  if/else needed.

### starter
```python
def is_available(users, name):
    
```

### solution
```python
def is_available(users, name):
    return name not in users
```

### check
is_available({"ana": 1, "bo": 2}, "cy") is True
is_available({"ana": 1, "bo": 2}, "ana") is False
is_available({}, "ana") is True
is_available({"ana": 1}, "ana") is False
is_available({"ana": "bo"}, "bo") is True
is_available({"ana": 1, "bo": 2}, "Ana") is True

---

## mcq_dup_dict_key
kind: mcq
title: Two prices for tea
tags: dicts, predict, concept
difficulty: medium
answer: 2

### prompt
Read this code carefully. The key "tea" is written twice.

    prices = {"tea": 2, "coffee": 3, "tea": 4}
    print(len(prices), prices["tea"])

What does it print?

### choices
- 3 4
- 2 4
- 2 2
- Nothing — Python raises an error for the repeated key

### walkthrough
A dict key is unique. Python builds this dict one pair at a time, left to right,
and each pair is really an assignment into the dict.

So it sets "tea" to 2, sets "coffee" to 3, and then reaches `"tea": 4` — a key it
already has. It does not complain and it does not keep both. It just overwrites,
exactly like `x = 2` followed by `x = 4`. The last write wins.

That leaves two keys, "tea" and "coffee", so `len(prices)` is 2, and "tea" now
holds 4. The output is `2 4`.

The trap is expecting an error. A repeated key is silent — which is what makes it
worth knowing. When a dict you built in a loop comes out shorter than the list you
built it from, this is almost always why: two entries shared a key, and the second
one quietly erased the first.

---

## tally_dice_rolls
kind: code_fn
title: Tally the dice
tags: dicts, loops, arrays
difficulty: medium
entry: tally

### prompt
Create a function that takes a list of dice rolls and reports how many times each
number appeared. Return a list of `[face, count]` pairs, sorted from the smallest
face to the largest.

Examples

    tally([1, 2, 2, 5]) → [[1, 1], [2, 2], [5, 1]]
    tally([6, 6, 6]) → [[6, 3]]
    tally([]) → []

Notes

- Count into a dict first: `counts[r] = counts.get(r, 0) + 1`.
- `sorted(counts)` gives you the keys in order.
- A face that was never rolled should not appear at all.

### starter
```python
def tally(rolls):
    counts = {}
    
```

### solution
```python
def tally(rolls):
    counts = {}
    for r in rolls:
        counts[r] = counts.get(r, 0) + 1
    return [[face, counts[face]] for face in sorted(counts)]
```

### check
tally([1, 2, 2, 5]) == [[1, 1], [2, 2], [5, 1]]
tally([6, 6, 6]) == [[6, 3]]
tally([]) == []
tally([3]) == [[3, 1]]
tally([4, 1, 4, 1, 4]) == [[1, 2], [4, 3]]

---

## fix_high_scores_loop
kind: code_fn
title: Fix the high score list
tags: dicts, bugs, loops
difficulty: medium
entry: high_scores

### prompt
The `scores` dict maps each player's name to their score. This function should
return a list of the names who scored above 90, in the order they appear in the
dict. It crashes instead. Fix it.

Examples

    high_scores({"ana": 95, "bo": 88}) → ["ana"]
    high_scores({"ana": 95, "bo": 91}) → ["ana", "bo"]
    high_scores({"ana": 90}) → []

Notes

- Looping over a dict directly gives you its keys and nothing else.
- "Above 90" does not include 90 itself.

### walkthrough
Run the starter and Python says something like "too many values to unpack". That
message is the whole clue.

`for name, score in scores:` asks Python for two things per step. But looping over
a dict hands you one thing per step — a key. So Python takes the key "ana", a
three-letter string, and tries to split it into `name` and `score`. Three letters,
two variables, and it gives up.

If you want the key and the value together, you have to ask for both:

    for name, score in scores.items():

Now each step hands over a `("ana", 95)` pair, which splits into two variables
neatly.

The three ways to loop a dict are worth memorizing as a set: `scores` gives keys,
`scores.values()` gives values, `scores.items()` gives both. A useful sanity check
before you run anything: count the variables to the left of `in`, and make sure
the thing on the right actually produces that many per step.

### starter
```python
def high_scores(scores):
    winners = []
    for name, score in scores:
        if score > 90:
            winners.append(name)
    return winners
```

### solution
```python
def high_scores(scores):
    winners = []
    for name, score in scores.items():
        if score > 90:
            winners.append(name)
    return winners
```

### check
high_scores({"ana": 95, "bo": 88}) == ["ana"]
high_scores({"ana": 95, "bo": 91}) == ["ana", "bo"]
high_scores({"ana": 90}) == []
high_scores({}) == []
high_scores({"cy": 100, "di": 12, "ed": 91}) == ["cy", "ed"]

---

## expand_textspeak
kind: code_fn
title: Expand the text-speak
tags: dicts, strings, loops
difficulty: medium
entry: expand

### prompt
Create a function that takes a list of `words` and a `codes` dict mapping
abbreviations to their full meaning. Replace every word that appears in `codes`
with its expansion, leave every other word alone, and return the result as one
space-separated string.

Examples

    expand(["brb", "now"], {"brb": "be right back"}) → "be right back now"
    expand(["hello"], {}) → "hello"
    expand(["omw", "omw"], {"omw": "on my way"}) → "on my way on my way"

Notes

- The default for a word you cannot expand is the word itself.
- `" ".join(list_of_strings)` glues a list into one string.

### starter
```python
def expand(words, codes):
    
```

### solution
```python
def expand(words, codes):
    out = []
    for w in words:
        out.append(codes.get(w, w))
    return " ".join(out)
```

### check
expand(["brb", "now"], {"brb": "be right back"}) == "be right back now"
expand(["idk", "lol"], {"idk": "I do not know", "lol": "laughing out loud"}) == "I do not know laughing out loud"
expand(["hello"], {}) == "hello"
expand([], {"brb": "be right back"}) == ""
expand(["omw", "omw"], {"omw": "on my way"}) == "on my way on my way"

---

## vote_winner
kind: code_fn
title: Who won the vote?
tags: dicts, loops, algorithms
difficulty: hard
entry: winner

### prompt
Create a function that takes a `votes` dict mapping each candidate's name to their
number of votes. Return a `[name, margin]` pair for the candidate with the most
votes, where `margin` is how many votes they beat second place by. If the dict is
empty, return None.

Examples

    winner({"ana": 5, "bo": 3}) → ["ana", 2]
    winner({"ana": 1, "bo": 4, "cy": 2}) → ["bo", 2]
    winner({}) → None

Notes

- With only one candidate, treat second place as having 0 votes, so the margin is
  just the winner's own count.
- Assume there is never a tie for first place.
- A candidate can have 0 votes and still win, if they are the only candidate.

### walkthrough
First, an honest word about `max`. If all you needed was the winner's name,
`max(votes, key=votes.get)` would do the whole job in one line, and you should know
that. But you were also asked for the margin over second place, and one call to
`max` cannot hand you two different candidates' counts. So you have to walk the dict
yourself — which is worth doing, because "remember the best so far" is the pattern
every rule more complicated than "biggest" is built on.

Keep three variables and update them as you go:

    def winner(votes):
        best_name = None
        best_count = 0
        second_count = 0
        for name, count in votes.items():
            if best_name is None or count > best_count:
                second_count = best_count
                best_name = name
                best_count = count
            elif count > second_count:
                second_count = count
        if best_name is None:
            return None
        return [best_name, best_count - second_count]

The line to stare at is `second_count = best_count` inside the `if`. When someone
new takes first place, the old leader does not vanish — they are now second. Forget
that line and you compare everyone against a stale second place, so the margin comes
out too big in a way that still looks plausible.

The `elif` matters just as much. A candidate who loses to the leader might still be
the best of the losers, so they get their own chance to claim second. If you write a
plain `if` there instead of `elif`, the brand-new leader immediately gets compared
against themselves and becomes their own runner-up, and every margin collapses to 0.

Finally, notice `best_name is None or count > best_count` rather than just
`count > best_count`. Starting `best_count` at 0 quietly assumes nobody has 0 votes.
If the only candidate has 0, `0 > 0` is False, nobody is ever recorded, and you
return None for a dict that had a perfectly good winner in it. The `best_name is
None` half forces the first candidate to be accepted no matter what — and it hands
you the empty-dict answer for free, since the loop never runs and `best_name` is
still None.

### starter
```python
def winner(votes):
    best_name = None
    best_count = 0
    second_count = 0
    
```

### solution
```python
def winner(votes):
    best_name = None
    best_count = 0
    second_count = 0
    for name, count in votes.items():
        if best_name is None or count > best_count:
            second_count = best_count
            best_name = name
            best_count = count
        elif count > second_count:
            second_count = count
    if best_name is None:
        return None
    return [best_name, best_count - second_count]
```

### check
winner({"ana": 5, "bo": 3}) == ["ana", 2]
winner({"ana": 1, "bo": 4, "cy": 2}) == ["bo", 2]
winner({"solo": 0}) == ["solo", 0]
winner({"solo": 6}) == ["solo", 6]
winner({}) is None
winner({"ana": 2, "bo": 2, "cy": 7}) == ["cy", 5]
winner({"bo": 3, "ana": 5}) == ["ana", 2]

---

## seat_by_initial
kind: code_fn
title: Group the guests by initial
tags: dicts, strings, algorithms
difficulty: hard
entry: group_by_initial

### prompt
Create a function that groups guest names by their first letter and writes one
seating line per letter, in the form `"A: Ana, Amy"`. Return the list of those
lines. Both the letters and the names inside each line stay in the order they first
appear in the input.

Examples

    group_by_initial(["Ana", "Bo", "Amy"]) → ["A: Ana, Amy", "B: Bo"]
    group_by_initial(["Zed"]) → ["Z: Zed"]
    group_by_initial([]) → []

Notes

- `name[0]` is a name's first letter.
- Build a dict whose values are lists of names, then turn it into lines at the end.
- `", ".join(some_names)` glues names into one string with commas between them.
- Capital "A" and lowercase "a" are different letters.

### walkthrough
This one has a real trap in it. The obvious first attempt is:

    groups[n[0]].append(n)

and it crashes on the very first name with a KeyError. Of course it does — the key
"A" does not exist yet, so there is no list there to append to. You cannot add to a
list you have not created.

That diagnosis tells you the fix directly: if the list is missing, make it, then
append. Two lines, in that order.

    def group_by_initial(names):
        groups = {}
        for n in names:
            if n[0] not in groups:
                groups[n[0]] = []
            groups[n[0]].append(n)
        return [letter + ": " + ", ".join(groups[letter]) for letter in groups]

The `if` runs only the first time each letter shows up, so by the time you reach the
`.append`, the list is guaranteed to exist. First "A" creates `[]` and appends to get
`["Ana"]`; later "Amy" skips the `if` entirely and appends onto what is already
there.

A compact alternative you will see in other people's code is
`groups[n[0]] = groups.get(n[0], []) + [n]`, which creates-or-fetches and adds in one
line. It reads nicely, but it builds a brand-new list for every single name, so
prefer the two-liner above until you have a reason not to.

The last line does the reporting. `", ".join(groups[letter])` turns `["Ana", "Amy"]`
into `"Ana, Amy"`, and gluing the letter and `": "` on the front finishes the line.
Note that `join` only works on a list of strings — that is fine here, but the moment
your values are numbers it will refuse.

The ordering asked for is free, not something you have to arrange: dicts remember
the order their keys were first inserted, so looping `for letter in groups` at the
end replays the letters in the order the guests introduced them.

### starter
```python
def group_by_initial(names):
    groups = {}
    
```

### solution
```python
def group_by_initial(names):
    groups = {}
    for n in names:
        if n[0] not in groups:
            groups[n[0]] = []
        groups[n[0]].append(n)
    return [letter + ": " + ", ".join(groups[letter]) for letter in groups]
```

### check
group_by_initial(["Ana", "Bo", "Amy"]) == ["A: Ana, Amy", "B: Bo"]
group_by_initial(["Zed"]) == ["Z: Zed"]
group_by_initial([]) == []
group_by_initial(["Bo", "Ana", "Ben", "Cy"]) == ["B: Bo, Ben", "A: Ana", "C: Cy"]
group_by_initial(["ana", "Ana"]) == ["a: ana", "A: Ana"]
