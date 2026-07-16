# Week 1 — the basics (variables, arithmetic, functions)

Each problem: a `## id` header, `key: value` lines, then `### prompt`,
`### starter`, `### solution`, `### check`. Checks must pass against the
solution (build fails otherwise) and also define the grading tests. MCQ
`answer:` is 1-based.

---

## hello_438
kind: code_fn
title: How challenges work
tags: language_fundamentals, strings, functions, week1
difficulty: easy
entry: hello

### prompt
Start here — this is how every challenge in this course works.

In the editor below you'll see a starter function:

    def hello():

All you have to do is type  return "hello chem 438"  on the second line, indented
four spaces, then hit Run to test it. When it passes, hit Submit.

Examples

    hello() → "hello chem 438"

Notes

- The returned string must be all lowercase.
- Run tests your code as many times as you like, and costs you nothing. Use it constantly.
- Every challenge names the function you must write and shows examples of what it
  should give back. Match those examples exactly and you pass.
- A function that computes the right answer but never says `return` gives back nothing.

Stuck on any challenge? Hit "Show me how" under the prompt for a worked example.

### walkthrough
Here's the whole process on a different problem, start to finish. Say a challenge asks:

    Write a function that takes an integer minutes and converts it to seconds.

    convert(5) → 300
    convert(3) → 180

Step 1 — read the examples, find the pattern. 5 becomes 300, and 3 becomes 180.
Both are the input times 60. That makes sense: 60 seconds in a minute.

Step 2 — write the def line. The challenge gives you the name and what goes in.
It's called convert and takes one thing, so:

    def convert(minutes):

Step 3 — return the answer. The body is indented four spaces, and it must say
`return`, or the function hands back nothing at all:

    def convert(minutes):
        return minutes * 60

Step 4 — check one example by hand. convert(5) is 5 * 60, which is 300. That
matches the first example, so hit Run.

That's every challenge: read the examples, spot the pattern, write the def line,
return the answer, test it. Now go do this one — type
return "hello chem 438" into the editor and hit Run.

### starter
```python
def hello():
    
```

### solution
```python
def hello():
    return "hello chem 438"
```

### check
hello() == "hello chem 438"

---

## addition
kind: code_fn
title: Return the sum of two numbers
tags: math, numbers, algebra, functions, week1
difficulty: easy
entry: addition

### prompt
Create a function that takes two numbers as arguments and returns their sum.

Examples

    addition(3, 2) → 5
    addition(-3, -6) → -9
    addition(7, 3) → 10

Notes

- Don't forget to `return` the result.

### starter
```python
def addition(a, b):
    
```

### solution
```python
def addition(a, b):
    return a + b
```

### check
addition(3, 2) == 5
addition(-3, -6) == -9
addition(7, 3) == 10
addition(0, 0) == 0
addition(100, -1) == 99

---

## next_num
kind: code_fn
title: Return the next number from the integer passed
tags: math, numbers, algebra, functions, week1
difficulty: easy
entry: next_num

### prompt
Create a function that takes a number as an argument, increments the number by +1
and returns the result.

Examples

    next_num(0) → 1
    next_num(9) → 10
    next_num(-3) → -2

Notes

- Don't forget to `return` the result.

### starter
```python
def next_num(num):
    
```

### solution
```python
def next_num(num):
    return num + 1
```

### check
next_num(0) == 1
next_num(9) == 10
next_num(-3) == -2
next_num(100) == 101
next_num(-1) == 0

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
