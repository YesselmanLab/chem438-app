# Lists — indexing and built-ins

First contact with lists: getting an element out by position, and letting Python's
built-ins do the searching for you.

---

## get_first_value
kind: code_fn
title: Return the first element in a list
tags: arrays, language_fundamentals, week2
see: 06_lists#indexing-getting-one-item-out
difficulty: easy
entry: get_first_value

### prompt
Create a function that takes a list containing only numbers and returns the first
element.

Examples

    get_first_value([1, 2, 3]) → 1
    get_first_value([80, 5, 100]) → 80
    get_first_value([-500, 0, 50]) → -500

Notes

- The first element in a list always has an index of 0.

### walkthrough
Pull an item out of a list by putting its position in square brackets after the
list. Positions start at 0, not 1 — so the first item is at index 0:

    def get_first_value(lst):
        return lst[0]

Counting from zero feels wrong for about a week and then never bothers you again.
It's worth saying the indexes out loud once: in [80, 5, 100], the 80 is at index
0, the 5 at index 1, the 100 at index 2.

### starter
```python
def get_first_value(lst):
    
```

### solution
```python
def get_first_value(lst):
    return lst[0]
```

### check
get_first_value([1, 2, 3]) == 1
get_first_value([80, 5, 100]) == 80
get_first_value([-500, 0, 50]) == -500
get_first_value([42]) == 42
get_first_value([7, 7, 7]) == 7

---

## find_largest_num
kind: code_fn
title: Find the largest number in a list
tags: arrays, numbers, sorting, week2
see: 06_lists#whole-list-math-sum-min-max
difficulty: easy
entry: find_largest_num

### prompt
Create a function that takes a list of numbers. Return the largest number in the list.

Examples

    find_largest_num([4, 5, 1, 3]) → 5
    find_largest_num([300, 200, 600, 150]) → 600
    find_largest_num([1000, 1001, 857, 1]) → 1001

Notes

- Expect either positive numbers or zero (there are no negative numbers).

### walkthrough
You could loop over the list comparing as you go — and later in the course you
will, because it's worth knowing how. But Python already ships with a built-in
that does exactly this:

    def find_largest_num(nums):
        return max(nums)

`max()` takes the list and hands back the biggest item. Its twin `min()` gives you
the smallest. Reaching for a built-in instead of writing the loop yourself is
normal, good Python — not cheating.

### starter
```python
def find_largest_num(nums):
    
```

### solution
```python
def find_largest_num(nums):
    return max(nums)
```

### check
find_largest_num([4, 5, 1, 3]) == 5
find_largest_num([300, 200, 600, 150]) == 600
find_largest_num([1000, 1001, 857, 1]) == 1001
find_largest_num([0, 0, 0]) == 0
find_largest_num([9]) == 9

---

## find_smallest_num
kind: code_fn
title: Find the smallest number in a list
tags: arrays, numbers, sorting, week2
see: 06_lists#whole-list-math-sum-min-max
difficulty: easy
entry: find_smallest_num

### prompt
Create a function that takes a list of numbers and returns the smallest number in
the list.

Examples

    find_smallest_num([34, 15, 88, 2]) → 2
    find_smallest_num([34, -345, -1, 100]) → -345
    find_smallest_num([-76, 1.345, 1, 0]) → -76
    find_smallest_num([0.4356, 0.8795, 0.5435, -0.9999]) → -0.9999
    find_smallest_num([7, 7, 7]) → 7

Notes

- Test cases contain decimals, and negative numbers.

### starter
```python
def find_smallest_num(nums):
    
```

### solution
```python
def find_smallest_num(nums):
    return min(nums)
```

### check
find_smallest_num([34, 15, 88, 2]) == 2
find_smallest_num([34, -345, -1, 100]) == -345
find_smallest_num([-76, 1.345, 1, 0]) == -76
find_smallest_num([0.4356, 0.8795, 0.5435, -0.9999]) == -0.9999
find_smallest_num([7, 7, 7]) == 7
