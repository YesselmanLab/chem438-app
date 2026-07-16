# Loops — accumulation & counting

Building up an answer one step at a time: counters, running totals, product
accumulators, and trackers that remember the best thing seen so far.

---

## sum_the_scores
kind: code_fn
title: Add up the scores
tags: loops, arrays, numbers
difficulty: easy
entry: sum_scores

### prompt
Create a function that takes a list of numbers and returns their total.

Examples

    sum_scores([1, 2, 3]) → 6
    sum_scores([10]) → 10
    sum_scores([-2, 5]) → 3

Notes

- Start a total at 0 before the loop, then add each number to it as you go.
- The total of an empty list is 0.
- Don't forget to return the result.

### walkthrough
This is the shape every problem in this file is built on, so get it in your
fingers now. Three parts, always in this order.

Before the loop, create the thing you're building up. It starts at 0, because
adding 0 to anything leaves it alone:

    total = 0

Inside the loop, one item at a time, add it in. `total += n` is shorthand for
`total = total + n` — take what you had, add the new number, put it back:

    for n in nums:
        total += n

After the loop, hand back the answer:

    return total

Two mistakes to name, because they are the two you will actually make. First,
putting `total = 0` inside the loop — then you wipe it clean on every trip and
only the last number survives. It goes above the `for`, not under it. Second,
putting `return total` inside the loop — then you quit after the first number.
Both lines belong outside the loop, lined up with the `for`.

### starter
```python
def sum_scores(nums):
    
```

### solution
```python
def sum_scores(nums):
    total = 0
    for n in nums:
        total += n
    return total
```

### check
sum_scores([1, 2, 3]) == 6
sum_scores([10]) == 10
sum_scores([-2, 5]) == 3
sum_scores([]) == 0
sum_scores([0, 0]) == 0

---

## count_above_threshold
kind: code_fn
title: Count the high scores
tags: loops, arrays, conditions
difficulty: medium
entry: count_above

### prompt
Create a function that takes a list of numbers and a limit, and returns how many
of the numbers are greater than the limit.

Examples

    count_above([4, 9, 2], 3) → 2
    count_above([1, 2, 3], 10) → 0
    count_above([5, 5, 5], 4) → 3

Notes

- Start a counter at 0 before the loop, and add 1 only when the test is true.
- "Greater than" is strict: a number equal to the limit does not count.
- An empty list should return 0.

### starter
```python
def count_above(nums, limit):
    
```

### solution
```python
def count_above(nums, limit):
    count = 0
    for n in nums:
        if n > limit:
            count += 1
    return count
```

### check
count_above([4, 9, 2], 3) == 2
count_above([1, 2, 3], 10) == 0
count_above([5, 5, 5], 4) == 3
count_above([], 0) == 0
count_above([-1, 0, 1], 0) == 1

---

## dice_product_bug
kind: code_fn
title: Fix the dice multiplier
tags: bugs, loops, numbers
difficulty: medium
entry: dice_score

### prompt
This function is supposed to multiply all of the dice rolls together to get a
game score. It always returns 0 instead. Fix it.

Examples

    dice_score([2, 3]) → 6
    dice_score([6, 6, 6]) → 216
    dice_score([4]) → 4

Notes

- Only one line needs to change.
- Ask yourself what the score should be *before* any dice have been multiplied in.

### walkthrough
Run the broken version in your head with [2, 3]. The score starts at 0. First
time round the loop, score = 0 * 2, which is 0. Second time, score = 0 * 3, which
is still 0. Zero is a black hole for multiplication — once it's in there, nothing
gets it out.

This is the trap: you learned to start a running *total* at 0, and that is exactly
right, because adding 0 to something changes nothing:

    total = 0
    total += 5     # 5

But for a running *product* you need the number that changes nothing when you
multiply by it, and that number is 1:

    score = 1
    score *= 5     # 5

So the fix is `score = 1`. The rule worth remembering: an accumulator starts at
the value that leaves the first item untouched — 0 for sums, 1 for products.

### starter
```python
def dice_score(rolls):
    score = 0
    for roll in rolls:
        score *= roll
    return score
```

### solution
```python
def dice_score(rolls):
    score = 1
    for roll in rolls:
        score *= roll
    return score
```

### check
dice_score([2, 3]) == 6
dice_score([6, 6, 6]) == 216
dice_score([4]) == 4
dice_score([1, 1, 1]) == 1
dice_score([1, 5, 2]) == 10

---

## mcq_return_inside_loop
kind: mcq
title: The loop that only ran once
tags: loops, predict, functions
difficulty: medium
answer: 2

### prompt
What does this code print?

    def add_them(nums):
        total = 0
        for x in nums:
            total += x
            return total

    print(add_them([4, 7, 2]))

### choices
- 13
- 4
- 0
- 2

---

## written_why_not_start_max_at_zero
kind: written
title: Why not start the max at zero?
tags: written, loops, concept
difficulty: medium

