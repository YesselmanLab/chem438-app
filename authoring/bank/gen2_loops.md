# Loops — more practice

Extra drills on `for`, `range`, `enumerate`, accumulators, `break`/`continue`, `while`, and nested loops. Heavy on "if I loop over this, what prints?"

---

## p2_range3
kind: mcq
title: Warm-up spins from zero
tags: predict, loops
difficulty: easy
answer: 1

### prompt
A drone logs each warm-up spin, counting from 0. What prints, one per line?

    for spin in range(3):
        print(spin)

### code
for spin in range(3):
    print(spin)

### choices
- 0\n1\n2
- 1\n2\n3
- 0\n1\n2\n3
- 3

---

## p2_range_1_4
kind: mcq
title: Podium places one, two, three
tags: predict, loops
difficulty: easy
answer: 1

### prompt
A race announcer calls the top-3 podium places, starting at 1. What prints, one per line?

    for place in range(1, 4):
        print(place)

### code
for place in range(1, 4):
    print(place)

### choices
- 1\n2\n3
- 1\n2\n3\n4
- 0\n1\n2\n3
- 1\n4

---

## p2_range_step
kind: mcq
title: Even house numbers up the block
tags: predict, loops
difficulty: easy
answer: 1

### prompt
A mail carrier reads the even house numbers up one side of the street. What prints, one per line?

    for house in range(0, 10, 2):
        print(house)

### code
for house in range(0, 10, 2):
    print(house)

### choices
- 0\n2\n4\n6\n8
- 0\n2\n4\n6\n8\n10
- 2\n4\n6\n8\n10
- 0 2 4 6 8

---

## p2_for_string
kind: mcq
title: Spelling out the chant
tags: predict, loops
difficulty: easy
answer: 1

### prompt
The crowd spells out a two-letter chant, one letter per line. What prints?

    for letter in "go":
        print(letter)

### code
for letter in "go":
    print(letter)

### choices
- g\no
- go
- g o
- o\ng

---

## p2_range_len
kind: mcq
title: Numbering a tag's letters
tags: predict, loops
difficulty: easy
answer: 1

### prompt
A form numbers each letter position in a 3-letter tag, starting at 0. What prints, one per line?

    tag = "dog"
    for i in range(len(tag)):
        print(i)

### code
tag = "dog"
for i in range(len(tag)):
    print(i)

### choices
- 0\n1\n2
- 0\n1\n2\n3
- 1\n2\n3
- d\no\ng

---

## p2_accum_sum
kind: mcq
title: Adding up three rounds
tags: predict, loops
difficulty: easy
answer: 1

### prompt
A player tallies points from three rounds. What prints?

    total = 0
    for points in [4, 5, 6]:
        total += points
    print(total)

### code
total = 0
for points in [4, 5, 6]:
    total += points
print(total)

### choices
- 15
- 456
- 6
- 4\n5\n6

---

## p2_sum_range
kind: mcq
title: Coins stacked over four days
tags: predict, loops
difficulty: easy
answer: 1

### prompt
You stack 1 coin on day 1, 2 on day 2, and so on through day 4. What total prints?

    total = 0
    for day in range(1, 5):
        total += day
    print(total)

### code
total = 0
for day in range(1, 5):
    total += day
print(total)

### choices
- 10
- 15
- 6
- 1\n2\n3\n4

---

## p2_count_condition
kind: mcq
title: How many hit five goals
tags: predict, loops
difficulty: easy
answer: 1

### prompt
These are goal counts for five players. How many scored at least 5?

    goals = [8, 3, 9, 2, 7]
    count = 0
    for g in goals:
        if g >= 5:
            count += 1
    print(count)

### code
goals = [8, 3, 9, 2, 7]
count = 0
for g in goals:
    if g >= 5:
        count += 1
print(count)

### choices
- 3
- 2
- 5
- 8\n9\n7

---

## p2_star_end
kind: mcq
title: A row of rating stars
tags: predict, loops
difficulty: easy
answer: 1

