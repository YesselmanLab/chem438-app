# Math, numbers & geometry — function practice

Short "write one function" problems, in the Edabit style: a one-line task, a few
worked examples, and notes. Same rules as every bank file — the `### check` lines
must pass against the `### solution` (the build fails otherwise) and they define
the grading tests. An optional `### walkthrough` is shown behind a "Show me how"
toggle, so it helps a stuck student without spoiling the answer up front.

---

## convert_minutes
kind: code_fn
title: Convert minutes into seconds
tags: language_fundamentals, math, numbers, week1
see: 01_variables_math#the-basic-math-operators
difficulty: easy
entry: convert

### prompt
Write a function that takes an integer `minutes` and converts it to seconds.

Examples

    convert(5) → 300
    convert(3) → 180
    convert(2) → 120

Notes

- Don't forget to `return` the result.

### walkthrough
Read the examples first and find the pattern: 5 → 300, 3 → 180, 2 → 120. Each
answer is the input times 60, because there are 60 seconds in a minute.

Now write that down as a function. The problem tells you the name (`convert`) and
that it takes one thing (`minutes`):

    def convert(minutes):
        return minutes * 60

Check it against an example in your head before you hit Run: convert(5) gives
5 * 60, which is 300. That matches. Hit Run.

### starter
```python
def convert(minutes):
    
```

### solution
```python
def convert(minutes):
    return minutes * 60
```

### check
convert(5) == 300
convert(3) == 180
convert(2) == 120
convert(0) == 0
convert(1) == 60

---

## how_many_seconds
kind: code_fn
title: Convert hours into seconds
tags: language_fundamentals, math, numbers, week1
see: 01_variables_math#the-basic-math-operators
difficulty: easy
entry: how_many_seconds

### prompt
Write a function that converts `hours` into seconds.

Examples

    how_many_seconds(2) → 7200
    how_many_seconds(10) → 36000
    how_many_seconds(24) → 86400

Notes

- 60 seconds in a minute, 60 minutes in an hour.
- Don't forget to `return` your answer.

### starter
```python
def how_many_seconds(hours):
    
```

### solution
```python
def how_many_seconds(hours):
    return hours * 60 * 60
```

### check
how_many_seconds(2) == 7200
how_many_seconds(10) == 36000
how_many_seconds(24) == 86400
how_many_seconds(0) == 0
how_many_seconds(1) == 3600

---

## remainder_fn
kind: code_fn
title: Return the remainder from two numbers
tags: math, numbers, week1
see: 01_variables_math#floor-division-and-remainder-and
difficulty: easy
entry: remainder

### prompt
There is a single operator in Python capable of providing the remainder of a
division operation. Two numbers are passed as parameters. The first parameter
divided by the second parameter will have a remainder, possibly zero. Return
that value.

Examples

    remainder(1, 3) → 1
    remainder(3, 4) → 3
    remainder(5, 5) → 0
    remainder(7, 2) → 1

Notes

- The tests only use positive integers.
- Don't forget to `return` the result.

### starter
```python
def remainder(num1, num2):
    
```

### solution
```python
def remainder(num1, num2):
    return num1 % num2
```

### check
remainder(1, 3) == 1
remainder(3, 4) == 3
remainder(5, 5) == 0
remainder(7, 2) == 1
remainder(10, 3) == 1
remainder(9, 4) == 1

---

## calc_age
kind: code_fn
title: Convert age to days
tags: math, numbers, week1
see: 01_variables_math#the-basic-math-operators
difficulty: easy
entry: calc_age

### prompt
Create a function that takes the age in years and returns the age in days.

Examples

    calc_age(65) → 23725
    calc_age(0) → 0
    calc_age(20) → 7300

Notes

- Use 365 days as the length of a year for this challenge.
- Ignore leap years and days between the last birthday and now.
- Expect only positive integer inputs.

### starter
```python
def calc_age(age):
    
```

### solution
```python
def calc_age(age):
    return age * 365
```

### check
calc_age(65) == 23725
calc_age(0) == 0
calc_age(20) == 7300
calc_age(1) == 365
calc_age(100) == 36500

---

