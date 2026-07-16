# Arithmetic & operators

Everyday practice with Python's number operators — `/`, `//`, `%`, `**`, and the
built-ins `abs()`, `round()`, `min()` and `max()`.

---

## thermostat_gap
kind: code_fn
title: How far off is the thermostat
tags: functions, math, numbers
difficulty: starter
entry: gap

### prompt
Write a function that takes the current `room` temperature and the `dial` setting
and returns how far apart they are. The answer must be a positive number, no
matter which one is bigger.

Examples

    gap(18, 23) → 5
    gap(23, 18) → 5
    gap(20, 20) → 0

Notes

- `abs(x)` gives the size of a number, throwing away any minus sign.
- Do the subtraction inside `abs(...)`.
- Don't forget to `return` the result.

### walkthrough
The trap here is the order of the subtraction. If you write `room - dial` you get
`-5` for a room at 18 and a dial at 23, and a distance of "negative five degrees"
is nonsense. Swapping to `dial - room` gives `5`, which looks right — but check it
against the second example, where the room is 23 and the dial is 18. Now the same
code gives `-5` and you are back where you started. There is no fixed order that
works for both.

`abs()` removes the guesswork. It takes whatever number you hand it and returns
its size without the sign:

    abs(-5)   is 5
    abs(5)    is 5

So wrap the subtraction and stop worrying about the order:

    return abs(room - dial)

That is the general habit: whenever you want "how far apart are these two
numbers", write `abs(a - b)` rather than trying to work out which one is larger
first.

### starter
```python
def gap(room, dial):
    
```

### solution
```python
def gap(room, dial):
    return abs(room - dial)
```

### check
gap(18, 23) == 5
gap(23, 18) == 5
gap(20, 20) == 0
gap(-4, 3) == 7
gap(0, 12) == 12

---

## pizza_slices_each
kind: code_var
title: Slices each
tags: math, numbers, types
difficulty: starter
entry: each

### prompt
There are 8 slices of pizza and 4 people. Use division to store how many slices
each person gets in a variable `each`.

Notes

- Use the `/` operator.
- `/` always hands you back a float, even when the division comes out even.

### starter
```python
each = 
```

### solution
```python
each = 8 / 4
```

### check
each == 2.0 and type(each) is float

---

## score_range
kind: code_fn
title: How spread out are three scores
tags: functions, math, numbers
difficulty: easy
entry: score_range

### prompt
Three friends bowled a game each. Write a function that takes their three scores
and returns the spread: the distance between the best score and the worst.

Examples

    score_range(120, 95, 100) → 25
    score_range(5, 5, 5) → 0
    score_range(0, 7, 3) → 7

Notes

- `max(a, b, c)` hands back the largest of the three; `min(a, b, c)` the smallest.
- The spread is one of those subtracted from the other.
- Don't forget to `return` the result.

### walkthrough
Read the words and turn each one into code. "The best score" is `max(a, b, c)`.
"The worst score" is `min(a, b, c)`. "The distance between them" is a subtraction.
Put those three pieces together in that order:

    return max(a, b, c) - min(a, b, c)

Try it on 120, 95, 100: the max is 120, the min is 95, and 120 - 95 is 25.

The slip to name is the order of the subtraction. If you write
`min(a, b, c) - max(a, b, c)` you get `-25`, and a spread can never be negative —
the biggest number minus the smallest is always zero or more. The check
`score_range(5, 5, 5) == 0` will not catch that mistake for you, because when all
three are equal both orders give 0. That is exactly why the other checks are
there.

Notice you do not need an `if` anywhere. Beginners often reach for a chain of
comparisons to find the biggest of three numbers; `max` and `min` already did that
work, and they take as many arguments as you like.

### starter
```python
def score_range(a, b, c):
    
```

### solution
```python
def score_range(a, b, c):
    return max(a, b, c) - min(a, b, c)
```

### check
score_range(120, 95, 100) == 25
score_range(5, 5, 5) == 0
score_range(0, 7, 3) == 7
score_range(-4, -9, -1) == 8
score_range(10, 2, 60) == 58