### prompt
A review prints one star per rating point, all on one line. What shows for a 4-star review?

    for i in range(4):
        print("*", end="")

### code
for i in range(4):
    print("*", end="")

### choices
- ****
- *\n*\n*\n*
- * * * *
- 4

---

## p2_build_list
kind: mcq
title: Scaling scores by ten
tags: predict, loops
difficulty: easy
answer: 1

### prompt
Each raw score is multiplied by 10 and collected into a new list. What prints?

    scaled = []
    for score in [1, 2, 3]:
        scaled.append(score * 10)
    print(scaled)

### code
scaled = []
for score in [1, 2, 3]:
    scaled.append(score * 10)
print(scaled)

### choices
- [10, 20, 30]
- [1, 2, 3]
- 60
- 10\n20\n30

---

## p2_string_concat
kind: mcq
title: Spelling a word backwards
tags: predict, loops
difficulty: medium
answer: 1

### prompt
Each letter is glued onto the front of what came before. What prints?

    backwards = ""
    for letter in "abc":
        backwards = letter + backwards
    print(backwards)

### code
backwards = ""
for letter in "abc":
    backwards = letter + backwards
print(backwards)

### choices
- cba
- abc
- abcabc
- a\nb\nc

---

## p2_countdown_range
kind: mcq
title: Countdown to launch
tags: predict, loops
difficulty: easy
answer: 1

### prompt
Mission control counts down to launch. What prints, one per line?

    for n in range(5, 0, -1):
        print(n)

### code
for n in range(5, 0, -1):
    print(n)

### choices
- 5\n4\n3\n2\n1
- 5\n4\n3\n2\n1\n0
- 0\n1\n2\n3\n4\n5
- 1\n2\n3\n4\n5

---

## p2_enumerate
kind: mcq
title: Numbering a playlist
tags: predict, loops
difficulty: easy
answer: 1

### prompt
A playlist prints each track with its position number. What prints, one line per track?

    for i, song in enumerate(["Yes", "No"]):
        print(i, song)

### code
for i, song in enumerate(["Yes", "No"]):
    print(i, song)

### choices
- 0 Yes\n1 No
- 1 Yes\n2 No
- Yes No
- 0 1

---

## p2_break_early
kind: mcq
title: Stop at the reserved seat
tags: predict, loops
difficulty: easy
answer: 1

### prompt
Seats are called out in order, but calling stops the moment seat 3 comes up. What prints, one per line?

    for seat in [1, 2, 3, 4, 5]:
        if seat == 3:
            break
        print(seat)

### code
for seat in [1, 2, 3, 4, 5]:
    if seat == 3:
        break
    print(seat)

### choices
- 1\n2
- 1\n2\n3
- 1\n2\n4\n5
- 1\n2\n3\n4\n5

---

## p2_continue_skip
kind: mcq
title: The elevator skips a floor
tags: predict, loops
difficulty: easy
answer: 1

### prompt
An elevator announces each floor but skips floor 2. What prints, one per line?

    for floor in [1, 2, 3, 4]:
        if floor == 2:
            continue
        print(floor)

### code
for floor in [1, 2, 3, 4]:
    if floor == 2:
        continue
    print(floor)

### choices
- 1\n3\n4
- 1\n2\n3\n4
- 1\n4
- 2

---

## p2_while_countdown
kind: mcq
title: Lives ticking down
tags: predict, loops
difficulty: easy
answer: 1

### prompt
A game prints your remaining lives until they hit zero. What prints, one per line?

    lives = 3
    while lives > 0:
        print(lives)
        lives -= 1

### code
lives = 3
while lives > 0:
    print(lives)
    lives -= 1

### choices
- 3\n2\n1
- 3\n2\n1\n0
- 2\n1\n0
- 3

---

## p2_nested_pairs
kind: mcq
title: Every shirt-and-pants combo
tags: predict, loops
difficulty: medium
answer: 1