## string_int
kind: code_fn
title: Return a string as an integer
tags: language_fundamentals, numbers, strings, week1
see: 02_strings#converting-between-strings-and-numbers
difficulty: easy
entry: string_int

### prompt
Create a function that takes a string and returns it as an integer.

Examples

    string_int("6") → 6
    string_int("1000") → 1000
    string_int("12") → 12

Notes

- All numbers will be whole.
- All numbers will be positive.

### walkthrough
The text "6" and the number 6 are different things in Python — you can't do math
on the text. Python has a built-in that converts one to the other: `int()`.

    def string_int(s):
        return int(s)

The giveaway that they're different: "6" + "6" gives "66" (text glued together),
but 6 + 6 gives 12. That distinction matters constantly, so it's worth getting
straight now.

### starter
```python
def string_int(s):
    
```

### solution
```python
def string_int(s):
    return int(s)
```

### check
string_int("6") == 6
string_int("1000") == 1000
string_int("12") == 12
string_int("0") == 0
string_int("42") == 42

---

## tri_area
kind: code_fn
title: Area of a triangle
tags: geometry, math, numbers, week1
see: 01_variables_math#order-of-operations
difficulty: easy
entry: tri_area

### prompt
Write a function that takes the base and height of a triangle and returns its area.

Examples

    tri_area(3, 2) → 3
    tri_area(7, 4) → 14
    tri_area(10, 10) → 50

Notes

- The area of a triangle is: (base * height) / 2
- Don't forget to `return` the result.

### starter
```python
def tri_area(base, height):
    
```

### solution
```python
def tri_area(base, height):
    return (base * height) / 2
```

### check
tri_area(3, 2) == 3
tri_area(7, 4) == 14
tri_area(10, 10) == 50
tri_area(1, 1) == 0.5
tri_area(5, 6) == 15

---

## find_perimeter
kind: code_fn
title: Find the perimeter of a rectangle
tags: geometry, language_fundamentals, math, numbers, week1
see: 01_variables_math#order-of-operations
difficulty: easy
entry: find_perimeter

### prompt
Create a function that takes `length` and `width` and finds the perimeter of a
rectangle.

Examples

    find_perimeter(6, 7) → 26
    find_perimeter(20, 10) → 60
    find_perimeter(2, 9) → 22

Notes

- Don't forget to `return` the result.

### starter
```python
def find_perimeter(length, width):
    
```

### solution
```python
def find_perimeter(length, width):
    return 2 * (length + width)
```

### check
find_perimeter(6, 7) == 26
find_perimeter(20, 10) == 60
find_perimeter(2, 9) == 22
find_perimeter(1, 1) == 4
find_perimeter(5, 3) == 16

---

## sum_polygon
kind: code_fn
title: Sum of polygon angles
tags: math, numbers, geometry, week1
see: 01_variables_math#order-of-operations
difficulty: easy
entry: sum_polygon

### prompt
Given an n-sided regular polygon `n`, return the total sum of internal angles
(in degrees).

Examples

    sum_polygon(3) → 180
    sum_polygon(4) → 360
    sum_polygon(6) → 720

Notes

- n will always be greater than 2.
- The formula (n - 2) x 180 gives the sum of all the measures of the angles of
  an n-sided polygon.

### walkthrough
When a problem hands you the formula, your only job is to translate it into
Python. The formula is (n - 2) x 180, and x means multiply, which in Python is `*`:

    def sum_polygon(n):
        return (n - 2) * 180

Keep the parentheses. Without them Python would do n - (2 * 180) first, because
multiplication happens before subtraction — the same order-of-operations rule you
use in chemistry. sum_polygon(3) would give -357 instead of 180.

### starter
```python
def sum_polygon(n):
    
```

### solution
```python
def sum_polygon(n):
    return (n - 2) * 180
```

### check
sum_polygon(3) == 180
sum_polygon(4) == 360
sum_polygon(6) == 720
sum_polygon(5) == 540
sum_polygon(10) == 1440

---

## calculate_exponent
kind: code_fn
title: To the power of ____
tags: logic, math, numbers, week1
see: 01_variables_math#exponents
difficulty: easy
entry: calculate_exponent

### prompt
Create a function that takes a base number and an exponent number and returns the
calculation.

