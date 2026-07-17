# Functions — more practice

More predict-the-output, what's-wrong, conceptual, and write-a-function drills on defining and calling functions.

---

## g2_print_f3f4
kind: mcq
title: Predict — adding two calls
tags: predict, functions
difficulty: easy
answer: 1

### prompt
What does this print?

    def f(x):
        return x * 2

    print(f(3) + f(4))

### code
def f(x):
    return x * 2

print(f(3) + f(4))
### choices
- 14
- 68
- 6 8
- 7

---

## g2_print_vs_return_none
kind: mcq
title: Predict — it prints, then returns
tags: predict, functions
difficulty: easy
answer: 2

### prompt
What does this print?

    def f(x):
        print(x * 2)

    print(f(3))

### code
def f(x):
    print(x * 2)

print(f(3))
### choices
- 6
- 6\nNone
- None\n6
- 6\n6

---

## g2_g_prints_hi_none
kind: mcq
title: Predict — hi then what?
tags: predict, functions
difficulty: easy
answer: 3

### prompt
What does this print?

    def g():
        print("hi")

    x = g()
    print(x)

### code
def g():
    print("hi")

x = g()
print(x)
### choices
- hi
- hi\nhi
- hi\nNone
- None\nhi

---

## g2_default_two_ways
kind: mcq
title: Predict — a default called two ways
tags: predict, functions
difficulty: easy
answer: 1

### prompt
What does this print?

    def greet(name, greeting="Hi"):
        return greeting + ", " + name

    print(greet("Sam"))
    print(greet("Sam", "Yo"))

### code
def greet(name, greeting="Hi"):
    return greeting + ", " + name

print(greet("Sam"))
print(greet("Sam", "Yo"))
### choices
- Hi, Sam\nYo, Sam
- Hi, Sam\nHi, Sam
- Yo, Sam\nHi, Sam
- Hi, Sam

---

## g2_code_after_return
kind: mcq
title: Predict — code after return
tags: predict, functions
difficulty: easy
answer: 1

### prompt
What does this print?

    def f(x):
        return x
        print("done")

    print(f(5))

### code
def f(x):
    return x
    print("done")

print(f(5))
### choices
- 5
- done\n5
- 5\ndone
- done

---

## g2_multiple_returns
kind: mcq
title: Predict — which return fires?
tags: predict, functions
difficulty: easy
answer: 2

### prompt
What does this print?

    def describe(n):
        if n > 10:
            return "big"
        if n > 5:
            return "medium"
        return "small"

    print(describe(8))

### code
def describe(n):
    if n > 10:
        return "big"
    if n > 5:
        return "medium"
    return "small"

print(describe(8))
### choices
- big
- medium
- small
- medium\nsmall

---

## g2_call_from_call
kind: mcq
title: Predict — one function calls another
tags: predict, functions
difficulty: easy
answer: 1

### prompt
What does this print?

    def area(w, h):
        return w * h

    def label(w, h):
        return "area=" + str(area(w, h))

    print(label(2, 3))

### code
def area(w, h):
    return w * h

def label(w, h):
    return "area=" + str(area(w, h))

print(label(2, 3))
### choices
- area=6
- area=23
- 6
- area=w*h

---

## g2_nested_calls
kind: mcq
title: Predict — a function calling itself's helper
tags: predict, functions
difficulty: medium
answer: 3

### prompt
What does this print?

    def add1(x):
        return x + 1

    def add3(x):
        return add1(add1(add1(x)))

    print(add3(0))

### code
def add1(x):
    return x + 1

def add3(x):
    return add1(add1(add1(x)))

print(add3(0))
### choices
- 1
- 0
- 3
- 111

---

## g2_reassign_param
kind: mcq
title: Predict — does the caller's number change?
tags: predict, functions
difficulty: medium
answer: 1

### prompt
What does this print?

    def f(x):
        x = x + 1
        return x

    n = 10
    print(f(n))
    print(n)

### code
def f(x):
    x = x + 1
    return x

n = 10
print(f(n))
print(n)
### choices
- 11\n10
- 11\n11
- 10\n11
- 11

---

## g2_return_stops_loop
kind: mcq
title: Predict — return inside a loop
tags: predict, functions
difficulty: medium
answer: 3