### prompt
You try every pairing of 2 shirts and 2 pants. What prints, one pair per line?

    for shirt in range(2):
        for pant in range(2):
            print(shirt, pant)

### code
for shirt in range(2):
    for pant in range(2):
        print(shirt, pant)

### choices
- 0 0\n0 1\n1 0\n1 1
- 0 0\n1 1
- 0 1\n0 1
- 0\n1\n0\n1

---

## p2_nested_stars
kind: mcq
title: Building a staircase of stars
tags: predict, loops
difficulty: medium
answer: 1

### prompt
Each row prints one more star than the last. What prints?

    for row in range(3):
        for star in range(row + 1):
            print("*", end="")
        print()

### code
for row in range(3):
    for star in range(row + 1):
        print("*", end="")
    print()

### choices
- *\n**\n***
- ***\n***\n***
- *\n*\n*
- ******

---

## g2_fix_accum_inside
kind: code_fn
title: The step counter keeps resetting
tags: loops, bugs, functions
difficulty: medium
entry: total_steps

### prompt
`total_steps(days)` should add up every day's step count. Instead it always reports just the last day. Find out why and fix it.

Examples

    total_steps([100, 200, 300]) → 600
    total_steps([50]) → 50
    total_steps([]) → 0

Notes

- The bug is about *where* a line sits, not what it says.
- An empty list should give 0.

### walkthrough
Walk the broken loop with `[100, 200, 300]`. Each pass runs `total = 0` first — that line is *inside* the loop — and only then adds the day's steps. So the running total is wiped clean every single trip, and you return only the final day.

A variable that accumulates across a loop must be created **once, before** the loop. Only the work that changes each pass belongs inside:

    def total_steps(days):
        total = 0
        for steps in days:
            total += steps
        return total

Moving `total = 0` out one level of indentation is the whole fix. The empty list then falls out for free: the body never runs and you return the 0 you started with.

### starter
```python
def total_steps(days):
    for steps in days:
        total = 0
        total += steps
    return total
```

### solution
```python
def total_steps(days):
    total = 0
    for steps in days:
        total += steps
    return total
```

### check
total_steps([100, 200, 300]) == 600
total_steps([50]) == 50
total_steps([]) == 0
total_steps([1, 2, 3, 4]) == 10
total_steps([10, 10]) == 20

---

## g2_loop_return_stops_total
kind: code_fn
title: The total stops after one item
tags: loops, bugs, functions
difficulty: medium
entry: total_price

### prompt
`total_price(prices)` should add up every price in the cart. Right now it returns after looking at only the first one. Fix it.

Examples

    total_price([2, 3, 4]) → 9
    total_price([5]) → 5
    total_price([]) → 0

Notes

- The bug is about *where* the `return` sits.
- An empty cart costs 0.

### walkthrough
The `return total` is indented to sit *inside* the loop, so the very first pass hits it and hands the value back immediately — the loop never gets to a second item. With `[2, 3, 4]` you add 2, then return 2.

`return` should run once, after the loop has finished all its passes:

    def total_price(prices):
        total = 0
        for p in prices:
            total += p
        return total

Dedenting `return` one level is the fix. Notice the empty-list case: the loop body never runs, so you fall straight through to `return total`, which is still 0 — exactly right. In the broken version an empty cart never reaches the `return` at all and the function quietly hands back `None`.

### starter
```python
def total_price(prices):
    total = 0
    for p in prices:
        total += p
        return total
```

### solution
```python
def total_price(prices):
    total = 0
    for p in prices:
        total += p
    return total
```

### check
total_price([2, 3, 4]) == 9
total_price([5]) == 5
total_price([]) == 0
total_price([1, 1, 1, 1]) == 4
total_price([10, 20]) == 30

---

## g2_fix_range_end
kind: code_fn
title: The last parking spot is missing
tags: loops, bugs, arrays
difficulty: easy
entry: spot_numbers