Examples

    calculate_exponent(5, 5) → 3125
    calculate_exponent(10, 10) → 10000000000
    calculate_exponent(3, 3) → 27

Notes

- All test inputs will be positive integers.
- Don't forget to `return` the result.

### walkthrough
Python has an operator for raising to a power: `**`. It is not `^` — that's a
different operation entirely (bitwise XOR), and using it gives you a wrong answer
rather than an error, which is the worst kind of bug.

    def calculate_exponent(base, exponent):
        return base ** exponent

Sanity check: 5 ** 5 is 5*5*5*5*5 = 3125, matching the first example. If you'd
written 5 ^ 5 you'd have silently gotten 0.

### starter
```python
def calculate_exponent(base, exponent):
    
```

### solution
```python
def calculate_exponent(base, exponent):
    return base ** exponent
```

### check
calculate_exponent(5, 5) == 3125
calculate_exponent(10, 10) == 10000000000
calculate_exponent(3, 3) == 27
calculate_exponent(2, 8) == 256
calculate_exponent(7, 1) == 7

---

## football_points
kind: code_fn
title: Football points
tags: algebra, math, numbers, week1
see: 01_variables_math#the-basic-math-operators
difficulty: easy
entry: football_points

### prompt
Create a function that takes the number of `wins`, `draws` and `losses` and
calculates the number of points a football team has obtained so far.

    wins get 3 points
    draws get 1 point
    losses get 0 points

Examples

    football_points(3, 4, 2) → 13
    football_points(5, 0, 2) → 15
    football_points(0, 0, 1) → 0

Notes

- Inputs will be numbers greater than or equal to 0.

### starter
```python
def football_points(wins, draws, losses):
    
```

### solution
```python
def football_points(wins, draws, losses):
    return wins * 3 + draws * 1
```

### check
football_points(3, 4, 2) == 13
football_points(5, 0, 2) == 15
football_points(0, 0, 1) == 0
football_points(0, 0, 0) == 0
football_points(10, 10, 10) == 40

---

## animals
kind: code_fn
title: The farm problem
tags: algorithms, language_fundamentals, math, week1
see: 01_variables_math#the-basic-math-operators
difficulty: easy
entry: animals

### prompt
In this challenge, a farmer is asking you to tell him how many legs can be counted
among all his animals. The farmer breeds three species:

    chickens = 2 legs
    cows = 4 legs
    pigs = 4 legs

The farmer has counted his animals and gives you a subtotal for each species. You
have to implement a function that returns the total number of legs of all the animals.

Examples

    animals(2, 3, 5) → 36
    animals(1, 2, 3) → 22
    animals(5, 2, 8) → 50

Notes

- Don't forget to `return` the result.
- The order of animals passed is animals(chickens, cows, pigs).
- Remember that the farmer wants to know the total number of legs and not the
  total number of animals.

### starter
```python
def animals(chickens, cows, pigs):
    
```

### solution
```python
def animals(chickens, cows, pigs):
    return chickens * 2 + cows * 4 + pigs * 4
```

### check
animals(2, 3, 5) == 36
animals(1, 2, 3) == 22
animals(5, 2, 8) == 50
animals(0, 0, 0) == 0
animals(1, 0, 0) == 2

---

## next_edge
kind: code_fn
title: Maximum edge of a triangle
tags: algorithms, math, numbers, week1
see: 01_variables_math#the-basic-math-operators
difficulty: medium
entry: next_edge

### prompt
Create a function that finds the maximum range of a triangle's third edge, where
the side lengths are all integers.

Examples

    next_edge(8, 10) → 17
    next_edge(5, 7) → 11
    next_edge(9, 2) → 10

Notes

- (side1 + side2) - 1 = maximum range of third edge.
- The side lengths of the triangle are positive integers.
- Don't forget to `return` the result.

### starter
```python
def next_edge(side1, side2):
    
```

### solution
```python
def next_edge(side1, side2):
    return side1 + side2 - 1
```

### check
next_edge(8, 10) == 17
next_edge(5, 7) == 11
next_edge(9, 2) == 10
next_edge(1, 1) == 1
next_edge(100, 3) == 102
