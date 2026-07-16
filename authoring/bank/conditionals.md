# Conditionals

Choosing between paths: if/elif/else, the ternary expression, and the order your tests run in.

---

## free_shipping_cost
kind: code_fn
title: Free shipping at fifty
tags: conditions, logic, numbers
difficulty: easy
entry: free_shipping_cost

### prompt
An online store ships free once your cart reaches $50. Given the cart total,
return the shipping cost: `0.0` when the total is 50 or more, otherwise `5.99`.
Fill in the three blanks so the whole thing is a single ternary (conditional)
expression.

Examples

    free_shipping_cost(80) → 0.0
    free_shipping_cost(12.5) → 5.99
    free_shipping_cost(50) → 0.0

Notes

- A ternary reads left to right: `value_if_true if condition else value_if_false`.
- "50 or more" includes exactly 50 — pick your comparison carefully.

### walkthrough
A ternary is one expression that produces one of two values. The shape is:

    result = a if condition else b

The tempting mistake is to read it like an English sentence starting with "if",
so people write `if total >= 50 then 0.0` — that is not Python. The *value comes
first*, then the condition, then the alternative:

    def free_shipping_cost(total):
        return 0.0 if total >= 50 else 5.99

The second trap is the boundary. "Free once you reach $50" means a $50 cart ships
free, so the test is `>= 50`, not `> 50`. Off-by-one at a boundary is the single
most common bug in conditional code, and it hides well: every check except the
exact-50 one still passes. Always test the boundary itself.

### starter
```python
def free_shipping_cost(total):
    return ___ if ___ else ___
```

### solution
```python
def free_shipping_cost(total):
    return 0.0 if total >= 50 else 5.99
```

### check
free_shipping_cost(80) == 0.0
free_shipping_cost(12.5) == 5.99
free_shipping_cost(50) == 0.0
free_shipping_cost(49.99) == 5.99
free_shipping_cost(0) == 5.99

---

## nickname_or_name
kind: code_fn
title: Shorten the long names
tags: strings, conditions, indexing
difficulty: easy
entry: nickname_or_name

### prompt
A name tag only has room for short names. Given a name, return the first 3
letters followed by a period if the name is longer than 6 characters. Otherwise
return the name unchanged.

Examples

    nickname_or_name("Alexander") → "Ale."
    nickname_or_name("Sam") → "Sam"
    nickname_or_name("Jasmine") → "Jas."

Notes

- `name[:3]` gives you the first three characters of a string.
- "Longer than 6" means a 6-character name is left alone.

### starter
```python
def nickname_or_name(name):
    
```

### solution
```python
def nickname_or_name(name):
    if len(name) > 6:
        return name[:3] + '.'
    return name
```

### check
nickname_or_name("Alexander") == "Ale."
nickname_or_name("Sam") == "Sam"
nickname_or_name("Jasmine") == "Jas."
nickname_or_name("Robert") == "Robert"
nickname_or_name("") == ""

---

## weekend_or_not
kind: code_fn
title: Is it the weekend?
tags: bugs, conditions, logic
difficulty: easy
entry: weekend_or_not

### prompt
This function should return True for `"Saturday"` and `"Sunday"` and False for
every other day. Instead it says every day is the weekend. Find the bug and fix it.

Examples

    weekend_or_not("Saturday") → True
    weekend_or_not("Monday") → False
    weekend_or_not("Sunday") → True

Notes

- `or` joins two complete conditions — it does not distribute across a comparison.
- Ask yourself what `'Sunday'` on its own is worth to Python.

### walkthrough
Read the broken line the way Python reads it, not the way English reads it:

    if day == 'Saturday' or 'Sunday':

English hears "if day equals Saturday or Sunday". Python sees two separate
operands joined by `or`. The left one is `day == 'Saturday'` (fine). The right
one is just the string `'Sunday'` — a bare, non-empty string, which Python
considers truthy. So the whole condition becomes `something or True`, which is
always True, no matter what `day` is. That is why Monday is a weekend.

The fix is to make each side of `or` a full comparison:

    def weekend_or_not(day):
        return day == 'Saturday' or day == 'Sunday'