### prompt
`spot_numbers(n)` should return the list of parking-spot numbers from 1 to `n`. Right now the very last spot never shows up. Fix it.

Examples

    spot_numbers(3) → [1, 2, 3]
    spot_numbers(1) → [1]
    spot_numbers(0) → []

Notes

- Spots are numbered starting at 1.
- A lot with 0 spots is an empty list, not an error.

### walkthrough
`range(1, n)` starts at 1 and stops *before* `n`, so `range(1, 3)` is just 1 and 2 — the 3 never appears. That is the single most common off-by-one bug in Python.

To include `n` itself, ask `range` to stop one past it:

    for i in range(1, n + 1):

The `+ 1` is not a fudge factor — it is you saying "stop before `n + 1`", which is the same as "include `n`". Check `spot_numbers(0)`: `range(1, 1)` is empty, so you correctly get `[]`.

### starter
```python
def spot_numbers(n):
    spots = []
    for i in range(1, n):
        spots.append(i)
    return spots
```

### solution
```python
def spot_numbers(n):
    spots = []
    for i in range(1, n + 1):
        spots.append(i)
    return spots
```

### check
spot_numbers(3) == [1, 2, 3]
spot_numbers(1) == [1]
spot_numbers(0) == []
spot_numbers(5) == [1, 2, 3, 4, 5]

---

## g2_fix_count_start
kind: code_fn
title: The pass count is one too high
tags: loops, bugs, functions
difficulty: medium
entry: count_passes

### prompt
`count_passes(scores)` should count how many scores are 60 or higher. Every answer comes out one too big. Fix it.

Examples

    count_passes([70, 50, 80]) → 2
    count_passes([40, 30]) → 0
    count_passes([]) → 0

Notes

- A score of exactly 60 counts as a pass.
- No scores at all means 0 passes.

### walkthrough
A counter has to start at the number of things you've counted *before the loop begins* — and that is zero, always. This code starts `count = 1`, so every answer is inflated by one, and an empty list wrongly reports 1.

    def count_passes(scores):
        count = 0
        for s in scores:
            if s >= 60:
                count += 1
        return count

Change the starting value from 1 to 0 and the whole thing lines up: with no scores you never add anything and return the 0 you began with.

### starter
```python
def count_passes(scores):
    count = 1
    for s in scores:
        if s >= 60:
            count += 1
    return count
```

### solution
```python
def count_passes(scores):
    count = 0
    for s in scores:
        if s >= 60:
            count += 1
    return count
```

### check
count_passes([70, 50, 80]) == 2
count_passes([40, 30]) == 0
count_passes([]) == 0
count_passes([60, 60, 60]) == 3
count_passes([100]) == 1

---

## g2_fix_build_list
kind: code_fn
title: The even list keeps forgetting itself
tags: loops, bugs, arrays
difficulty: medium
entry: collect_evens

### prompt
`collect_evens(nums)` should return a new list containing only the even numbers. Right now it never keeps more than the last one. Fix it.

Examples

    collect_evens([1, 2, 3, 4]) → [2, 4]
    collect_evens([2]) → [2]
    collect_evens([1, 3]) → []

Notes

- The bug is about *where* the empty list is created.
- A list with no evens gives `[]`.

### walkthrough
The line `result = []` is inside the loop, so every pass throws away everything collected so far and starts a fresh empty list. You end up with at most the last even number.

The empty list you build into must be created **once, before** the loop:

    def collect_evens(nums):
        result = []
        for n in nums:
            if n % 2 == 0:
                result.append(n)
        return result

Move `result = []` up one level and each `append` now piles onto the same growing list.

### starter
```python
def collect_evens(nums):
    for n in nums:
        result = []
        if n % 2 == 0:
            result.append(n)
    return result
```

### solution
```python
def collect_evens(nums):
    result = []
    for n in nums:
        if n % 2 == 0:
            result.append(n)
    return result
```

