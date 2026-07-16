# Booleans & comparisons

Problems about True/False: comparing values, combining conditions with `and`/`or`/`not`,
and returning the answer directly instead of dressing it up in an if/else.

---

## keep_playing_flag
kind: code_fn
title: Flip the game-over flag
tags: logic, language_fundamentals, functions
difficulty: starter
entry: keep_playing

### prompt
A game keeps a flag telling it whether play has ended. Write `keep_playing(game_over)`
that returns the opposite of `game_over`.

Examples

    keep_playing(False) → True
    keep_playing(True) → False

Notes

- `not` flips a boolean: `not True` is `False`, and `not False` is `True`.
- The flipped value is already True or False — you can `return` it directly.

### starter
```python
def keep_playing(game_over):
    
```

### solution
```python
def keep_playing(game_over):
    return not game_over
```

### check
keep_playing(True) is False
keep_playing(False) is True

---

## free_shipping
kind: code_fn
title: Do they get free shipping?
tags: logic, validation, functions
difficulty: starter
entry: free_shipping

### prompt
A store gives free shipping once your cart total reaches 35 dollars. Write
`free_shipping(cart_total)` that returns True when the total is 35 or more, and
False otherwise.

Examples

    free_shipping(40) → True
    free_shipping(35) → True
    free_shipping(12) → False

Notes

- A cart of exactly 35 dollars qualifies.
- A comparison is already True or False — you can `return` it directly.

### walkthrough
The trap here is writing four lines where one will do:

    if cart_total >= 35:
        return True
    else:
        return False

That works, but look closely at what it does. Python evaluates `cart_total >= 35`
and gets back True or False. Then the if/else looks at that answer and... hands
back the exact same answer. It's a middleman that adds nothing.

    def free_shipping(cart_total):
        return cart_total >= 35

The other mistake to name: `>` versus `>=`. A cart of exactly 35 dollars *does*
qualify. With `>` you'd tell that shopper "no", and it's the one test case a
beginner never thinks to try. When a rule says "or more", "at least", or "no less
than", reach for `>=`.

### starter
```python
def free_shipping(cart_total):
    
```

### solution
```python
def free_shipping(cart_total):
    return cart_total >= 35
```

### check
free_shipping(40) is True
free_shipping(35) is True
free_shipping(12) is False
free_shipping(0) is False
free_shipping(34) is False
free_shipping(100) is True

---

## mcq_four_vs_string_four
kind: mcq
title: Is 4 the same as "4"?
tags: types, predict, concept
difficulty: starter
answer: 3

### prompt
What does this code print?

    a = 4
    b = "4"
    print(a == b)

### choices
- True, because both `a` and `b` hold the value 4
- True, because Python converts `"4"` to `4` before comparing
- False, because a number and a string are never equal to each other
- The code crashes, because you can't compare a number to a string

---

## can_ride_coaster
kind: code_fn
title: Can they ride the coaster?
tags: logic, conditions, functions
difficulty: easy
entry: can_ride

### prompt
A roller coaster requires that you are taller than 120 cm **and** that you are
holding a ticket. Write `can_ride(height_cm, has_ticket)` that returns True only
when both are satisfied.

Examples

    can_ride(150, True) → True
    can_ride(150, False) → False
    can_ride(110, True) → False

Notes

- "Taller than 120" means strictly over 120 — exactly 120 is not tall enough.
- `and` is True only when the expression on each side is True.

### starter
```python
def can_ride(height_cm, has_ticket):
    
```

### solution
```python
def can_ride(height_cm, has_ticket):
    return height_cm > 120 and has_ticket
```

### check
can_ride(150, True) is True
can_ride(150, False) is False
can_ride(110, True) is False
can_ride(110, False) is False
can_ride(120, True) is False
can_ride(121, True) is True

---

## staircase_switches
kind: code_fn
title: One light, two switches
tags: logic, conditions, functions
difficulty: easy
entry: light_on

### prompt
A staircase light is wired to two switches, one at the top and one at the bottom.
The light is on exactly when the two switches are in *different* positions. Write
`light_on(top, bottom)`, where each argument is True or False, returning True when
the light is on.

Examples

    light_on(True, False) → True
    light_on(False, True) → True
    light_on(True, True) → False

Notes

- Each argument is already True or False.

### walkthrough
Four cases, and it's tempting to spell out all of them:

    if top == True and bottom == False:
        return True
    elif top == False and bottom == True:
        return True
    else:
        return False

Correct, but it buries the idea. Step back and read the two True rows: in both,
`top` and `bottom` *disagree*. And "these two disagree" has a name in Python — it's
`!=`.

    def light_on(top, bottom):
        return top != bottom

Booleans are ordinary values, so you can compare them to each other, not just test
them. That's the shift to make here: `top != bottom` asks "are these two different?"
and True/False are perfectly good things to ask that about.

One more habit to break while you're here: never write `if top == True`. `top` is
already True or False, so just write `if top`. Comparing a boolean to True is the
same redundancy as the if/else that returns True and False.

### starter
```python
def light_on(top, bottom):
    
```

### solution
```python
def light_on(top, bottom):
    return top != bottom
```

### check
light_on(True, False) is True
light_on(False, True) is True
light_on(True, True) is False
light_on(False, False) is False