Repeat the `day ==` part. It feels wordy, and that wordiness is exactly what
tempts beginners into the bug. (Once you're comfortable, `day in ('Saturday',
'Sunday')` says the same thing more compactly.)

### starter
```python
def weekend_or_not(day):
    if day == 'Saturday' or 'Sunday':
        return True
    return False
```

### solution
```python
def weekend_or_not(day):
    return day == 'Saturday' or day == 'Sunday'
```

### check
weekend_or_not("Saturday") is True
weekend_or_not("Sunday") is True
weekend_or_not("Monday") is False
weekend_or_not("Friday") is False
weekend_or_not("") is False

---

## elevator_direction
kind: code_fn
title: Which way does the elevator go?
tags: conditions, logic, numbers
difficulty: easy
entry: elevator_direction

### prompt
An elevator is sitting on some floor when a passenger requests another floor.
Given the current floor and the requested floor, return `'up'`, `'down'`, or
`'stay'`.

Examples

    elevator_direction(2, 7) → "up"
    elevator_direction(9, 3) → "down"
    elevator_direction(4, 4) → "stay"

Notes

- Three outcomes means three branches: `if` / `elif` / `else`.
- Floors can be negative (a basement is fine).

### starter
```python
def elevator_direction(current, target):
    
```

### solution
```python
def elevator_direction(current, target):
    if target > current:
        return 'up'
    elif target < current:
        return 'down'
    else:
        return 'stay'
```

### check
elevator_direction(2, 7) == "up"
elevator_direction(9, 3) == "down"
elevator_direction(4, 4) == "stay"
elevator_direction(-2, 1) == "up"
elevator_direction(0, -3) == "down"

---

## grade_letter_order
kind: code_fn
title: Everyone got a D
tags: bugs, conditions, logic
difficulty: medium
entry: grade_letter_order

### prompt
This function should turn a score into a letter grade: 90 and up is `'A'`, 80 and
up `'B'`, 70 and up `'C'`, 60 and up `'D'`, and anything lower `'F'`. But a 95
comes back as `'D'`. Every comparison in it is correct on its own — the bug is in
the order they run in.

Examples

    grade_letter_order(95) → "A"
    grade_letter_order(72) → "C"
    grade_letter_order(41) → "F"

Notes

- An `if`/`elif` chain stops at the *first* test that is true.
- Nothing is wrong with any single comparison. Look at their order.

### walkthrough
Every comparison in the broken version is correct. A 95 really is `>= 60`. That
is the whole problem.

An `if`/`elif` chain is not "find the best match" — it is "take the first door
that opens, and never look at the rest". With `score >= 60` written first, a 95
opens that door immediately, returns `'D'`, and the `>= 70`, `>= 80`, and `>= 90`
tests below it never run at all. In fact *every* passing score returns `'D'`.

The fix is to order the branches from strictest to loosest, so the first door
that opens is the right one:

    def grade_letter_order(score):
        if score >= 90:
            return 'A'
        elif score >= 80:
            return 'B'
        elif score >= 70:
            return 'C'
        elif score >= 60:
            return 'D'
        else:
            return 'F'

Now a 95 stops at the first test. An 85 fails `>= 90`, then stops at `>= 80` —
and because it got past the first test, you already know it's below 90. That is
why you never need `if 80 <= score < 90`: the ordering carries the upper bound
for you. Whenever branches overlap, ask which one you want checked first.

### starter
```python
def grade_letter_order(score):
    if score >= 60:
        return 'D'
    elif score >= 70:
        return 'C'
    elif score >= 80:
        return 'B'
    elif score >= 90:
        return 'A'
    else:
        return 'F'