### check
collect_evens([1, 2, 3, 4]) == [2, 4]
collect_evens([2]) == [2]
collect_evens([1, 3]) == []
collect_evens([]) == []
collect_evens([2, 4, 6]) == [2, 4, 6]

---

## g2_wrong_infinite_while
kind: mcq
title: What's wrong — the loop never ends
tags: loops, bugs
difficulty: easy
answer: 1

### prompt
This code is supposed to count down and stop, but it runs forever. What's wrong?

    n = 5
    while n > 0:
        print(n)

### choices
- `n` is never changed inside the loop, so `n > 0` stays true forever
- `while` can't be used to count down
- `print` needs `end=""` to stop the loop
- the condition should be `n < 0`

---

## g2_wrong_range_end
kind: mcq
title: What's wrong — 10 never prints
tags: loops, bugs
difficulty: easy
answer: 1

### prompt
You want to print the numbers 1 through 10, but 10 is missing. What's wrong?

    for i in range(1, 10):
        print(i)

### choices
- `range(1, 10)` stops before 10, so it prints only 1 through 9
- `range` cannot start at 1
- you must write `range(1, 10, 1)` for it to work
- nothing is wrong; it prints 1 through 10

---

## g2_wrong_return_in_loop
kind: mcq
title: What's wrong — it adds only one number
tags: loops, bugs
difficulty: medium
answer: 1

### prompt
`add_up` is supposed to sum a whole list, but it always returns just the first number. What's wrong?

    def add_up(nums):
        total = 0
        for n in nums:
            total += n
            return total

### choices
- the `return` is inside the loop, so it exits on the first pass
- `total` should start at 1, not 0
- you cannot use `+=` inside a loop
- the loop needs a `break` at the end

---

## g2_wrong_reset_inside
kind: mcq
title: What's wrong — only the last number survives
tags: loops, bugs
difficulty: medium
answer: 1

### prompt
This is meant to add 1, 2 and 3 to get 6, but it prints 3. What's happening?

    total = 0
    for n in [1, 2, 3]:
        total = 0
        total += n
    print(total)

### choices
- `total = 0` runs every pass, wiping the sum, so only the last number is left
- the list should be written as a range
- `print` is indented wrong
- `+=` only works on the first item

---

## g2_concept_range5
kind: mcq
title: What range(5) actually gives
tags: loops, concept
difficulty: easy
answer: 1

### prompt
How many numbers does `range(5)` produce, and what are they?

### choices
- 5 numbers: 0, 1, 2, 3, 4
- 5 numbers: 1, 2, 3, 4, 5
- 6 numbers: 0 through 5
- just one number: 5

---

## g2_concept_total_location
kind: mcq
title: Where the accumulator starts
tags: loops, concept
difficulty: easy
answer: 1

### prompt
You're summing a list with an accumulator. Where must `total = 0` be written?

### choices
- on the line just above the `for` loop
- as the first line inside the loop body
- after the loop, right before you print
- it doesn't matter where it goes

---

## g2_concept_enumerate
kind: mcq
title: What enumerate hands you
tags: loops, concept
difficulty: easy
answer: 1

### prompt
In `for i, x in enumerate(["a", "b", "c"])`, what are `i` and `x` on the first pass?

### choices
- `i` is 0 and `x` is "a"
- `i` is 1 and `x` is "a"
- `i` is "a" and `x` is 0
- `i` is "a" and `x` is "b"

---

## g2_concept_break_continue
kind: mcq
title: break versus continue
tags: loops, concept
difficulty: easy
answer: 1

### prompt
What is the difference between `break` and `continue` inside a loop?

### choices
- `break` stops the loop entirely; `continue` skips to the next pass
- `break` skips one pass; `continue` stops the loop
- they do exactly the same thing
- `break` pauses the loop; `continue` restarts it from the beginning

---

## g2_concept_for_item
kind: mcq
title: What the loop variable holds
tags: loops, concept
difficulty: easy
answer: 1

### prompt
In `for song in playlist:`, what does `song` hold on each pass?

