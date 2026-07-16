# Types & conversion

Turning text into numbers, numbers into text, and knowing what kind of value you actually have.

---

## cart_total_from_text
kind: code_fn
title: The total came in as text
tags: types, numbers, language_fundamentals
difficulty: starter
entry: cart_total_from_text

### prompt
A checkout page hands you the cart total as text, like the string `"8.50"`. Return that same amount as a real number you could do math with.

Examples

    cart_total_from_text("8.50") → 8.5
    cart_total_from_text("3.25") → 3.25
    cart_total_from_text("10.00") → 10.0

Notes

- A string of digits is not a number — `"8.50" * 2` gives you `"8.508.50"`, not `17.0`.
- Use `float()` to convert.
- Don't forget to return the result.

### starter
```python
def cart_total_from_text(total_text):
    pass
```

### solution
```python
def cart_total_from_text(total_text):
    return float(total_text)
```

### check
cart_total_from_text("8.50") == 8.5
cart_total_from_text("3.25") == 3.25
cart_total_from_text("10.00") == 10.0
cart_total_from_text("0.05") == 0.05

---

## nickname_filled
kind: code_fn
title: Did they pick a nickname?
tags: types, strings, logic
difficulty: starter
entry: nickname_filled

### prompt
A signup form gives you whatever the user typed into the nickname box, as a string. Return `True` if they typed anything at all, and `False` if they left it blank.

Examples

    nickname_filled("ace") → True
    nickname_filled("") → False
    nickname_filled("Zebra99") → True

Notes

- A blank box arrives as the empty string `""`.
- `bool()` on a string is `False` for the empty string and `True` for every other string.
- Don't forget to return the result.

### starter
```python
def nickname_filled(nickname):
    pass
```

### solution
```python
def nickname_filled(nickname):
    return bool(nickname)
```

### check
nickname_filled("ace") is True
nickname_filled("") is False
nickname_filled("Zebra99") is True
nickname_filled("x") is True

---

## whole_dollars_only
kind: code_fn
title: Ignore the cents
tags: types, numbers, math
difficulty: starter
entry: whole_dollars_only

### prompt
A receipt line gives you a price as a decimal number, like `12.99`. Return just the whole-dollar part of it.

Examples

    whole_dollars_only(12.99) → 12
    whole_dollars_only(0.99) → 0
    whole_dollars_only(199.95) → 199

Notes

- `int()` on a float throws the decimal part away.
- Prices are never negative here.

### walkthrough
The tempting move is to reach for `round()`, because "12.99 is basically 13". But read the task again: it asks for the whole-dollar *part*, not the nearest dollar. Those are different questions, and `12.99` is exactly where they disagree.

    round(12.99)  →  13
    int(12.99)    →  12

`int()` does not round. It chops — it walks back to the whole number and drops everything after the decimal point. `round()` fails almost immediately here: `round(12.99)` is `13`, not `12`, so the very first check catches it.

The clearest place to see the difference is `0.99`. `round(0.99)` is `1` — round looks at the whole value and asks "which dollar is it nearest?". `int(0.99)` is `0` — int just deletes the cents, and there was never a dollar there to begin with. That is why the edge case is in the checks: an edge case is not busywork, it is the input that tells two plausible answers apart in the most obvious way.

So the body is one line:

    return int(price)

### starter
```python
def whole_dollars_only(price):
    
```

### solution
```python
def whole_dollars_only(price):
    return int(price)
```

### check
whole_dollars_only(12.99) == 12
whole_dollars_only(0.99) == 0
whole_dollars_only(199.95) == 199
whole_dollars_only(5.0) == 5

---

## mcq_divide_type
kind: mcq
title: What kind of number is 10 / 5?
tags: types, numbers, predict
difficulty: easy
answer: 3

### prompt
What does this print?

    print(type(10 / 5))

Notes

- `10 / 5` is exactly 2, with nothing left over.

### walkthrough
Almost everyone picks `<class 'int'>` here, and the reasoning is sensible: 10 divided by 5 is 2, and 2 is a whole number. But Python does not decide the type by looking at the answer. It decides by looking at the operator.

The `/` operator is *true division*, and it always produces a float — every single time, no exceptions. `10 / 5` is `2.0`, not `2`. Print it and you will see the `.0` sitting right there.

    print(10 / 5)        →  2.0
    print(type(10 / 5))  →  <class 'float'>

Read those two lines carefully, because they are different questions. `2.0` is the *value*. `<class 'float'>` is what `type()` hands back when you ask what kind of thing that value is. If you picked `2.0`, you answered `print(10 / 5)` — you dropped the `type()` on the way past.

If you want the int, that is a different operator: `10 // 5` is floor division and gives `2` as an int. This matters more than it looks. The day you use a divided value as a list index, `scores[len(scores) / 2]` will crash with a "list indices must be integers" error, and you will stare at it wondering why — the value looked like a whole number. It was a float the whole time.

### choices
- <class 'int'>
- 2.0
- <class 'float'>
- Nothing — it raises an error

---

## count_digits
kind: code_fn
title: How long is that ticket number?
tags: types, strings, numbers
difficulty: easy
entry: count_digits

### prompt
A raffle ticket number arrives as a whole number. Return how many digits it has.

Examples

    count_digits(4021) → 4
    count_digits(7) → 1
    count_digits(100000) → 6

Notes

- You cannot call `len()` on an int, but you can call it on a string.
- Ticket numbers are zero or positive.
- Don't forget to return the result.

### starter
```python
def count_digits(number):
    pass
```

### solution
```python
def count_digits(number):
    return len(str(number))
```