```

### solution
```python
def grade_letter_order(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'
```

### check
grade_letter_order(95) == "A"
grade_letter_order(83) == "B"
grade_letter_order(72) == "C"
grade_letter_order(60) == "D"
grade_letter_order(41) == "F"
grade_letter_order(0) == "F"

---

## first_over_budget
kind: code_fn
title: First price over the limit
tags: loops, conditions, arrays
difficulty: medium
entry: first_over_budget

### prompt
You are scanning a receipt for the first thing that blew the budget. Given a list
of prices and a limit, return the first price that is greater than the limit. If
every price is within budget, return `None`.

Examples

    first_over_budget([3, 8, 25, 4], 10) → 25
    first_over_budget([1, 2, 3], 10) → None
    first_over_budget([12, 40], 10) → 12

Notes

- Return as soon as you find it — don't keep looping.
- The fallback `return None` goes *after* the loop, not inside it.

### walkthrough
The pattern here is "search and stop early":

    def first_over_budget(prices, limit):
        for p in prices:
            if p > limit:
                return p
        return None

`return` inside a loop doesn't just end the loop — it ends the whole function on
the spot. So the first price over the limit is returned and nothing after it is
even looked at. That's exactly what "first" means.

The mistake to name: putting `return None` inside the loop, like this —

    for p in prices:
        if p > limit:
            return p
        return None          # WRONG — runs on the very first item

Indented like that, the `return None` belongs to the loop body, so the function
quits after examining item zero and can never find anything later in the list.
The fallback must sit at the *function's* indent level, so it only runs when the
loop finished without ever returning. The empty list falls out for free: the loop
body never runs, and you land on `return None`.

### starter
```python
def first_over_budget(prices, limit):
    
```

### solution
```python
def first_over_budget(prices, limit):
    for p in prices:
        if p > limit:
            return p
    return None
```

### check
first_over_budget([3, 8, 25, 4], 10) == 25
first_over_budget([12, 40], 10) == 12
first_over_budget([1, 2, 3], 10) is None
first_over_budget([], 10) is None
first_over_budget([10, 11], 10) == 11

---

## censor_words
kind: code_fn
title: Bleep the banned words
tags: strings, arrays, conditions, loops
difficulty: medium
entry: censor_words

### prompt
Given a list of words and a list of banned words, return a new list where every
banned word is replaced by `'***'` and every other word is kept as it is.

Examples

    censor_words(["you", "are", "silly"], ["silly"]) → ["you", "are", "***"]
    censor_words(["hi", "there"], []) → ["hi", "there"]
    censor_words(["bad", "bad"], ["bad"]) → ["***", "***"]

Notes

- The list you return must not shrink — same length, same order.
- `w in banned` asks whether a word appears in the banned list.
- Build a fresh list and append to it. Leave `words` itself alone.

### walkthrough
Start an empty list, walk the words, and append exactly one thing per word:

    def censor_words(words, banned):
        out = []
        for w in words:
            if w in banned:
                out.append('***')
            else:
                out.append(w)
        return out

The mistake to name is the missing `else`. It is tempting to write only the half
you care about:

    for w in words:
        if w in banned:
            out.append('***')     # and then... nothing

Now clean words are silently dropped and the list comes back short —
`["you", "are", "silly"]` returns `["***"]` instead of three items. Every word
must put *something* into `out`: either the bleep or the original word. One word
in, one word out.

The other trap is editing `words` in place instead of building `out`. The prompt
asks for a *new* list, and a caller who handed you their list rarely expects it
to come back censored. Appending to a fresh `out` keeps the original intact.

(Once loops and comprehensions feel comfortable, this same logic fits on one
line: `['***' if w in banned else w for w in words]`. Write the explicit version
first — it is the one you can debug.)

### starter
```python
def censor_words(words, banned):
    
```

### solution
```python
def censor_words(words, banned):
    out = []
    for w in words:
        if w in banned:
            out.append('***')
        else:
            out.append(w)
    return out
```

### check
censor_words(["you", "are", "silly"], ["silly"]) == ["you", "are", "***"]
censor_words(["hi", "there"], []) == ["hi", "there"]
censor_words(["bad", "bad"], ["bad"]) == ["***", "***"]
censor_words([], ["bad"]) == []
censor_words(["a", "b", "c"], ["a", "c"]) == ["***", "b", "***"]

---

## mcq_elif_stops
kind: mcq
title: Predict — if/elif with n = 12
tags: conditions, predict, concept
difficulty: medium
answer: 1

### prompt
What does this code print?

    n = 12
    if n % 2 == 0:
        print('even')
    elif n % 3 == 0:
        print('by three')
    else:
        print('neither')

### choices
- even
- even, then by three
- by three
- neither

---

