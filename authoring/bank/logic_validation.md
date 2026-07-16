# Logic & validation — returning True/False

Problems whose answer is a boolean. The recurring lesson: a comparison like
`n <= 0` is *already* True or False, so you return it directly — no if/else needed.

---

## divisible_by_five
kind: code_fn
title: Check if an integer is divisible by five
tags: math, numbers, validation, week1
difficulty: easy
entry: divisible_by_five

### prompt
Create a function that returns True if an integer is evenly divisible by 5, and
False otherwise.

Examples

    divisible_by_five(5) → True
    divisible_by_five(-55) → True
    divisible_by_five(37) → False

Notes

- Don't forget to `return` the result.

### walkthrough
"Evenly divisible by 5" means dividing by 5 leaves no remainder. The `%` operator
gives you the remainder, so the question is whether `n % 5` is 0:

    def divisible_by_five(num):
        return num % 5 == 0

Note what you *don't* need. This works, but it's clumsy:

    if num % 5 == 0:
        return True
    else:
        return False

`num % 5 == 0` is already True or False on its own — the if/else just takes that
answer and laboriously restates it. Return the comparison directly. You'll use
this move on every problem in this file.

### starter
```python
def divisible_by_five(num):
    
```

### solution
```python
def divisible_by_five(num):
    return num % 5 == 0
```

### check
divisible_by_five(5) is True
divisible_by_five(-55) is True
divisible_by_five(37) is False
divisible_by_five(0) is True
divisible_by_five(1) is False
divisible_by_five(100) is True

---

## less_than_or_equal_to_zero
kind: code_fn
title: Is the number less than or equal to zero?
tags: conditions, language_fundamentals, validation, week1
difficulty: easy
entry: less_than_or_equal_to_zero

### prompt
Create a function that takes a number as its only argument and returns True if
it's less than or equal to zero, otherwise return False.

Examples

    less_than_or_equal_to_zero(5) → False
    less_than_or_equal_to_zero(0) → True
    less_than_or_equal_to_zero(-2) → True

Notes

- Don't forget to `return` the result.

### starter
```python
def less_than_or_equal_to_zero(num):
    
```

### solution
```python
def less_than_or_equal_to_zero(num):
    return num <= 0
```

### check
less_than_or_equal_to_zero(5) is False
less_than_or_equal_to_zero(0) is True
less_than_or_equal_to_zero(-2) is True
less_than_or_equal_to_zero(1) is False
less_than_or_equal_to_zero(-100) is True

---

## is_same_num
kind: code_fn
title: Are the numbers equal?
tags: conditions, language_fundamentals, numbers, validation, week1
difficulty: easy
entry: is_same_num

### prompt
Create a function that returns True when `num1` is equal to `num2`; otherwise
return False.

Examples

    is_same_num(4, 8) → False
    is_same_num(2, 2) → True
    is_same_num(2, "2") → False

Notes

- Look closely at that third example.
- Don't forget to `return` the result.

### walkthrough
The answer is short:

    def is_same_num(num1, num2):
        return num1 == num2

The interesting part is the third example. Why is 2 == "2" False? Because the
number 2 and the text "2" are different types of thing, and Python never quietly
converts one into the other to make a comparison succeed. They look alike printed
on screen; they are not alike.

Also mind the difference between `=` and `==`. A single `=` assigns a value; a
double `==` asks a question. Writing `num1 = num2` here would be a bug.

### starter
```python
def is_same_num(num1, num2):
    
```

### solution
```python
def is_same_num(num1, num2):
    return num1 == num2
```

### check
is_same_num(4, 8) is False
is_same_num(2, 2) is True
is_same_num(2, "2") is False
is_same_num(0, 0) is True
is_same_num(-5, 5) is False

---

## less_than_100
kind: code_fn
title: Less than 100?
tags: language_fundamentals, math, validation, week1
difficulty: easy
entry: less_than_100

### prompt
Given two numbers, return True if the sum of both numbers is less than 100.
Otherwise return False.

Examples

    less_than_100(22, 15) → True     # 22 + 15 = 37
    less_than_100(83, 34) → False    # 83 + 34 = 117
    less_than_100(3, 77) → True

Notes

- Don't forget to `return` the result.

### starter
```python
def less_than_100(a, b):
    
```

### solution
```python
def less_than_100(a, b):
    return a + b < 100
```

### check
less_than_100(22, 15) is True
less_than_100(83, 34) is False
less_than_100(3, 77) is True
less_than_100(50, 50) is False
less_than_100(0, 0) is True

---

## makes10
kind: code_fn
title: Two makes ten
tags: algorithms, conditions, validation, week1
difficulty: medium
entry: makes10

### prompt
Create a function that takes two arguments. Both arguments are integers, `a` and
`b`. Return True if one of them is 10 or if their sum is 10.

Examples

    makes10(9, 10) → True
    makes10(9, 9) → False
    makes10(1, 9) → True

Notes

- Don't forget to `return` the result.

### walkthrough
Three separate ways to win, and any one of them is enough. That's what `or` means:

    def makes10(a, b):
        return a == 10 or b == 10 or a + b == 10

`or` is True when at least one side is True. (Its counterpart `and` needs every
side to be True.)

One trap: you must write out `a == 10 or b == 10`. The English sentence "if a or b
is 10" shortens nicely, but `a or b == 10` is not the same thing to Python and
will give wrong answers. Each comparison needs its own complete statement.

### starter
```python
def makes10(a, b):
    
```

### solution
```python
def makes10(a, b):
    return a == 10 or b == 10 or a + b == 10
```

### check
makes10(9, 10) is True
makes10(9, 9) is False
makes10(1, 9) is True
makes10(10, 0) is True
makes10(3, 4) is False
makes10(5, 5) is True

---

## profitable_gamble
kind: code_fn
title: Profitable gamble
tags: conditions, math, validation, week1
difficulty: medium
entry: profitable_gamble

### prompt
Create a function that takes three arguments `prob`, `prize`, `pay` and returns
True if prob * prize > pay; otherwise return False.

To illustrate:

    profitable_gamble(0.2, 50, 9)

... should yield True, since the net profit is 1 (0.2 * 50 - 9), and 1 > 0.

Examples

    profitable_gamble(0.2, 50, 9) → True
    profitable_gamble(0.9, 1, 2) → False
    profitable_gamble(0.9, 3, 2) → True

Notes

- Don't forget to `return` the result.

### starter
```python
def profitable_gamble(prob, prize, pay):
    
```

### solution
```python
def profitable_gamble(prob, prize, pay):
    return prob * prize > pay
```

### check
profitable_gamble(0.2, 50, 9) is True
profitable_gamble(0.9, 1, 2) is False
profitable_gamble(0.9, 3, 2) is True
profitable_gamble(0.5, 10, 5) is False
profitable_gamble(1.0, 10, 9) is True