---

## door_code_bug
kind: code_fn
title: One equals sign too few
tags: bugs, conditions, logic
difficulty: easy
entry: door_unlocks

### prompt
This function is supposed to unlock a door when the keypad code is 1234. Right now
it doesn't even run — Python refuses the file. Fix it.

Examples

    door_unlocks(1234) → True
    door_unlocks(1111) → False
    door_unlocks(0) → False

Notes

- `=` puts a value into a variable. `==` asks whether two values are the same.
- One character is enough to make it run. Once it runs, look again and ask whether
  the `if` is still earning its keep.

### walkthrough
Run the starter and Python won't even get as far as calling your function:

    SyntaxError: invalid syntax

That is actually good news. `if code = 1234:` tries to *assign* 1234 to `code` in
a spot where Python demands a question, and Python catches it up front. In some
other languages this same line compiles fine and silently sets the code to 1234
every time, so the door always opens — a real security bug that shipped in real
software. Python saves you from that by refusing outright.

The rule to memorize: one equals sign *stores*, two equals signs *ask*.

    code = 1234       # store: code is now 1234
    code == 1234      # ask: is code 1234? -> True or False

An `if` always wants the asking version:

    def door_unlocks(code):
        return code == 1234

And once you've made it a comparison, notice it's already True or False — the
`if`/`return True`/`return False` scaffolding can go entirely.

### starter
```python
def door_unlocks(code):
    if code = 1234:
        return True
    return False
```

### solution
```python
def door_unlocks(code):
    return code == 1234
```

### check
door_unlocks(1234) is True
door_unlocks(1111) is False
door_unlocks(0) is False
door_unlocks(4321) is False
door_unlocks(1235) is False

---

## valid_username
kind: code_fn
title: Is that username allowed?
tags: strings, validation, logic
difficulty: medium
entry: valid_username

### prompt
A site accepts a username when its length is between 3 and 12 characters
(inclusive) and the name is not "admin". Write `valid_username(name)` returning
True when the name is allowed.

Examples

    valid_username("joe") → True
    valid_username("ab") → False
    valid_username("admin") → False

Notes

- `len(name)` gives the number of characters in a string.
- "Between 3 and 12 (inclusive)" means 3 and 12 are both allowed.

### walkthrough
There are two independent rules, and the answer is True only when both hold — so
they're joined with `and`.

The length rule is a range. You could write it as two comparisons:

    len(name) >= 3 and len(name) <= 12

Python offers a shorter form that reads like math and means exactly the same thing:

    3 <= len(name) <= 12

The mistake waiting for you is "between 3 and 12" — does that include 3 and 12? The
prompt says *inclusive*, so yes, and that means `<=` on both ends, not `<`. Whenever
a spec says "between", find out about the endpoints before you write anything; they
are where the bugs live.

Then bolt on the second rule:

    def valid_username(name):
        return 3 <= len(name) <= 12 and name != "admin"

Note that "admin" passes the length test with room to spare — 5 characters. It has
to be excluded by name, which is why the `!=` is doing real work here rather than
being decoration.

### starter
```python
def valid_username(name):
    
```

### solution
```python
def valid_username(name):
    return 3 <= len(name) <= 12 and name != "admin"
```

### check
valid_username("joe") is True
valid_username("ab") is False
valid_username("admin") is False
valid_username("") is False
valid_username("abc") is True
valid_username("abcdefghijkl") is True
valid_username("abcdefghijklm") is False
valid_username("administrator") is False

---

## playlist_first_vs_last
kind: code_fn
title: Front-loaded playlist?
tags: arrays, indexing, logic
difficulty: medium
entry: front_loaded

### prompt
You have a list of play counts, one per song, in playlist order. Write
`front_loaded(plays)` that returns True when the first song was played more times
than the last song.

Examples

    front_loaded([90, 40, 12]) → True
    front_loaded([5, 40, 90]) → False
    front_loaded([7, 7]) → False

Notes

- "More than" is strict, so equal counts are not front-loaded.
- The list always has at least one song.

### walkthrough
Two things to get right, and neither is the comparison itself.

First, reaching the last item. Beginners write `plays[len(plays)]` and get an
IndexError, because a list of 3 items has indexes 0, 1, 2 — there is no index 3.
You could write `plays[len(plays) - 1]`, but Python gives you a cleaner way:
negative indexes count from the end, so `plays[-1]` is the last item, `plays[-2]`
the one before it.

Second, the counts are just numbers, so compare them and return the comparison:

    def front_loaded(plays):
        return plays[0] > plays[-1]

Now the edge case that surprises people: a one-song list like `[7]`. Then `plays[0]`
and `plays[-1]` are the *same* item, so you're asking `7 > 7`, which is False. That
falls out correctly with no special handling — but you should be able to say why
before you trust it.

### starter
```python
def front_loaded(plays):
    
```

### solution
```python
def front_loaded(plays):
    return plays[0] > plays[-1]
```

### check
front_loaded([90, 40, 12]) is True
front_loaded([5, 40, 90]) is False
front_loaded([7, 7]) is False
front_loaded([7]) is False
front_loaded([2, 1]) is True
front_loaded([0, 3, 0]) is False