---

## mcq_precedence_power
kind: mcq
title: What does this print?
tags: predict, concept, math
difficulty: starter
answer: 1

### prompt
What does this print?

    print(2 + 3 * 4 ** 2)

### choices
- 50
- 80
- 400
- 26

---

## quiz_percent
kind: code_fn
title: Score as a percent
tags: functions, math, numbers
difficulty: easy
entry: quiz_percent

### prompt
Write a function that takes how many questions a student got `correct` and how
many there were in `total`, and returns their score as a percentage rounded to
the nearest whole number.

Examples

    quiz_percent(9, 10) → 90
    quiz_percent(1, 3) → 33
    quiz_percent(7, 9) → 78

Notes

- Divide, multiply by 100, then hand the result to `round()`.
- `round()` with one argument gives you a whole number back.

### walkthrough
Build this in the order the words describe it. "How much of the quiz did they
get" is a fraction — `correct / total`. For 9 out of 10 that is `0.9`.

A percent is just that fraction out of a hundred, so multiply by 100 and you get
`90.0`. Nearly there, but the examples show `90`, not `90.0`, so pass it through
`round()`:

    return round(correct / total * 100)

Here is the mistake waiting for you. It is tempting to round first and multiply
after — `round(correct / total) * 100`. Try it on 9 out of 10: `round(0.9)` is
`1`, times 100 is `100`. You just told a student who missed a question that they
got a perfect score. Rounding collapses the number to a whole one, so any detail
smaller than 1 is gone for good. Do it last, once the number is already scaled to
the size you want.

You don't need parentheses around `correct / total * 100` inside the `round(...)`
call — `/` and `*` are the same precedence and run left to right, which is
exactly the order you want.

### starter
```python
def quiz_percent(correct, total):
    
```

### solution
```python
def quiz_percent(correct, total):
    return round(correct / total * 100)
```

### check
quiz_percent(9, 10) == 90
quiz_percent(1, 3) == 33
quiz_percent(7, 9) == 78
quiz_percent(2, 7) == 29
quiz_percent(0, 5) == 0
quiz_percent(4, 4) == 100

---

## average_three_bug
kind: code_fn
title: The average is way too big
tags: bugs, math, functions
difficulty: easy
entry: average

### prompt
This function is supposed to return the average of three numbers, but the answers
come out far too large. Averaging 9, 9 and 9 should obviously give 9.0, yet it
reports 21.0. Fix it.

Examples

    average(9, 9, 9) → 9.0
    average(1, 2, 3) → 2.0
    average(10, 20, 60) → 30.0

Notes

- `/` happens before `+`, so only the last number is being divided.
- One pair of parentheses is all you need.

### walkthrough
Run the broken version by hand on `average(9, 9, 9)`. Python does not read the
line left to right the way you do — it does division before addition. So

    return a + b + c / 3

really means "9 plus 9 plus (9 divided by 3)", which is 9 + 9 + 3 = 21.0. Only
the third number ever got divided, which is why the answer is roughly three times
too big.

Parentheses let you overrule the default order. Wrap the whole sum so it is
finished before the division starts:

    return (a + b + c) / 3

Now it is (9 + 9 + 9) / 3, which is 27 / 3, which is 9.0. This is the single most
common arithmetic bug in beginner code: when you mean "add these up, then divide",
you must say so with parentheses, because Python will otherwise divide first.

### starter
```python
def average(a, b, c):
    return a + b + c / 3
```

### solution
```python
def average(a, b, c):
    return (a + b + c) / 3
```

### check
average(9, 9, 9) == 9.0
average(1, 2, 3) == 2.0
average(10, 20, 60) == 30.0
average(0, 0, 0) == 0.0
average(-3, 0, 3) == 0.0

---

## split_change
kind: code_fn
title: Quarters, dimes and leftover
tags: functions, math, numbers
difficulty: medium
entry: split_change

### prompt
You have a pile of loose change worth `cents` cents. Make it into as few coins as
possible, biggest first: take out all the whole quarters (25 cents each) you can,
then all the whole dimes (10 cents each) you can from what remains. Write a
function that returns a three-item list of the quarter count, the dime count, and
the cents still left over.