### prompt
What does this print?

    def first_even(nums):
        for n in nums:
            if n % 2 == 0:
                return n
        return -1

    print(first_even([1, 3, 4, 7, 8]))

### code
def first_even(nums):
    for n in nums:
        if n % 2 == 0:
            return n
    return -1

print(first_even([1, 3, 4, 7, 8]))
### choices
- 8
- -1
- 4
- 4\n8

---

## g2_return_two_values
kind: mcq
title: Predict — returning two things
tags: predict, functions
difficulty: medium
answer: 2

### prompt
What does this print?

    def stats(a, b):
        return a + b, a * b

    print(stats(2, 3))

### code
def stats(a, b):
    return a + b, a * b

print(stats(2, 3))
### choices
- 5 6
- (5, 6)
- (6, 5)
- 5, 6

---

## g2_print_then_return
kind: mcq
title: Predict — print inside, print outside
tags: predict, functions
difficulty: easy
answer: 1

### prompt
What does this print?

    def f(x):
        print("in")
        return x

    print(f(9))

### code
def f(x):
    print("in")
    return x

print(f(9))
### choices
- in\n9
- 9
- in
- 9\nin

---

## g2_fix_print_not_return
kind: code_fn
title: It prints the answer instead of returning it
tags: functions, bugs
difficulty: starter
entry: triple

### prompt
This function is supposed to hand back three times its input, but callers keep getting None. Fix it.

    n = triple(2)
    print(n + 1)     # crashes: None + 1

Examples

    triple(2) → 6
    triple(0) → 0
    triple(5) → 15

Notes

- print shows a value on the screen; it does not hand the value back to the caller.
- Only one word needs to change.

### starter
```python
def triple(x):
    print(x * 3)
```

### solution
```python
def triple(x):
    return x * 3
```

### check
triple(2) == 6
triple(0) == 0
triple(5) == 15
triple(-3) == -9

---

## g2_fix_missing_return
kind: code_fn
title: The sum never comes back
tags: functions, bugs
difficulty: starter
entry: add

### prompt
This function computes the total but forgets to hand it back, so every call gives None. Fix it.

Examples

    add(2, 3) → 5
    add(10, 0) → 10
    add(-1, 1) → 0

Notes

- Computing a value into a local variable is not the same as returning it.
- Add one line so the function returns total.

### starter
```python
def add(a, b):
    total = a + b
```

### solution
```python
def add(a, b):
    total = a + b
    return total
```

### check
add(2, 3) == 5
add(10, 0) == 10
add(-1, 1) == 0
add(100, 100) == 200

---

## g2_fix_return_in_loop
kind: code_fn
title: The counter quits after the first item
tags: functions, bugs
difficulty: medium
entry: count_positives

### prompt
This function should count how many numbers in the list are greater than zero, but it keeps returning too early. Fix it.

Examples

    count_positives([1, 2, 3]) → 3
    count_positives([-1, 2, -3]) → 1
    count_positives([]) → 0

Notes

- A return inside the loop stops the whole function the first time it runs.
- The return that hands back the count belongs after the loop, not inside it.

### starter
```python
def count_positives(nums):
    count = 0
    for n in nums:
        if n > 0:
            count += 1
            return count
    return count
```

### solution
```python
def count_positives(nums):
    count = 0
    for n in nums:
        if n > 0:
            count += 1
    return count
```

### check
count_positives([1, 2, 3]) == 3
count_positives([-1, 2, -3]) == 1
count_positives([]) == 0
count_positives([5]) == 1

---

## g2_fix_default_order
kind: code_fn
title: The default is in the wrong place
tags: functions, bugs
difficulty: medium
entry: greet

### prompt
This function will not even define — Python rejects the header. Fix the parameter order so the greeting is optional and defaults to "Hi".

Examples

    greet("Sam") → "Hi, Sam"
    greet("Sam", "Yo") → "Yo, Sam"

Notes

- Once a parameter has a default, every parameter after it must also have one.
- Put the required parameter first and the one with a default last.

### starter
```python
def greet(greeting="Hi", name):
    return greeting + ", " + name
```

### solution
```python
def greet(name, greeting="Hi"):
    return greeting + ", " + name
```

### check
greet("Sam") == "Hi, Sam"
greet("Sam", "Yo") == "Yo, Sam"
greet("Al") == "Hi, Al"
greet("Al", "Hey") == "Hey, Al"

