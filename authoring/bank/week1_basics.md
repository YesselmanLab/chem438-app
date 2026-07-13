# Week 1 — the basics (variables, arithmetic, functions)

Each problem: a `## id` header, `key: value` lines, then `### prompt`,
`### starter`, `### solution`, `### check`. Checks must pass against the
solution (build fails otherwise) and also define the grading tests. MCQ
`answer:` is 1-based.

---

## sum_total
kind: code_var
title: Sum two variables
tags: arithmetic, variables, week1
entry: total

### prompt
Create a variable `a` equal to 7 and `b` equal to 5, then store their sum in a variable `total`.

### starter
```python
a = 
b = 
total = 
```

### solution
```python
a = 7
b = 5
total = a + b
```

### check
total == 12

---

## remainder_mod
kind: code_var
title: Remainder with %
tags: arithmetic, operators, week1
entry: rem

### prompt
Store the remainder of 17 divided by 5 in a variable `rem` (use the % operator).

### starter
```python
rem = 
```

### solution
```python
rem = 17 % 5
```

### check
rem == 2

---

## double_fix
kind: code_fn
title: Fix the double function
tags: functions, debug, week1
entry: double

### prompt
Fix the bug: `double` should return its input doubled.

### starter
```python
def double(x):
    return x + 2      # <-- wrong, fix it
```

### solution
```python
def double(x):
    return x * 2
```

### check
double(4) == 8
double(10) == 20
double(0) == 0
double(7) == 14
double(25) == 50

---

## area_rect
kind: code_fn
title: Rectangle area
tags: functions, arithmetic, week1
entry: area

### prompt
Write a function `area(length, width)` that returns the area of a rectangle.

### starter
```python
def area(length, width):
    
```

### solution
```python
def area(length, width):
    return length * width
```

### check
area(3, 4) == 12
area(5, 5) == 25
area(2, 10) == 20
area(7, 3) == 21
area(1, 9) == 9

---

## is_even
kind: code_fn
title: is_even
tags: functions, logic, week1
entry: is_even

### prompt
Write a function `is_even(n)` that returns True if n is even, False otherwise.

### starter
```python
def is_even(n):
    
```

### solution
```python
def is_even(n):
    return n % 2 == 0
```

### check
is_even(4) is True
is_even(7) is False
is_even(0) is True
is_even(3) is False
is_even(10) is True
is_even(1) is False

---

## mcq_str_plus_int
kind: mcq
title: What's wrong — text + number
tags: concept, debug, types, week1
answer: 2

### prompt
What is wrong with this code?

    print("Total: " + 5)

### choices
- Nothing — it prints  Total: 5
- You can't join text and a number with + — the 5 must be str(5)
- print is spelled wrong
- It needs another set of parentheses

---

## mcq_floor_div
kind: mcq
title: Predict — 7 // 2
tags: concept, predict, operators, week1
answer: 2

### prompt
What does this print?

    print(7 // 2)

### choices
- 3.5
- 3
- 3.0
- 1

---

## written_plus_vs_star_hello
kind: written
title: Explain — hello + 2 vs hello * 2
tags: concept, written, types, week1

### prompt
Why does  "hello" + 2  cause an error, but  "hello" * 2  works fine? (One or two sentences.)