### prompt
A student writes this to find the largest temperature reading in a list of
freezer readings:

    def biggest_reading(readings):
        biggest = 0
        for r in readings:
            if r > biggest:
                biggest = r
        return biggest

It works on [3, 9, 5], but on [-4, -18, -9] it returns 0 — a reading that was
never in the list.

In one or two sentences, explain why starting at 0 is a bad idea here, and say
what you would start `biggest` at instead so the answer is always a real reading
from the list.

---

## running_balance
kind: code_fn
title: Running token balance
tags: loops, arrays, algorithms
difficulty: medium
entry: running_balance

### prompt
You start with 0 tokens. Given a list of daily changes (positive for tokens
earned, negative for tokens spent), return a list of your balance at the end of
each day.

Examples

    running_balance([5, -2, 10]) → [5, 3, 13]
    running_balance([1, 1, 1]) → [1, 2, 3]
    running_balance([10, -10]) → [10, 0]

Notes

- The result has exactly as many numbers as the input does.
- You need a running total AND a list to collect it into.
- An empty list of changes should return an empty list.

### walkthrough
Two things have to happen inside this loop, and mixing them up is where people
get stuck. You need a number that keeps growing, and a list that keeps getting
longer. They are not the same variable.

Set both up before the loop:

    total = 0
    out = []

Then on each day, update the total first, then record a snapshot of it:

    for change in changes:
        total += change
        out.append(total)
    return out

Walk [5, -2, 10] through: total becomes 5, append 5. Total becomes 3, append 3.
Total becomes 13, append 13. Out is [5, 3, 13].

The mistake to watch for is appending the *change* instead of the total —
`out.append(change)` just hands back the list you were given. You want the total
after the change, not the change itself. The other classic slip is putting
`return out` inside the loop, which stops you after day one. Return it after the
loop finishes, lined up with the `for`, not indented under it.

### starter
```python
def running_balance(changes):
    
```

### solution
```python
def running_balance(changes):
    total = 0
    out = []
    for change in changes:
        total += change
        out.append(total)
    return out
```

### check
running_balance([5, -2, 10]) == [5, 3, 13]
running_balance([1, 1, 1]) == [1, 2, 3]
running_balance([10, -10]) == [10, 0]
running_balance([-3]) == [-3]
running_balance([]) == []

---

## longest_song_titles
kind: code_fn
title: Every longest song title
tags: loops, strings, algorithms
difficulty: hard
entry: longest_song_titles

### prompt
Create a function that takes a list of song titles and returns a list of every
title tied for longest, in the order they appear in the original list.

Examples

    longest_song_titles(["Hey", "Yesterday", "Help"]) → ["Yesterday"]
    longest_song_titles(["one", "two", "six"]) → ["one", "two", "six"]
    longest_song_titles(["a", "bbbb", "cc", "dddd"]) → ["bbbb", "dddd"]

Notes

- Always return a list, even when only one title is longest.
- The list always has at least one title.
- Compare lengths, but collect the titles themselves — not their lengths.

### walkthrough
The instinct is to do this in one pass: walk the list, keep the best title so far,
and collect as you go. Try it and watch it break. On ["a", "bbbb", "cc", "dddd"]
you'd collect "a" (best so far), then "bbbb" beats it, then "dddd" ties it — and
now your list is ["a", "bbbb", "dddd"] with a stale "a" in it that stopped being
the longest three steps ago. You can't collect ties until you know what the
winning length actually is, and you don't know that until you've seen the whole
list.

So do it in two passes. First pass finds the number:

    best = 0
    for t in titles:
        if len(t) > best:
            best = len(t)

Note that `best` here is a *length*, not a title. Starting it at 0 is safe because
no title is shorter than 0 characters — this is the one place a 0 start is fine,
unlike the freezer readings that could go negative.

Second pass collects everything that matches it:

    out = []
    for t in titles:
        if len(t) == best:
            out.append(t)
    return out

That second loop uses `==`, not `>`. Ties are the entire point of this problem,
and `>` would keep only the first one. Order comes for free again: you append in
the order you meet things.

This is also why `max(titles, key=len)` won't rescue you here. It hands back one
title and silently forgets the rest — the question you were asked is a different
question.

### starter
```python
def longest_song_titles(titles):
    
```

### solution
```python
def longest_song_titles(titles):
    best = 0
    for t in titles:
        if len(t) > best:
            best = len(t)
    out = []
    for t in titles:
        if len(t) == best:
            out.append(t)
    return out
```

### check
longest_song_titles(["Hey", "Yesterday", "Help"]) == ["Yesterday"]
longest_song_titles(["one", "two", "six"]) == ["one", "two", "six"]
longest_song_titles(["a", "bbbb", "cc", "dddd"]) == ["bbbb", "dddd"]
longest_song_titles(["Solo"]) == ["Solo"]
longest_song_titles(["Help", "Help!"]) == ["Help!"]

