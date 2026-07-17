# Booleans & if/else — more practice

Extra drill on True/False, comparisons, combining conditions, and choosing a path
with if/elif/else. Heavy on predicting output and spotting the bug.

---

## pb_greater
kind: mcq
title: Predict — did you clear the jump?
tags: predict, logic
difficulty: starter
answer: 1

### prompt
The ledge needs a jump of 5; yours gives 3. What does this print?

    jump = 3
    print(jump > 5)

### code
jump = 3
print(jump > 5)

### choices
- False
- True
- jump > 5
- 0

---

## pb_eq
kind: mcq
title: Predict — do the dice match?
tags: predict, logic
difficulty: starter
answer: 1

### prompt
You rolled a 2 and so did your friend. What does this print?

    my_roll = 2
    their_roll = 2
    print(my_roll == their_roll)

### code
my_roll = 2
their_roll = 2
print(my_roll == their_roll)

### choices
- True
- False
- 2
- 4

---

## pb_str_case
kind: mcq
title: Predict — is "yes" the same as "YES"?
tags: predict, logic
difficulty: starter
answer: 1

### prompt
A login checks the typed reply against the saved one. What does this print?

    print("yes" == "YES")

### code
print("yes" == "YES")

### choices
- False
- True
- yes
- YES

---

## pb_and_mix
kind: mcq
title: Predict — one side of `and` fails
tags: predict, logic
difficulty: easy
answer: 1

### prompt
Cast the spell only if HP is up AND mana is over 50. What does this print?

    hp = 10
    mana = 20
    print(hp > 0 and mana > 50)

### code
hp = 10
mana = 20
print(hp > 0 and mana > 50)

### choices
- False
- True
- hp > 0
- None

---

## pb_not_true
kind: mcq
title: Predict — flipping game_over
tags: predict, logic
difficulty: starter
answer: 1

### prompt
`game_over` is True; `not` flips it. What does this print?

    game_over = True
    print(not game_over)

### code
game_over = True
print(not game_over)

### choices
- False
- True
- not game_over
- 0

---

## pb_or_zero
kind: mcq
title: Predict — 0 coins or a backup 5
tags: predict, logic
difficulty: medium
answer: 1

### prompt
Watch closely — `or` hands back the first truthy value, not True/False. You have 0
coins and fall back to 5. What prints?

    coins = 0
    print(coins or 5)

### code
coins = 0
print(coins or 5)

### choices
- 5
- True
- 0
- False

---

## pb_or_empty
kind: mcq
title: Predict — blank nickname falls back
tags: predict, logic
difficulty: medium
answer: 1

### prompt
If the nickname is blank, fall back to "Guest". Watch what `or` returns.

    nickname = ""
    print(nickname or "Guest")

### code
nickname = ""
print(nickname or "Guest")

### choices
- Guest
- True
- (nothing — a blank line)
- nickname or "Guest"

---

## pb_num_str
kind: mcq
title: Predict — the number 2 versus the typed "2"
tags: predict, logic
difficulty: easy
answer: 1

### prompt
A text box hands you the string `"2"`; you compare it to the number 2. What prints?

    typed = "2"
    print(2 == typed)

### code
typed = "2"
print(2 == typed)

### choices
- False
- True
- The code crashes with a TypeError
- 2

---

## pf_temp_elif
kind: mcq
title: Predict — which weather label?
tags: predict, conditions
difficulty: easy
answer: 1

### prompt
A weather app labels today's 55°F. What does this print?

    temp = 55
    if temp >= 80:
        print("hot")
    elif temp >= 60:
        print("warm")
    elif temp >= 40:
        print("cool")
    else:
        print("cold")

### code
temp = 55
if temp >= 80:
    print("hot")
elif temp >= 60:
    print("warm")
elif temp >= 40:
    print("cool")
else:
    print("cold")

### choices
- cool
- warm
- cold
- hot

---

## pf_wrong_order
kind: mcq
title: Predict — the reward tiers are in the wrong order
tags: predict, conditions
difficulty: medium
answer: 1

