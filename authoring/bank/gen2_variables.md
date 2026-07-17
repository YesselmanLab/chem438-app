# Variables & math — more practice

---

## p_floor_div_seven_two
kind: mcq
title: Predict — 7 // 2
tags: predict, math
difficulty: easy
answer: 1

### prompt
What does this print?

    print(7 // 2)

### code
```python
print(7 // 2)
```

### choices
- 3
- 3.5
- 4
- 2

---

## p_true_div_seven_two
kind: mcq
title: Predict — 7 / 2
tags: predict, math
difficulty: easy
answer: 1

### prompt
What does this print?

    print(7 / 2)

### code
```python
print(7 / 2)
```

### choices
- 3.5
- 3
- 4
- 3.0 remainder 1

---

## p_two_to_third
kind: mcq
title: Predict — 2 ** 3
tags: predict, math
difficulty: easy
answer: 1

### prompt
What does this print?

    print(2 ** 3)

### code
```python
print(2 ** 3)
```

### choices
- 8
- 6
- 9
- 23

---

## p_mod_ten_three
kind: mcq
title: Predict — 10 % 3
tags: predict, math
difficulty: easy
answer: 1

### prompt
What does this print?

    print(10 % 3)

### code
```python
print(10 % 3)
```

### choices
- 1
- 3
- 0
- 3.33

---

## p_add_then_mul
kind: mcq
title: Predict — order of operations
tags: predict, math
difficulty: easy
answer: 1

### prompt
What does this print?

    print(2 + 3 * 4)

### code
```python
print(2 + 3 * 4)
```

### choices
- 14
- 20
- 24
- 11

---

## p_int_truncate
kind: mcq
title: Predict — int(3.9)
tags: predict, numbers
difficulty: easy
answer: 1

### prompt
What does this print?

    print(int(3.9))

### code
```python
print(int(3.9))
```

### choices
- 3
- 4
- 3.9
- 0

---

## p_round_banker
kind: mcq
title: Predict — round(2.5)
tags: predict, numbers
difficulty: medium
answer: 1

### prompt
What does this print?

    print(round(2.5))

Notes

- Python rounds a value that lands exactly halfway toward the nearest *even* whole number. This is called banker's rounding, and it surprises almost everyone.

### code
```python
print(round(2.5))
```

### choices
- 2
- 3
- 2.5
- 1

---

## p_augmented_add
kind: mcq
title: Predict — x += 3
tags: predict, math
difficulty: easy
answer: 1

### prompt
What does this print?

    x = 5
    x += 3
    print(x)

### code
```python
x = 5
x += 3
print(x)
```

### choices
- 8
- 5
- 3
- 53

---

## p_int_plus_int
kind: mcq
title: Predict — 5 + 5
tags: predict, types
difficulty: easy
answer: 1

### prompt
What does this print?

    print(5 + 5)

Notes

- These `5`s have no quotes around them, so they are numbers.

### code
```python
print(5 + 5)
```

### choices
- 10
- 55
- "10"
- 25

---

## p_type_div
kind: mcq
title: Predict — type(10 / 2)
tags: predict, types
difficulty: medium
answer: 1

### prompt
What does this print?

    print(type(10 / 2))

Notes

- `10 / 2` is exactly 5, with nothing left over.

### code
```python
print(type(10 / 2))
```

### choices
- <class 'float'>
- <class 'int'>
- 5.0
- <class 'number'>

---

## p_power_before_mult
kind: mcq
title: Predict — 2 * 3 ** 2
tags: predict, math
difficulty: medium
answer: 1

### prompt
What does this print?

    print(2 * 3 ** 2)

Notes

- `**` runs before `*`.

### code
```python
print(2 * 3 ** 2)
```

### choices
- 18
- 36
- 12
- 64

---

## p_neg_floor_div
kind: mcq
title: Predict — -7 // 2
tags: predict, math
difficulty: hard
answer: 1

### prompt
What does this print?

    print(-7 // 2)

Notes

- `//` always rounds *down* — toward the smaller number — not toward zero.

### code
```python
print(-7 // 2)
```

### choices
- -4
- -3
- -3.5
- 3

---

## p_round_two_dp
kind: mcq
title: Predict — round to 2 places
tags: predict, numbers
difficulty: medium
answer: 1

### prompt
What does this print?

    print(round(3.14159, 2))

### code
```python
print(round(3.14159, 2))
```

### choices
- 3.14
- 3.15
- 3.1
- 3

---

## p_paren_first
kind: mcq
title: Predict — parentheses first
tags: predict, math
difficulty: easy
answer: 1

### prompt
What does this print?

    print((2 + 3) * 4)

### code
```python
print((2 + 3) * 4)
```

### choices
- 20
- 14
- 24
- 9

---

## bug_power_caret
kind: code_fn
title: The wrong power symbol
tags: bugs, math, numbers
difficulty: easy
entry: power

### prompt
`power` should return `base` raised to the power `exp` — so `power(2, 3)` is `8` (2 × 2 × 2). Instead it returns strange small numbers. Fix it.

Examples

    power(2, 3) → 8
    power(5, 2) → 25
    power(3, 3) → 27

Notes

- In Python, `^` does *not* mean "to the power of" — it is a different operator entirely.
- The power operator is `**`.

### starter
```python
def power(base, exp):
    return base ^ exp
```

### solution
```python
def power(base, exp):
    return base ** exp
```

### check
power(2, 3) == 8
power(5, 2) == 25
power(3, 3) == 27
power(10, 2) == 100

---

## bug_avg_floor
kind: code_fn
title: The halfway point that lost its decimal
tags: bugs, math, numbers
difficulty: medium
entry: midpoint

### prompt
`midpoint` should return the value exactly halfway between two mile markers. For markers 3 and 4 that is `3.5`, but the code returns `3`. Fix it.

Examples

    midpoint(3, 4) → 3.5
    midpoint(2, 4) → 3.0
    midpoint(10, 15) → 12.5

Notes

- `//` throws away the fractional part, so it can never return `3.5`.
- Which division operator keeps the decimal?

### starter
```python
def midpoint(a, b):
    return (a + b) // 2
```

### solution
```python
def midpoint(a, b):
    return (a + b) / 2
```

### check
midpoint(3, 4) == 3.5
midpoint(2, 4) == 3.0
midpoint(1, 2) == 1.5
midpoint(10, 15) == 12.5

---

## bug_whole_groups
kind: code_fn
title: Counting full boxes
tags: bugs, math, numbers
difficulty: medium
entry: whole_groups

### prompt
`whole_groups` should return how many *completely full* boxes you can fill — so 7 items with 2 per box makes `3` full boxes (with one left over). Instead it returns things like `3.5`. Fix it.

Examples

    whole_groups(7, 2) → 3
    whole_groups(9, 4) → 2
    whole_groups(5, 5) → 1

Notes

- A count of boxes should be a whole number, never `3.5`.
- `/` always gives a decimal; you want the operator that divides and drops the remainder.

### starter
```python
def whole_groups(total, size):
    return total / size
```

### solution
```python
def whole_groups(total, size):
    return total // size
```

### check
whole_groups(7, 2) == 3
whole_groups(9, 4) == 2
whole_groups(5, 5) == 1
whole_groups(20, 6) == 3
whole_groups(10, 3) == 3

---

## bug_add_boxes
kind: code_fn
title: Two counts typed as text
tags: bugs, types, numbers
difficulty: medium
entry: add_boxes

### prompt
`add_boxes` receives two counts as text (like `"12"` and `"3"`) and should return their sum as a number. Instead, `add_boxes("12", "3")` comes back as `"123"`. Fix it.

Examples

    add_boxes("12", "3") → 15
    add_boxes("4", "5") → 9
    add_boxes("11", "9") → 20

Notes

- `+` between two strings glues them together instead of adding.
- Convert each piece with `int()` before you add.

### starter
```python
def add_boxes(a_text, b_text):
    return a_text + b_text
```

### solution
```python
def add_boxes(a_text, b_text):
    return int(a_text) + int(b_text)
```

### check
add_boxes("12", "3") == 15
add_boxes("4", "5") == 9
add_boxes("11", "9") == 20
add_boxes("10", "0") == 10

---

## wrong_equals_sign
kind: mcq
title: What's wrong — = vs ==
tags: bugs, language_fundamentals
difficulty: medium
answer: 1

### prompt
This code crashes with a `SyntaxError`. What is wrong?

    temperature = 70
    if temperature = 100:
        print("hot")

### choices
- Line 2 uses `=` (assignment) where it needs `==` (comparison)
- `print` should be spelled `Print`
- The string `"hot"` should be a number
- You cannot store a number in a variable called `temperature`

---

## wrong_caret_power
kind: mcq
title: What's wrong — using ^ for a power
tags: bugs, math
difficulty: medium
answer: 1

### prompt
This is meant to print `8` (which is 2 to the power of 3), but it prints `1` instead. Why?

    print(2 ^ 3)

### choices
- `^` is not the power operator in Python; you need `**`
- `2 ^ 3` is a syntax error and prints nothing
- `print` can only display one number at a time
- Python cannot compute powers of 2

---

## wrong_missing_quotes
kind: mcq
title: What's wrong — a missing pair of quotes
tags: bugs, types
difficulty: medium
answer: 1

### prompt
Running this raises `NameError: name 'Maria' is not defined`. Why?

    first_name = Maria
    print(first_name)

### choices
- `Maria` needs quotes; without them Python thinks it is a variable name
- You are not allowed to name a variable `first_name`
- `print` needs the value written twice
- Variables can never hold text, only numbers

---

## wrong_int_of_decimal_text
kind: mcq
title: What's wrong — int() on decimal text
tags: bugs, types, numbers
difficulty: medium
answer: 1

### prompt
This line raises a `ValueError`. What is the problem?

    age = int("42.5")

### choices
- `int()` cannot convert text that has a decimal point; use `float()` first
- `int()` never works on text of any kind
- `"42.5"` is too large a number for an int
- You must write `Int` with a capital I

---

## concept_float_value
kind: mcq
title: Which value is a float?
tags: concept, types, numbers
difficulty: easy
answer: 3

### prompt
Which of these values is a float?

### choices
- 7
- "7"
- 7.0
- 700

---

## concept_equals_does
kind: mcq
title: What does x = 5 do?
tags: concept, language_fundamentals
difficulty: easy
answer: 1

### prompt
What does the line `count = 5` do?

### choices
- Stores the value `5` in a variable called `count`
- Checks whether `count` is already equal to `5`
- Prints `5` to the screen
- Raises an error unless `count` already exists

---

## concept_floor_div
kind: mcq
title: What does // do?
tags: concept, math, numbers
difficulty: easy
answer: 1

### prompt
What does the `//` operator do in Python?

### choices
- Divides and throws away the remainder, giving a whole-number result
- Divides and keeps *only* the remainder
- Starts a comment
- Doubles the number on its left

---

## concept_which_float_op
kind: mcq
title: Which operator always gives a float?
tags: concept, numbers, types
difficulty: medium
answer: 1

### prompt
Which operator always produces a float, even when the two numbers divide evenly (like `10` and `2`)?

### choices
- /
- //
- %
- **

---

## concept_mod_meaning
kind: mcq
title: What does 17 % 5 give you?
tags: concept, math, numbers
difficulty: easy
answer: 1

### prompt
What does `17 % 5` give you?

### choices
- The remainder left after dividing 17 by 5
- 17 percent of 5
- 17 divided by 5, written as a decimal
- The larger of 17 and 5

---

## concept_augmented_meaning
kind: mcq
title: What is score += 10 shorthand for?
tags: concept, language_fundamentals, math
difficulty: easy
answer: 1

### prompt
The line `score += 10` is shorthand for which line?

### choices
- score = score + 10
- score == score + 10
- score + 10
- score = 10

---

## store_remainder
kind: code_var
title: Store a remainder
tags: math, numbers
difficulty: easy
entry: remainder

### prompt
In a variable named `remainder`, store the remainder left over when 17 is divided by 5.

Notes

- The `%` operator gives you the remainder.
- Do not print it — just store it in the variable.

### starter
```python
# store the remainder of 17 divided by 5
remainder =
```

### solution
```python
remainder = 17 % 5
```

### check
remainder == 2

---

## to_the_power
kind: code_fn
title: Raise a number to a power
tags: math, numbers
difficulty: easy
entry: to_the_power

### prompt
Return `base` raised to the power `exp`.

Examples

    to_the_power(2, 4) → 16
    to_the_power(5, 3) → 125
    to_the_power(10, 0) → 1

Notes

- The power operator is `**`.
- Don't forget to return the result.

### starter
```python
def to_the_power(base, exp):
    pass
```

### solution
```python
def to_the_power(base, exp):
    return base ** exp
```

### check
to_the_power(2, 4) == 16
to_the_power(5, 3) == 125
to_the_power(10, 0) == 1
to_the_power(3, 2) == 9

---

## leftover_items
kind: code_fn
title: What's left over
tags: math, numbers
difficulty: easy
entry: leftover_items

### prompt
You are packing `items` into boxes that each hold `per_box`. Return how many items are left over after filling as many full boxes as you can.

Examples

    leftover_items(17, 5) → 2
    leftover_items(10, 2) → 0
    leftover_items(9, 4) → 1

Notes

- The `%` operator gives you exactly this leftover amount.
- Don't forget to return the result.

### starter
```python
def leftover_items(items, per_box):
    pass
```

### solution
```python
def leftover_items(items, per_box):
    return items % per_box
```

### check
leftover_items(17, 5) == 2
leftover_items(10, 2) == 0
leftover_items(9, 4) == 1
leftover_items(20, 6) == 2

---

## round_to_cents
kind: code_fn
title: Round a price to cents
tags: numbers, math
difficulty: easy
entry: round_to_cents

### prompt
Return the price rounded to 2 decimal places (the nearest cent).

Examples

    round_to_cents(3.14159) → 3.14
    round_to_cents(9.999) → 10.0
    round_to_cents(2.5) → 2.5

Notes

- `round(value, 2)` rounds to 2 decimal places.
- Don't forget to return the result.

### starter
```python
def round_to_cents(price):
    pass
```

### solution
```python
def round_to_cents(price):
    return round(price, 2)
```

### check
round_to_cents(3.14159) == 3.14
round_to_cents(9.999) == 10.0
round_to_cents(2.5) == 2.5
round_to_cents(0.0) == 0.0

---

## higher_score
kind: code_fn
title: The higher of two scores
tags: numbers, math
difficulty: easy
entry: higher_score

### prompt
Two players finished a round. Return the higher of their two scores.

Examples

    higher_score(4, 9) → 9
    higher_score(12, 3) → 12
    higher_score(7, 7) → 7

Notes

- `max(a, b)` gives you the larger of two values.
- Don't forget to return the result.

### starter
```python
def higher_score(a, b):
    pass
```

### solution
```python
def higher_score(a, b):
    return max(a, b)
```

### check
higher_score(4, 9) == 9
higher_score(12, 3) == 12
higher_score(7, 7) == 7
higher_score(0, 5) == 5

---

## points_apart
kind: code_fn
title: How far apart
tags: numbers, math
difficulty: medium
entry: points_apart

### prompt
Return how many points separate two scores. The answer is always zero or positive, no matter which score is bigger.

Examples

    points_apart(3, 10) → 7
    points_apart(10, 3) → 7
    points_apart(5, 5) → 0

Notes

- `abs()` turns a negative number positive and leaves a positive number alone.
- Don't forget to return the result.

### starter
```python
def points_apart(a, b):
    pass
```

### solution
```python
def points_apart(a, b):
    return abs(a - b)
```

### check
points_apart(3, 10) == 7
points_apart(10, 3) == 7
points_apart(5, 5) == 0
points_apart(0, 8) == 8