---

## g2_wrong_missing_colon
kind: mcq
title: What is wrong — the def line
tags: bugs, functions
difficulty: easy
answer: 2

### prompt
This code will not run. What is wrong?

    def f(x)
        return x * 2

### choices
- x is not defined
- The def line is missing a colon at the end
- A function cannot multiply its argument
- return must come before def

---

## g2_wrong_print_then_use
kind: mcq
title: What is wrong — result * 2 crashes
tags: bugs, functions
difficulty: medium
answer: 1

### prompt
This program crashes on the last line. What is the real cause?

    def area(w, h):
        print(w * h)

    result = area(3, 4)
    print(result * 2)

### choices
- area prints instead of returning, so result is None and None * 2 fails
- You cannot multiply two numbers inside a function
- area needs three arguments, not two
- print(result * 2) should be print(result + 2)

---

## g2_wrong_arg_count
kind: mcq
title: What is wrong — one argument
tags: bugs, functions
difficulty: easy
answer: 3

### prompt
This code raises an error. What is wrong?

    def add(a, b):
        return a + b

    print(add(5))

### choices
- add is missing a return statement
- a and b were never given default values, which is required
- add is called with one argument but needs two
- You cannot print the result of a function

---

## g2_wrong_call_before_def
kind: mcq
title: What is wrong — call comes first
tags: bugs, functions
difficulty: medium
answer: 2

### prompt
This program raises a NameError. What is wrong?

    print(greet("Sam"))

    def greet(name):
        return "Hi, " + name

### choices
- greet is missing a return statement
- greet is called before it is defined, so the name does not exist yet
- A function cannot take a string as an argument
- You must call greet twice for it to work

---

## g2_concept_return_vs_print
kind: mcq
title: Concept — return vs print
tags: concept, functions
difficulty: easy
answer: 3

### prompt
What is the real difference between return and print inside a function?

### choices
- There is no difference; they do the same thing
- print hands a value back to the caller; return only shows it on the screen
- return hands a value back to the caller; print only shows it on the screen
- return can only be used with numbers, print only with text

---

## g2_concept_param_vs_arg
kind: mcq
title: Concept — parameter vs argument
tags: concept, functions
difficulty: easy
answer: 1

### prompt
Given this definition and call, which statement is correct?

    def f(x):
        return x + 1

    f(5)

### choices
- x is the parameter; 5 is the argument
- 5 is the parameter; x is the argument
- Both x and 5 are parameters
- Both x and 5 are arguments

---

## g2_concept_what_is_none
kind: mcq
title: Concept — what a function with no return gives back
tags: concept, functions
difficulty: easy
answer: 2

### prompt
A function runs to the end without ever hitting a return statement. What value does the call hand back?

### choices
- 0
- None
- An empty string ""
- It raises an error

---

## g2_concept_def_runs
kind: mcq
title: Concept — does defining run it?
tags: concept, functions
difficulty: easy
answer: 3

### prompt
When Python reads a `def` statement, what happens?

### choices
- It runs the function body once immediately
- It runs the body and prints whatever the function returns
- It defines the function but does not run the body until the function is called
- It causes an error unless the function is called on the same line

---

## g2_concept_local_variable
kind: mcq
title: Concept — a variable made inside a function
tags: concept, functions
difficulty: easy
answer: 2

### prompt
A variable is created inside a function's body. Which statement is true?

### choices
- It can be used anywhere in the program after the function is defined
- It exists only inside that function and cannot be used outside it
- It replaces any variable with the same name outside the function
- It is automatically printed when the function is called

---

## g2_concept_which_is_call
kind: mcq
title: Concept — which one actually calls it?
tags: concept, functions
difficulty: easy
answer: 4

### prompt
You have a function named `double`. Which of these actually calls it with the value 5?

### choices
- double
- def double(5)
- return double
- double(5)

---

## g2_make_greeting
kind: code_fn
title: Write a greeting
tags: functions
difficulty: starter
entry: make_greeting

### prompt
Write a function that takes a name and returns a greeting: the word "Hello", a comma and a space, the name, then an exclamation mark.

Examples

    make_greeting("Sam") → "Hello, Sam!"
    make_greeting("Ada") → "Hello, Ada!"

Notes