### prompt
A rewards program ranks a $120 spender — but look at the order of the tiers.

    spend = 120
    if spend >= 50:
        print("silver")
    elif spend >= 100:
        print("gold")
    else:
        print("none")

### code
spend = 120
if spend >= 50:
    print("silver")
elif spend >= 100:
    print("gold")
else:
    print("none")

### choices
- silver
- gold
- none
- silver\ngold

---

## pf_first_wins
kind: mcq
title: Predict — 12 hits two tests
tags: predict, conditions
difficulty: medium
answer: 1

### prompt
12 is divisible by both 2 and 3. Does the elif also run?

    n = 12
    if n % 2 == 0:
        print("even")
    elif n % 3 == 0:
        print("three")
    else:
        print("other")

### code
n = 12
if n % 2 == 0:
    print("even")
elif n % 3 == 0:
    print("three")
else:
    print("other")

### choices
- even
- even\nthree
- three
- other

---

## pf_empty_falsy
kind: mcq
title: Predict — a blank username in an if
tags: predict, conditions
difficulty: medium
answer: 1

### prompt
A new player left the username blank. What does this print?

    username = ""
    if username:
        print("saved")
    else:
        print("empty")

### code
username = ""
if username:
    print("saved")
else:
    print("empty")

### choices
- empty
- saved
- (nothing — a blank line)
- The code crashes

---

## pf_ternary
kind: mcq
title: Predict — the one-line ticket label
tags: predict, conditions
difficulty: easy
answer: 1

### prompt
A kiosk labels a 20-year-old in one line. What does this print?

    age = 20
    rating = "adult" if age >= 18 else "minor"
    print(rating)

### code
age = 20
rating = "adult" if age >= 18 else "minor"
print(rating)

### choices
- adult
- minor
- True
- adult if age >= 18 else minor

---

## pf_two_separate_ifs
kind: mcq
title: Predict — two separate score checks
tags: predict, conditions
difficulty: medium
answer: 1

### prompt
Your score is 10 and two separate ifs each award a badge. What prints?

    score = 10
    if score > 5:
        print("big")
    if score > 8:
        print("huge")

### code
score = 10
if score > 5:
    print("big")
if score > 8:
    print("huge")

### choices
- big\nhuge
- big
- huge
- (nothing — a blank line)

---

## wb_assign_if
kind: mcq
title: What's wrong — one equals sign
tags: bugs, logic
difficulty: easy
answer: 1

### prompt
This code won't run. What is wrong with it?

    if level = 5:
        print("boss fight")

### choices
- It uses `=` (which stores a value) where it needs `==` (which compares)
- It is missing a colon at the end of the `if` line
- You can't compare numbers in Python with `==`
- `print` needs to be on the same line as `if`

---

## wb_or_split
kind: mcq
title: What's wrong — `or "quit"`
tags: bugs, logic
difficulty: medium
answer: 1

### prompt
This is meant to be True only when `cmd` is `"go"` or `"quit"`, but it is True for
every command. What is wrong?

    if cmd == "go" or "quit":
        print("valid command")

### choices
- `"quit"` on its own is always truthy, so the whole condition is always True — it should be `cmd == "go" or cmd == "quit"`
- `or` should be `and`
- You cannot compare strings with `==`
- The `if` needs an `else` to work

---

## wb_wrap_comparison
kind: mcq
title: What's wrong — the long-way height check
tags: bugs, logic
difficulty: easy
answer: 1

### prompt
This ride-height check works, but it does something the long way. What is the real
problem?

    def can_ride(height):
        if height >= 48:
            return True
        else:
            return False

### choices
- The if/else is unnecessary — `return height >= 48` gives the exact same answer
- It should use `==` instead of `>=`
- It crashes when `height` is exactly 48
- It returns the wrong answer for tall riders

---

## fix_both_on
kind: code_fn
title: Fix — both keys must be turned
tags: bugs, logic, functions
difficulty: easy
entry: both_on

### prompt
A rocket launches only when *both* safety keys are turned. `both_on(a, b)` takes
two True/False values and should return True only when both are True. It returns
True too often — fix it.

Examples

    both_on(True, True) → True
    both_on(True, False) → False