### choices
- one item from the list, in order
- the position number (0, 1, 2, ...)
- the whole list at once
- the length of the list

---

## g2_concept_while_true
kind: mcq
title: When a while loop keeps going
tags: loops, concept
difficulty: easy
answer: 1

### prompt
A `while` loop keeps repeating for as long as its condition is...?

### choices
- True
- False
- equal to zero
- a whole number

---

## g2_count_negatives
kind: code_fn
title: How many freezing days
tags: loops, functions
difficulty: easy
entry: count_negatives

### prompt
Write `count_negatives(nums)` that counts how many temperature readings dropped below zero (negative).

Examples

    count_negatives([-1, 2, -3]) → 2
    count_negatives([1, 2, 3]) → 0
    count_negatives([]) → 0

Notes

- 0 itself is not negative.
- An empty list has 0 negatives.

### walkthrough
This is the counting pattern: a counter that starts at 0 *before* the loop, and goes up by one whenever the current number passes a test.

    def count_negatives(nums):
        count = 0
        for n in nums:
            if n < 0:
                count += 1
        return count

The test is `n < 0` — strictly less than, so 0 is not counted. An empty list never enters the loop and returns the starting 0.

### starter
```python
def count_negatives(nums):
    
```

### solution
```python
def count_negatives(nums):
    count = 0
    for n in nums:
        if n < 0:
            count += 1
    return count
```

### check
count_negatives([-1, 2, -3]) == 2
count_negatives([1, 2, 3]) == 0
count_negatives([]) == 0
count_negatives([-5, -6]) == 2
count_negatives([0, -1, 0]) == 1

---

## g2_sum_evens
kind: code_fn
title: Points from the even rounds
tags: loops, functions
difficulty: easy
entry: sum_evens

### prompt
Write `sum_evens(nums)` that adds up only the even numbers in a list and returns the total.

Examples

    sum_evens([1, 2, 3, 4]) → 6
    sum_evens([2, 4, 6]) → 12
    sum_evens([1, 3, 5]) → 0

Notes

- A number is even when `n % 2 == 0`.
- With no even numbers the total is 0.

### walkthrough
Combine the accumulator with a condition: keep a running `total` that starts at 0, and only add a number when it passes the even test.

    def sum_evens(nums):
        total = 0
        for n in nums:
            if n % 2 == 0:
                total += n
        return total

`n % 2` is the remainder after dividing by 2 — it is 0 for even numbers and 1 for odd ones.

### starter
```python
def sum_evens(nums):
    
```

### solution
```python
def sum_evens(nums):
    total = 0
    for n in nums:
        if n % 2 == 0:
            total += n
    return total
```

### check
sum_evens([1, 2, 3, 4]) == 6
sum_evens([2, 4, 6]) == 12
sum_evens([1, 3, 5]) == 0
sum_evens([]) == 0
sum_evens([0, 2]) == 2

---

## g2_word_lengths
kind: code_fn
title: Character count of each text
tags: loops, functions, arrays
difficulty: easy
entry: word_lengths

### prompt
Write `word_lengths(words)` that takes a list of words and returns a new list with the length of each word, in order.

Examples

    word_lengths(["hi", "bye"]) → [2, 3]
    word_lengths(["a"]) → [1]
    word_lengths([]) → []

Notes

- Return a new list; don't print anything.
- An empty list of words gives an empty list.

### walkthrough
This is the build-a-list pattern. Start with an empty list before the loop, then append one computed value per word.

    def word_lengths(words):
        result = []
        for w in words:
            result.append(len(w))
        return result

`len(w)` is how many characters the word has. Each pass appends exactly one number, so the result lines up one-to-one with the input.

### starter
```python
def word_lengths(words):
    
```

### solution
```python
def word_lengths(words):
    result = []
    for w in words:
        result.append(len(w))
    return result
```

### check
word_lengths(["hi", "bye"]) == [2, 3]
word_lengths(["a"]) == [1]
word_lengths([]) == []
word_lengths(["cat", "dogs", "x"]) == [3, 4, 1]