---

## rumor_doubling_hours
kind: code_fn
title: How many hours until everyone knows?
tags: loops, numbers, algorithms
difficulty: hard
entry: rumor_hours

### prompt
At hour 0, exactly 1 person knows a rumor. Every hour, the number of people who
know it doubles. Return how many whole hours it takes until at least `target`
people know.

Examples

    rumor_hours(2) → 1
    rumor_hours(5) → 3
    rumor_hours(100) → 7

Notes

- A while loop is the right tool: keep doubling while too few people know.
- rumor_hours(5) is 3 because the counts go 1 → 2 → 4 → 8, and 8 is the first
  count that reaches 5.
- If the target is already met at hour 0, the answer is 0.

### walkthrough
Every other problem in this file used a `for` loop, and a `for` loop needs to know
how many trips to take before it starts — `for song in songs` takes one trip per
song, `for i in range(5)` takes five. Here you don't know the number of trips.
That's the whole difficulty: how many hours it takes is the answer you're trying
to find, so you can't put it in a `range()` up front.

That is what `while` is for. A `while` loop doesn't count trips — it checks a
question before each trip, and keeps going as long as the answer is True.

Set up the two things you're tracking before the loop, exactly like any
accumulator:

    people = 1
    hours = 0

Now read the loop header as an English sentence:

    while people < target:

"As long as too few people know, keep going." When that stops being true, the
loop stops on its own. Inside, do one hour's worth of work — double the people,
and count the hour:

    while people < target:
        people *= 2
        hours += 1
    return hours

Trace target = 5. Is 1 < 5? Yes → people = 2, hours = 1. Is 2 < 5? Yes → people
= 4, hours = 2. Is 4 < 5? Yes → people = 8, hours = 3. Is 8 < 5? No → stop, and
return 3. Three doublings, which matches 1 → 2 → 4 → 8.

Two slips to name, because you will make one of them. The first: forgetting
`hours += 1`, or forgetting `people *= 2`. A `for` loop always ends because it
runs out of items, but a `while` loop only ends when *you* change something that
makes its question False. Leave `people` alone and it stays 1 forever, 1 < 5 is
forever True, and your program hangs. Every `while` loop needs a line inside it
that moves you toward the exit.

The second: writing `while people <= target`. Check it against target = 1. One
person already knows, so the answer is 0 hours — and `1 < 1` is False, so the
loop never runs and you correctly return 0. But `1 <= 1` is True, so it doubles
once and hands back 1. "At least target" means stop when `people >= target`, so
keep going while `people < target`.

### starter
```python
def rumor_hours(target):
    
```

### solution
```python
def rumor_hours(target):
    people = 1
    hours = 0
    while people < target:
        people *= 2
        hours += 1
    return hours
```

### check
rumor_hours(2) == 1
rumor_hours(5) == 3
rumor_hours(100) == 7
rumor_hours(1) == 0
rumor_hours(8) == 3

---

## dedupe_playlist
kind: code_fn
title: Trim the repeat plays
tags: loops, arrays, conditions
difficulty: hard
entry: dedupe_playlist

### prompt
Create a function that takes a playlist (a list of song names, possibly with
repeats) and returns a new list keeping only the first appearance of each song,
in the original order.

Examples

    dedupe_playlist(["a", "b", "a", "c", "b"]) → ["a", "b", "c"]
    dedupe_playlist(["x", "x", "x"]) → ["x"]
    dedupe_playlist(["p", "q"]) → ["p", "q"]

Notes

- Build a new list — don't change the one you were given.
- `if song not in out:` asks whether you have collected that song already.
- Song names are case sensitive: "Blue" and "blue" are different songs.

### walkthrough
The trick here is that the list you are building is also the list you check
against. You don't need a second bookkeeping variable — the answer so far already
knows everything you've kept.

Start empty, and before adding a song, ask whether it's in there yet:

    out = []
    for song in songs:
        if song not in out:
            out.append(song)
    return out

The `not in` operator asks "is this missing from the list?" and gives back True
or False. So the first "a" gets added; when the second "a" comes round, `"a" not
in out` is False and it gets skipped. Order is preserved for free, because you
append in the order you meet things.

The mistake to name: appending first and trying to clean up afterwards, or
checking `if song not in songs`, which is always False — you're checking the
wrong list. Check what you've *collected*, not what you were *given*.

### starter
```python
def dedupe_playlist(songs):
    
```

### solution
```python
def dedupe_playlist(songs):
    out = []
    for song in songs:
        if song not in out:
            out.append(song)
    return out
```

### check
dedupe_playlist(["a", "b", "a", "c", "b"]) == ["a", "b", "c"]
dedupe_playlist(["x", "x", "x"]) == ["x"]
dedupe_playlist(["p", "q"]) == ["p", "q"]
dedupe_playlist(["Blue", "blue", "Blue"]) == ["Blue", "blue"]
dedupe_playlist([]) == []