Notes

- `and` is True only when the value on each side is True.
- `or` is True when *either* side is True — that's the bug here.

### starter
```python
def both_on(a, b):
    return a or b
```

### solution
```python
def both_on(a, b):
    return a and b
```

### check
both_on(True, True) is True
both_on(True, False) is False
both_on(False, True) is False
both_on(False, False) is False

---

## fix_matches_secret
kind: code_fn
title: Fix — the door password won't even run
tags: bugs, logic, functions
difficulty: easy
entry: matches_secret

### prompt
`matches_secret(word)` should return True when `word` is exactly `"open"` (the magic
word for the door). Right now Python refuses to even run the file. Fix it.

Examples

    matches_secret("open") → True
    matches_secret("nope") → False

Notes

- `=` stores a value into a variable. `==` asks whether two values are equal.
- Once it runs, notice the comparison is already True or False.

### starter
```python
def matches_secret(word):
    if word = "open":
        return True
    return False
```

### solution
```python
def matches_secret(word):
    return word == "open"
```

### check
matches_secret("open") is True
matches_secret("nope") is False
matches_secret("") is False
matches_secret("Open") is False

---

## wf_missing_colon
kind: mcq
title: What's wrong — no colon
tags: bugs, conditions
difficulty: easy
answer: 1

### prompt
This code won't run. What is wrong with it?

    if score > 90
        print("high score!")

### choices
- The `if` line is missing its colon (`:`) at the end
- `score` needs to be written in quotes
- `print` should not be indented
- It needs an `else` branch to be valid

---

## wf_order_unreachable
kind: mcq
title: What's wrong — a 5-star review that never happens
tags: bugs, conditions
difficulty: medium
answer: 1

### prompt
This is supposed to return `"great"` for 4 or 5 stars, but it never does. What is
wrong?

    def rate(stars):
        if stars >= 1:
            return "ok"
        elif stars >= 4:
            return "great"
        else:
            return "none"

### choices
- Any value that is `>= 4` is also `>= 1`, so the first branch always wins and `"great"` is unreachable — the `>= 4` test must come first
- `elif` is spelled wrong
- It should use `==` instead of `>=`
- The function is missing a `return` statement

---

## fix_size_label
kind: code_fn
title: Fix — the download-size labels come out wrong
tags: bugs, conditions, functions
difficulty: medium
entry: size_label

### prompt
`size_label(n)` labels a download in megabytes: `"negative"` when `n` is below 0,
`"small"` for 0 through 99, and `"large"` for 100 or more. The branches are in an
order that makes `"large"` impossible — fix it.

Examples

    size_label(150) → "large"
    size_label(50) → "small"
    size_label(-3) → "negative"

Notes

- The first branch whose test is True wins; the rest are skipped.
- Order your tests from the most specific to the most general.

### starter
```python
def size_label(n):
    if n >= 0:
        return "small"
    elif n >= 100:
        return "large"
    else:
        return "negative"
```

### solution
```python
def size_label(n):
    if n < 0:
        return "negative"
    elif n >= 100:
        return "large"
    else:
        return "small"
```

### check
size_label(150) == "large"
size_label(50) == "small"
size_label(-3) == "negative"
size_label(100) == "large"
size_label(0) == "small"

---

## fix_ticket_price
kind: code_fn
title: Fix — the movie price never comes back
tags: bugs, conditions, functions
difficulty: medium
entry: ticket_price

### prompt
`ticket_price(age)` gives the movie ticket price: 0 for under 5, 10 for 5 through 64,
and 7 for 65 and up. It picks the right price but hands back `None` every time. Fix it.

Examples

    ticket_price(3) → 0
    ticket_price(30) → 10
    ticket_price(70) → 7

Notes

- Setting `price = ...` inside the branches is not the same as returning it.
- A function gives back a value only when you `return` it.

### starter
```python
def ticket_price(age):
    if age < 5:
        price = 0
    elif age < 65:
        price = 10
    else:
        price = 7
```

### solution
```python
def ticket_price(age):
    if age < 5:
        price = 0
    elif age < 65:
        price = 10
    else:
        price = 7
    return price
```