- Return the string; do not print it.
- Join the pieces with + , and do not forget the "!" at the end.

### starter
```python
def make_greeting(name):
    pass
```

### solution
```python
def make_greeting(name):
    return "Hello, " + name + "!"
```

### check
make_greeting("Sam") == "Hello, Sam!"
make_greeting("Ada") == "Hello, Ada!"
make_greeting("Bo") == "Hello, Bo!"
make_greeting("") == "Hello, !"

---

## g2_final_price
kind: code_fn
title: Price after a coupon
tags: functions
difficulty: easy
entry: final_price

### prompt
Write a function that returns the price after subtracting a coupon amount. The coupon should be optional: if the caller does not pass one, no discount is applied.

Examples

    final_price(10) → 10
    final_price(10, 3) → 7
    final_price(20, 20) → 0

Notes

- Give the coupon parameter a default value so it is optional.
- With no coupon, the price comes back unchanged.

### starter
```python
def final_price(price, coupon=0):
    pass
```

### solution
```python
def final_price(price, coupon=0):
    return price - coupon
```

### check
final_price(10) == 10
final_price(10, 3) == 7
final_price(20, 20) == 0
final_price(5) == 5

---

## g2_is_adult
kind: code_fn
title: Is this person an adult?
tags: functions, logic
difficulty: easy
entry: is_adult

### prompt
Write a function that returns True when an age is 18 or more, and False otherwise.

Examples

    is_adult(18) → True
    is_adult(17) → False
    is_adult(21) → True

Notes

- A comparison already produces True or False, so you do not need an if statement.
- "18 or more" includes exactly 18.

### starter
```python
def is_adult(age):
    pass
```

### solution
```python
def is_adult(age):
    return age >= 18
```

### check
is_adult(18) is True
is_adult(17) is False
is_adult(21) is True
is_adult(0) is False

---

## g2_bigger
kind: code_fn
title: Return the bigger of two
tags: functions
difficulty: easy
entry: bigger

### prompt
Write a function that returns the larger of two numbers. If they are equal, return that value.

Examples

    bigger(3, 5) → 5
    bigger(9, 2) → 9
    bigger(4, 4) → 4

Notes

- Use an if to return one value, and a plain return for the other case.
- Do not print — return the number.

### starter
```python
def bigger(a, b):
    pass
```

### solution
```python
def bigger(a, b):
    if a > b:
        return a
    return b
```

### check
bigger(3, 5) == 5
bigger(9, 2) == 9
bigger(4, 4) == 4
bigger(-1, -5) == -1

---

## g2_total_area
kind: code_fn
title: Total area of two rectangles
tags: functions
difficulty: medium
entry: total_area

### prompt
You are given area(w, h), which returns the area of one rectangle. Write total_area(w1, h1, w2, h2) that returns the combined area of two rectangles by calling area twice.

Examples

    total_area(2, 3, 4, 5) → 26
    total_area(1, 1, 1, 1) → 2
    total_area(0, 5, 2, 2) → 4

Notes

- Call area for each rectangle instead of multiplying by hand.
- Add the two results together and return the sum.

### starter
```python
def area(w, h):
    return w * h

def total_area(w1, h1, w2, h2):
    pass
```

### solution
```python
def area(w, h):
    return w * h

def total_area(w1, h1, w2, h2):
    return area(w1, h1) + area(w2, h2)
```

### check
total_area(2, 3, 4, 5) == 26
total_area(1, 1, 1, 1) == 2
total_area(0, 5, 2, 2) == 4
total_area(10, 1, 0, 0) == 10

---

## g2_initials
kind: code_fn
title: Build the initials
tags: functions, strings
difficulty: easy
entry: initials

### prompt
Write a function that takes a first name and a last name and returns their two initials joined together: the first letter of each name.

Examples

    initials("Ada", "Lovelace") → "AL"
    initials("Sam", "Ray") → "SR"

Notes

- The first character of a string s is s[0].
- Join the two letters with + and return the result.

### starter
```python
def initials(first, last):
    pass
```

### solution
```python
def initials(first, last):
    return first[0] + last[0]
```

### check
initials("Ada", "Lovelace") == "AL"
initials("Sam", "Ray") == "SR"
initials("bo", "kim") == "bk"
initials("Q", "Z") == "QZ"