Examples

    split_change(80) → [3, 0, 5]
    split_change(95) → [3, 2, 0]
    split_change(12) → [0, 1, 2]

Notes

- `//` divides and throws away the remainder; `%` gives you that remainder back.
- The dimes do not come out of `cents` — they come out of what the quarters left
  behind.

### walkthrough
`//` and `%` are two halves of the same division, and this problem is the clearest
way to see it. Take 80 cents and pull out the quarters:

    80 // 25   is 3     (three whole quarters fit)
    80 % 25    is 5     (five cents don't fit into another quarter)

Sanity-check it: 3 quarters is 75 cents, plus the 5 left over, back to 80. The
count and the remainder always rebuild the original number.

Do not reach for `/` here. `80 / 25` is `3.2`, and "3.2 quarters" is not a thing
you can hold in your hand. When you are counting how many whole things fit, `//`
is the operator you want.

Now the part that catches people. The dimes must come out of the *remainder*, not
out of `cents`. Writing `cents // 10` for the dimes is the mistake: for 80 cents
that claims 8 dimes on top of the 3 quarters, which is 155 cents of coins out of a
pile worth 80. Once a quarter has claimed some money, that money is spent.

So give the remainder a name and keep whittling it down:

    rest = cents % 25
    return [cents // 25, rest // 10, rest % 10]

Walk 95 through it: `95 // 25` is 3, `rest` is 20, `20 // 10` is 2, `20 % 10` is 0
— `[3, 2, 0]`. Add it back up: 75 + 20 + 0 is 95. That "add it back up" check is
worth doing on every case you're unsure of.

### starter
```python
def split_change(cents):
    
```

### solution
```python
def split_change(cents):
    rest = cents % 25
    return [cents // 25, rest // 10, rest % 10]
```

### check
split_change(80) == [3, 0, 5]
split_change(95) == [3, 2, 0]
split_change(12) == [0, 1, 2]
split_change(0) == [0, 0, 0]
split_change(100) == [4, 0, 0]
split_change(49) == [1, 2, 4]

---

## clamp_volume
kind: code_fn
title: Keep the volume in range
tags: functions, math, numbers
difficulty: easy
entry: clamp_volume

### prompt
A speaker's volume dial only accepts numbers from 0 to 10. Write a function that
takes any number `v` and returns it pushed back into that range: anything below 0
becomes 0, anything above 10 becomes 10, and anything already in range comes back
unchanged.

Examples

    clamp_volume(-3) → 0
    clamp_volume(47) → 10
    clamp_volume(6) → 6

Notes

- `max()` and `min()` are both useful here — work out which one guards which end.
- `v` may be a whole number or have a decimal part; an in-range number must come
  back exactly as it went in.
- No `if` needed: one of these can be nested inside the other on a single line.

### walkthrough
Handle one end at a time. To stop the number going below 0, ask for the larger of
the number and 0:

    max(0, -3)   is 0
    max(0, 6)    is 6

That end is now safe — nothing can escape below zero. Now take that safe result
and stop it going above 10 by asking for the smaller of it and 10:

    min(10, 0)   is 0
    min(10, 6)   is 6
    min(10, 47)  is 10

Nest them and you have the whole thing:

    return min(10, max(0, v))

The mistake to name here is getting the two backwards — writing `max(0, min(10, v))`
happens to work too, but writing `min(0, max(10, v))` does not, and it is an easy
slip. Remember it as words: `max` is the floor (it raises numbers up), `min` is
the ceiling (it pushes numbers down). If the result of your version on `-3` isn't
`0`, you have them swapped.

### starter
```python
def clamp_volume(v):
    
```

### solution
```python
def clamp_volume(v):
    return min(10, max(0, v))
```

### check
clamp_volume(-3) == 0
clamp_volume(47) == 10
clamp_volume(6) == 6
clamp_volume(0) == 0
clamp_volume(10) == 10
clamp_volume(7.5) == 7.5
clamp_volume(12.4) == 10