### check
ticket_price(3) == 0
ticket_price(30) == 10
ticket_price(70) == 7
ticket_price(64) == 10
ticket_price(65) == 7

---

## cb_and_both
kind: mcq
title: Concept — what a co-op door needs
tags: concept, logic
difficulty: starter
answer: 1

### prompt
A co-op door opens on `player1_ready and player2_ready`. For `a and b` to be True,
how many of `a` and `b` must be True?

### choices
- Both `a` and `b` must be True
- At least one of them must be True
- Neither of them needs to be True
- Exactly one of them must be True

---

## cb_truthy
kind: mcq
title: Concept — which value is falsy?
tags: concept, logic
difficulty: medium
answer: 3

### prompt
Which of these values is *falsy* (Python treats it like False in an `if`)?

### choices
- the string `"0"`
- the number `7`
- the empty string `""`
- the list `[0]`

---

## cb_return_comparison
kind: mcq
title: Concept — return the comparison directly
tags: concept, logic
difficulty: easy
answer: 1

### prompt
Why can you write `return score >= 60` instead of an if/else that returns True or
False?

### choices
- Because `score >= 60` already evaluates to True or False on its own
- Because `return` always turns its value into True
- Because `>=` only works inside a `return`
- You can't — an if/else is always required

---

## cb_eq_vs_assign
kind: mcq
title: Concept — `=` versus `==`
tags: concept, logic
difficulty: starter
answer: 1

### prompt
What is the difference between `=` and `==` in Python?

### choices
- `=` stores a value in a variable; `==` checks whether two values are equal
- They mean exactly the same thing
- `=` checks equality; `==` stores a value
- `==` only works with numbers, `=` works with everything

---

## cf_elif_only_first
kind: mcq
title: Concept — how many elif branches run
tags: concept, conditions
difficulty: easy
answer: 1

### prompt
In an `if`/`elif`/`elif` chain where two of the conditions happen to be True, how
many branches actually run?

### choices
- Only the first True branch runs; the rest are skipped
- Every branch whose condition is True runs
- Only the last True branch runs
- None run unless there is an `else`

---

## cf_else
kind: mcq
title: Concept — when does `else` run?
tags: concept, conditions
difficulty: starter
answer: 1

### prompt
When does the `else` block run?

### choices
- Only when none of the `if`/`elif` conditions were True
- Always, right after the `if` block
- Whenever the `if` condition is True
- Only when there is no `elif` in the chain

---

## cf_indent
kind: mcq
title: Concept — what marks the block
tags: concept, conditions
difficulty: starter
answer: 1

### prompt
What decides which lines belong to an `if` block in Python?

### choices
- The indentation — the spaces at the start of the lines
- Curly braces `{ }` around the lines
- The keyword `end`
- A semicolon at the end of each line

---

## cf_ternary_form
kind: mcq
title: Concept — the one-line conditional shape
tags: concept, conditions
difficulty: medium
answer: 1

### prompt
Which line correctly gives `x` the value `"yes"` when `ok` is True, and `"no"`
otherwise?

### choices
- `x = "yes" if ok else "no"`
- `x = if ok then "yes" else "no"`
- `x = ok ? "yes" : "no"`
- `x = "yes" if ok then "no"`

---

## wa_is_teenager
kind: code_fn
title: Write — is this player a teenager?
tags: logic, functions
difficulty: easy
entry: is_teenager

### prompt
A game asks for the player's age band. Write `is_teenager(age)` that returns True
when `age` is between 13 and 19, inclusive, and False otherwise.

Examples

    is_teenager(15) → True
    is_teenager(13) → True
    is_teenager(20) → False

Notes

- "Between 13 and 19 inclusive" means 13 and 19 both count.
- You can chain the comparison: `13 <= age <= 19` — and return it directly.

### starter
```python
def is_teenager(age):
    
```

### solution
```python
def is_teenager(age):
    return 13 <= age <= 19
```

### check
is_teenager(15) is True
is_teenager(13) is True
is_teenager(19) is True
is_teenager(20) is False
is_teenager(12) is False
is_teenager(0) is False