---

## g2_repeat_string
kind: code_fn
title: Echo the cheer n times
tags: loops, functions, strings
difficulty: easy
entry: repeat_string

### prompt
Write `repeat_string(text, n)` that builds a new string by repeating `text` `n` times, using a loop.

Examples

    repeat_string("ab", 3) → "ababab"
    repeat_string("x", 1) → "x"
    repeat_string("hi", 0) → ""

Notes

- Repeating 0 times gives the empty string `""`.
- Build it with a loop (even though `text * n` also works).

### walkthrough
Start with an empty string and glue `text` onto it once per pass. Use `range(n)` to run the loop exactly `n` times:

    def repeat_string(text, n):
        result = ""
        for i in range(n):
            result += text
        return result

When `n` is 0, `range(0)` is empty, the loop body never runs, and you return the empty string you started with.

### starter
```python
def repeat_string(text, n):
    
```

### solution
```python
def repeat_string(text, n):
    result = ""
    for i in range(n):
        result += text
    return result
```

### check
repeat_string("ab", 3) == "ababab"
repeat_string("x", 1) == "x"
repeat_string("hi", 0) == ""
repeat_string("z", 4) == "zzzz"

---

## g2_count_target
kind: code_fn
title: How often the song repeats
tags: loops, functions
difficulty: medium
entry: count_target

### prompt
Write `count_target(items, target)` that counts how many times `target` appears in a list.

Examples

    count_target([1, 2, 1, 3, 1], 1) → 3
    count_target(["a", "b"], "c") → 0
    count_target([], 5) → 0

Notes

- Compare each item to `target` with `==`.
- If it never appears, the count is 0.

### walkthrough
Counting with a condition again — this time the condition compares each item to the value you're hunting for.

    def count_target(items, target):
        count = 0
        for item in items:
            if item == target:
                count += 1
        return count

Start `count` at 0 above the loop, add 1 each time `item == target`, and return the count. An empty list returns the starting 0.

### starter
```python
def count_target(items, target):
    
```

### solution
```python
def count_target(items, target):
    count = 0
    for item in items:
        if item == target:
            count += 1
    return count
```

### check
count_target([1, 2, 1, 3, 1], 1) == 3
count_target(["a", "b"], "c") == 0
count_target([], 5) == 0
count_target([7, 7], 7) == 2
count_target([1, 2, 3], 2) == 1

---

## g2_sum_1_to_n
kind: code_fn
title: Total steps on a stair climb
tags: loops, functions
difficulty: medium
entry: sum_1_to_n

### prompt
Write `sum_1_to_n(n)` that adds up every whole number from 1 to `n` (both included), using a `while` loop.

Examples

    sum_1_to_n(5) → 15
    sum_1_to_n(1) → 1
    sum_1_to_n(0) → 0

Notes

- 1 + 2 + 3 + 4 + 5 is 15.
- `sum_1_to_n(0)` is 0, since there is nothing to add.

### walkthrough
A `while` loop needs three parts: a counter set up before the loop, a condition that eventually goes false, and a step inside that moves the counter toward that condition.

    def sum_1_to_n(n):
        total = 0
        i = 1
        while i <= n:
            total += i
            i += 1
        return total

Start `i` at 1 and keep going while `i <= n`, adding `i` and then bumping it by one each pass. Forgetting the `i += 1` would leave `i` stuck at 1 forever — the classic infinite loop. When `n` is 0 the condition `1 <= 0` is false immediately, so you return 0.

### starter
```python
def sum_1_to_n(n):
    
```

### solution
```python
def sum_1_to_n(n):
    total = 0
    i = 1
    while i <= n:
        total += i
        i += 1
    return total
```

### check
sum_1_to_n(5) == 15
sum_1_to_n(1) == 1
sum_1_to_n(0) == 0
sum_1_to_n(10) == 55
sum_1_to_n(3) == 6