### check
count_digits(4021) == 4
count_digits(7) == 1
count_digits(100000) == 6
count_digits(0) == 1

---

## written_float_equality
kind: written
title: Why isn't 0.1 + 0.2 equal to 0.3?
tags: types, numbers, written
difficulty: easy

### prompt
Explain this result in one or two sentences:

    print(0.1 + 0.2 == 0.3)

Python prints `False`. Here is the clue you need:

    print(0.1 + 0.2)  →  0.30000000000000004

Explain why the addition produces that number, and why it makes the `==` comparison `False`.

Notes

- No code needed — plain English.
- Say something about how Python stores decimal numbers.
- Nothing is broken and this is not a Python bug; every language that stores decimals this way does the same thing.

---

## same_type_check
kind: code_fn
title: Same kind of thing?
tags: types, logic, conditions
difficulty: easy
entry: same_type_check

### prompt
A quiz app stores two answers and wants to know whether they are the same *kind* of value — not whether they are equal, but whether they are the same type. Return `True` if they are, `False` otherwise.

Examples

    same_type_check(1, 2) → True
    same_type_check(1, "2") → False
    same_type_check("a", "b") → True

Notes

- `type(x)` tells you what kind of value `x` is; two types can be compared with `==`.
- `1` and `1.0` look equal, but they are not the same type.
- Don't forget to return the result.

### starter
```python
def same_type_check(a, b):
    pass
```

### solution
```python
def same_type_check(a, b):
    return type(a) == type(b)
```

### check
same_type_check(1, 2) is True
same_type_check(1, "2") is False
same_type_check("a", "b") is True
same_type_check(1, 1.0) is False
same_type_check(3.5, 0.0) is True

---

## tip_total_bug
kind: code_fn
title: The tip that made the bill huge
tags: bugs, types, numbers
difficulty: medium
entry: total_paid

### prompt
`total_paid` is supposed to take a bill and a tip, each typed in as text, and return what was paid in total as a number. Instead, a $20 bill with a $3 tip comes back as the string `"203"` instead of the number `23.0`. Fix it.

Examples

    total_paid("20", "3") → 23.0
    total_paid("12.50", "2.50") → 15.0
    total_paid("0", "0") → 0.0

Notes

- Notice that the broken version does not crash — it happily returns a wrong answer.
- Return a number, not a string.

### walkthrough
The scary part of this bug is that nothing goes wrong. No error, no traceback, no red text. `"20" + "3"` is a perfectly legal Python expression — `+` on two strings means "glue them together", so you get `"203"`. The code did exactly what you told it to; you just told it the wrong thing.

This is why the type of a value matters even when it looks like a number. Anything a user types, anything read out of a file, anything from `input()` — it is text until you convert it. `"20"` is not 20.

The fix is to convert each piece before adding:

    return float(bill_text) + float(tip_text)

One more trap: don't write `float(bill_text + tip_text)`. That glues first and converts second, giving you `203.0` — the same wrong answer, now wearing a decimal point. Convert each string on its own, then add.

Why `float` and not `int`? Because `int("12.50")` raises an error — `int()` refuses text that has a decimal point in it. `float` handles both `"20"` and `"12.50"`, which is why `total_paid("20", "3")` gives `23.0` and not `23`.

### starter
```python
def total_paid(bill_text, tip_text):
    return bill_text + tip_text
```

### solution
```python
def total_paid(bill_text, tip_text):
    return float(bill_text) + float(tip_text)
```

### check
total_paid("20", "3") == 23.0
total_paid("12.50", "2.50") == 15.0
total_paid("0", "0") == 0.0
total_paid("100", "0") == 100.0
total_paid("5.25", "0.75") == 6.0

---

## scores_with_blanks
kind: code_fn
title: Some judges left it blank
tags: types, arrays, loops
difficulty: medium
entry: scores_with_blanks

### prompt
A panel of judges typed their scores into a form, so they arrive as a list of strings. A judge who skipped the round left the box empty, which shows up as `""`. Return a list of whole numbers, counting every blank as `0`.

Examples

    scores_with_blanks(["8", "9", ""]) → [8, 9, 0]
    scores_with_blanks(["", ""]) → [0, 0]
    scores_with_blanks(["10"]) → [10]

Notes

- `int("")` raises an error, so you have to handle the blank before converting.
- Return a new list — don't print it.
- Stuck? Hit "Show me how".

### walkthrough
Try it the obvious way first and watch it break:

    int("")

Python says `ValueError: invalid literal for int() with base 10: ''`. There is no
number in an empty string, so there is nothing for `int()` to convert. That means
you have to deal with the blank *before* you convert, not after.

So each score needs a decision: did the judge type something, or not? Build the
answer up one item at a time:

    result = []
    for s in scores:
        if s:
            result.append(int(s))
        else:
            result.append(0)
    return result

The `if s` line is the interesting part. You might expect to need `if s != ""`,
and that works — but Python already treats an empty string as False and any
non-empty string as True, so `if s` says the same thing. That's worth knowing,
because you'll see it constantly in other people's code.

Note `result = []` sits *above* the loop. Put it inside and you'd start a fresh
empty list on every pass and return a list holding only the last score.

### starter
```python
def scores_with_blanks(scores):
    pass
```

### solution
```python
def scores_with_blanks(scores):
    return [int(s) if s else 0 for s in scores]
```

### check
scores_with_blanks(["8", "9", ""]) == [8, 9, 0]
scores_with_blanks(["", ""]) == [0, 0]
scores_with_blanks(["10"]) == [10]
scores_with_blanks([]) == []
scores_with_blanks(["7", "0", "", "3"]) == [7, 0, 0, 3]