---

## wa_is_weekend_day
kind: code_fn
title: Write — can we sleep in today?
tags: validation, functions
difficulty: easy
entry: is_weekend_day

### prompt
Write `is_weekend_day(day)` that returns True when `day` is `"Sat"` or `"Sun"`,
and False for any other day.

Examples

    is_weekend_day("Sat") → True
    is_weekend_day("Sun") → True
    is_weekend_day("Mon") → False

Notes

- `day in ["Sat", "Sun"]` asks whether `day` is one of the items in the list.
- That membership test is already True or False — return it directly.

### starter
```python
def is_weekend_day(day):
    
```

### solution
```python
def is_weekend_day(day):
    return day in ["Sat", "Sun"]
```

### check
is_weekend_day("Sat") is True
is_weekend_day("Sun") is True
is_weekend_day("Mon") is False
is_weekend_day("Fri") is False
is_weekend_day("") is False

---

## va_is_positive
kind: code_var
title: Store — is the score above zero?
tags: logic
difficulty: starter
entry: answer

### prompt
Store in a variable named `answer` whether the score 5 is greater than 0. Don't
type `True` yourself — let a comparison produce the value.

Notes

- `5 > 0` evaluates to a True/False value all on its own.
- Assign that comparison straight into `answer`.

### starter
```python
answer = ___
```

### solution
```python
answer = 5 > 0
```

### check
answer is True

---

## wa_sign_label
kind: code_fn
title: Write — label a temperature's sign
tags: conditions, functions
difficulty: easy
entry: sign_label

### prompt
Write `sign_label(n)` for a thermometer that returns `"positive"` when `n` is above
0, `"zero"` when `n` is exactly 0, and `"negative"` when `n` is below 0.

Examples

    sign_label(4) → "positive"
    sign_label(0) → "zero"
    sign_label(-2) → "negative"

Notes

- Three outcomes means an `if` / `elif` / `else`.
- Make sure exactly one branch fires for `0`.

### starter
```python
def sign_label(n):
    
```

### solution
```python
def sign_label(n):
    if n > 0:
        return "positive"
    elif n == 0:
        return "zero"
    else:
        return "negative"
```

### check
sign_label(4) == "positive"
sign_label(0) == "zero"
sign_label(-2) == "negative"
sign_label(100) == "positive"
sign_label(-1) == "negative"

---

## wa_pass_or_fail
kind: code_fn
title: Write — did the quiz pass?
tags: conditions, functions
difficulty: starter
entry: pass_or_fail

### prompt
A quiz needs 60 points or more to pass. Write `pass_or_fail(points)` that returns
`"pass"` when `points` is 60 or more, and `"fail"` otherwise.

Examples

    pass_or_fail(75) → "pass"
    pass_or_fail(60) → "pass"
    pass_or_fail(59) → "fail"

Notes

- "60 or more" includes exactly 60, so use `>=`.

### starter
```python
def pass_or_fail(points):
    
```

### solution
```python
def pass_or_fail(points):
    if points >= 60:
        return "pass"
    else:
        return "fail"
```

### check
pass_or_fail(75) == "pass"
pass_or_fail(60) == "pass"
pass_or_fail(59) == "fail"
pass_or_fail(0) == "fail"
pass_or_fail(100) == "pass"

---

## wa_bigger
kind: code_fn
title: Write — whose high score wins?
tags: conditions, functions
difficulty: easy
entry: bigger

### prompt
Write `bigger(a, b)` that returns the larger of two high scores. If they are tied,
returning either one is fine (they're the same value).

Examples

    bigger(3, 9) → 9
    bigger(10, 4) → 10
    bigger(5, 5) → 5

Notes

- Compare the two with `>` and return the one that wins.

### starter
```python
def bigger(a, b):
    
```

### solution
```python
def bigger(a, b):
    if a > b:
        return a
    else:
        return b
```

### check
bigger(3, 9) == 9
bigger(10, 4) == 10
bigger(5, 5) == 5
bigger(-1, -8) == -1
bigger(0, 7) == 7
