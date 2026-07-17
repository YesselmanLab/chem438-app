# Lists — more practice

Extra drills on making lists, pulling items out by position, changing them in place, and the built-in tools that add, remove, count, and sort.

---

## p_first_item
kind: mcq
title: Top of the playlist
tags: predict, arrays
difficulty: starter
answer: 1

### prompt
Your playlist stores each song's play count. What plays back?

    print([210, 45, 180][0])

### code
print([210, 45, 180][0])

### choices
- 210
- 1
- 45
- 180

---

## p_last_neg
kind: mcq
title: Last one through the door
tags: predict, arrays, indexing
difficulty: starter
answer: 2

### prompt
The guest list is in arrival order. Who showed up last?

    print(["Ana", "Bo", "Cy"][-1])

### code
print(["Ana", "Bo", "Cy"][-1])

### choices
- Ana
- Cy
- Bo
- -1

---

## p_slice_mid
kind: mcq
title: The middle innings
tags: predict, arrays
difficulty: easy
answer: 1

### prompt
These are the runs scored each inning. What does this slice print?

    print([12, 15, 9, 20][1:3])

### code
print([12, 15, 9, 20][1:3])

### choices
- [15, 9]
- [15, 9, 20]
- [12, 15]
- [9, 20]

---

## p_append_end
kind: mcq
title: Tossing cheese in the cart
tags: predict, arrays
difficulty: easy
answer: 3

### prompt
You grab one more thing on the way out. What's in the cart now?

    cart = ["milk", "eggs", "bread"]
    cart.append("cheese")
    print(cart)

### code
cart = ["milk", "eggs", "bread"]
cart.append("cheese")
print(cart)

### choices
- ['cheese', 'milk', 'eggs', 'bread']
- ['milk', 'eggs', 'bread']
- ['milk', 'eggs', 'bread', 'cheese']
- ['bread', 'eggs', 'milk', 'cheese']

---

## p_len_list
kind: mcq
title: Headcount for the party
tags: predict, arrays
difficulty: starter
answer: 2

### prompt
How many people are on the guest list?

    print(len(["Ana", "Bo", "Cy", "Di"]))

### code
print(len(["Ana", "Bo", "Cy", "Di"]))

### choices
- 3
- 4
- 5
- ["Ana", "Bo", "Cy", "Di"]

---

## p_sum_list
kind: mcq
title: Ringing up the total
tags: predict, arrays
difficulty: easy
answer: 1

### prompt
Three items land in the cart. What's the total price?

    print(sum([12, 8, 5]))

### code
print(sum([12, 8, 5]))

### choices
- 25
- 5
- 1285
- 3

---

## p_max_list
kind: mcq
title: Who topped the leaderboard
tags: predict, arrays
difficulty: easy
answer: 3

### prompt
These are tonight's final scores. What's the high score?

    print(max([88, 72, 95, 60]))

### code
print(max([88, 72, 95, 60]))

### choices
- 88
- 72
- 95
- 60

---

## p_sort_returns_none
kind: mcq
title: The sort() trap
tags: predict, sorting
difficulty: medium
answer: 2

### prompt
Watch closely — you try to grab the sorted leaderboard in one line:

    ranked = [30, 10, 20].sort()
    print(ranked)

### code
ranked = [30, 10, 20].sort()
print(ranked)

### choices
- [10, 20, 30]
- None
- [30, 10, 20]
- it raises an error

---

## p_sorted_new
kind: mcq
title: Ranking the scores
tags: predict, sorting
difficulty: easy
answer: 1

### prompt
You sort tonight's scores lowest to highest. What prints?

    print(sorted([95, 60, 88]))

### code
print(sorted([95, 60, 88]))

### choices
- [60, 88, 95]
- [95, 60, 88]
- None
- [95, 88, 60]

---

## p_alias_append
kind: mcq
title: Two names, one playlist
tags: predict, arrays
difficulty: medium
answer: 4

### prompt
Watch closely — Bo copies your playlist, then you add a song:

    playlist = ["Ana", "Bo"]
    shared = playlist
    playlist.append("Cy")
    print(shared)

### code
playlist = ["Ana", "Bo"]
shared = playlist
playlist.append("Cy")
print(shared)

### choices
- ['Ana', 'Bo']
- ['Cy']
- it raises an error
- ['Ana', 'Bo', 'Cy']

---

## p_pop_last
kind: mcq
title: One guest heads home
tags: predict, arrays
difficulty: medium
answer: 1

### prompt
The last guest on the list leaves early. Who's still here?

    guests = ["Ana", "Bo", "Cy"]
    guests.pop()
    print(guests)

### code
guests = ["Ana", "Bo", "Cy"]
guests.pop()
print(guests)

### choices
- ['Ana', 'Bo']
- ['Bo', 'Cy']
- ['Ana', 'Bo', 'Cy']
- 'Cy'

---

## bug_append_returns_list
kind: code_fn
title: The cart keeps coming up empty
tags: bugs, arrays
difficulty: easy
entry: add_item
### prompt
`add_item` should drop `item` at the end of the `cart` list and return the updated
cart. Instead every call returns `None`. Fix it.

Examples

    add_item(["milk"], "eggs") → ["milk", "eggs"]
    add_item([], "bread")      → ["bread"]

Notes

- `.append()` changes the list in place and hands back `None`.
- Do the append on one line, then return the list on the next.

### starter
```python
def add_item(cart, item):
    return cart.append(item)
```

### solution
```python
def add_item(cart, item):
    cart.append(item)
    return cart
```

### check
add_item(["milk"], "eggs") == ["milk", "eggs"]
add_item([], "bread") == ["bread"]
add_item(["a", "b"], "c") == ["a", "b", "c"]
add_item(["p"], "q") == ["p", "q"]

---

## bug_sort_returns_none
kind: code_fn
title: The leaderboard shows nothing
tags: bugs, sorting
difficulty: easy
entry: rank_scores
### prompt
`rank_scores` should return a new list of the scores ranked lowest to highest.
Right now it returns `None`. Fix it.

Examples

    rank_scores([3, 1, 2]) → [1, 2, 3]
    rank_scores([5, 4])    → [4, 5]

Notes

- `.sort()` rearranges a list in place and returns `None`.
- `sorted(list)` hands back a brand-new sorted list.

### starter
```python
def rank_scores(scores):
    return scores.sort()
```

### solution
```python
def rank_scores(scores):
    return sorted(scores)
```

### check
rank_scores([3, 1, 2]) == [1, 2, 3]
rank_scores([5, 4]) == [4, 5]
rank_scores([9]) == [9]
rank_scores([2, 2, 1]) == [1, 2, 2]

---

## bug_second_item_index
kind: code_fn
title: Grabbing the runner-up
tags: bugs, arrays, indexing
difficulty: easy
entry: second_item
### prompt
`second_item` should return the SECOND finisher in the list. It grabs the wrong spot
(and crashes on a two-person list). Fix it.

Examples

    second_item(["a", "b", "c"]) → "b"
    second_item([10, 20, 30])    → 20

Notes

- The first item is at index 0, so the second item is at index 1.
- The list always has at least two items.

### starter
```python
def second_item(items):
    return items[2]
```

### solution
```python
def second_item(items):
    return items[1]
```

### check
second_item(["a", "b", "c"]) == "b"
second_item([10, 20, 30]) == 20
second_item(["x", "y"]) == "y"
second_item([1, 2, 3, 4]) == 2

---

## bug_last_two_slice
kind: code_fn
title: The last two across the line
tags: bugs, arrays
difficulty: medium
entry: last_two
### prompt
`last_two` should return a list of the last TWO finishers. Right now it returns just
one item, not a list. Fix it.

Examples

    last_two([1, 2, 3])           → [2, 3]
    last_two(["a", "b", "c", "d"]) → ["c", "d"]

Notes

- A single negative index like `items[-2]` gives one item, not a list.
- A slice like `items[-2:]` gives a list of the last two items.

### starter
```python
def last_two(items):
    return items[-2]
```

### solution
```python
def last_two(items):
    return items[-2:]
```

### check
last_two([1, 2, 3]) == [2, 3]
last_two(["a", "b", "c", "d"]) == ["c", "d"]
last_two([10, 20]) == [10, 20]
last_two([5, 6, 7]) == [6, 7]

---

## wrong_sort_then_index
kind: mcq
title: What's wrong — chasing the low score
tags: bugs, sorting
difficulty: medium
answer: 1

### prompt
A player wants the lowest score of the night, so they write:

    scores = [88, 72, 95]
    ranked = scores.sort()
    print(ranked[0])

This crashes with a TypeError. What is wrong?

### choices
- `.sort()` returns `None`, so `ranked` is `None` and `ranked[0]` has nothing to index
- `.sort()` sorted the list into the wrong order
- you cannot sort a list of numbers
- `print` cannot show a single list item

---

## wrong_append_reassign
kind: mcq
title: What's wrong — the cart vanished
tags: bugs, arrays
difficulty: medium
answer: 2

### prompt
A shopper writes:

    cart = ["milk"]
    cart = cart.append("eggs")
    print(cart)

They expected `['milk', 'eggs']` but got `None`. What went wrong?

### choices
- `.append` adds to the front of the list, not the end
- `cart.append(...)` returns `None`, so `cart = cart.append(...)` throws away the list and stores `None`
- you can't append a string to a list of strings
- the list must be sorted before you can append to it

---

## wrong_index_off_end
kind: mcq
title: What's wrong — no fourth guest
tags: bugs, arrays, indexing
difficulty: easy
answer: 3

### prompt
A host writes:

    names = ["ana", "ben", "cal"]
    print(names[3])

It raises an `IndexError`. Why?

### choices
- lists start counting at 1, so index 3 is simply the third name
- `names[3]` tries to print all three names at once
- the list has three items at indexes 0, 1, 2 — index 3 is one past the end
- you must write `names.get(3)` to read a list item

---

## wrong_alias_backup
kind: mcq
title: What's wrong — the backup changed too
tags: bugs, arrays
difficulty: medium
answer: 1

### prompt
A player wanted `backup` to keep the original, unchanged inventory:

    original = [1, 2, 3]
    backup = original
    original.append(4)

They were surprised that `backup` is now `[1, 2, 3, 4]`. What went wrong?

### choices
- `backup = original` makes both names point to the SAME list; to copy it, use `backup = original[:]` or `list(original)`
- `.append` accidentally changed `backup` instead of `original`
- lists cannot be copied in Python
- `backup` needs to be sorted to stay separate from `original`

---

## concept_sort_vs_sorted
kind: mcq
title: Concept — sort() vs sorted()
tags: concept, sorting
difficulty: medium
answer: 1

### prompt
What is the difference between `nums.sort()` and `sorted(nums)`?

### choices
- `.sort()` rearranges `nums` in place and returns `None`; `sorted(nums)` leaves `nums` alone and returns a new sorted list
- there is no difference; they do exactly the same thing
- `.sort()` returns a new list; `sorted(nums)` changes `nums` in place
- `sorted(nums)` only works on lists of numbers, `.sort()` works on anything

---

## concept_lists_mutable
kind: mcq
title: Concept — can you change a list?
tags: concept, arrays
difficulty: easy
answer: 2

### prompt
Which statement about Python lists is true?

### choices
- a list can never be changed once it is created
- a list is mutable — `lst[0] = "new"` replaces the first item in place
- you can add items to a list but you can never replace one
- writing `lst[0] = "new"` builds a brand-new list and leaves the old one untouched

---

## concept_append_returns
kind: mcq
title: Concept — what append returns
tags: concept, arrays
difficulty: easy
answer: 4

### prompt
What does `my_list.append(x)` return?

### choices
- the item `x` that was just added
- the new, longer list
- the length of the list after adding `x`
- `None` — it changes the list in place and hands back nothing

---

## concept_first_index_zero
kind: mcq
title: Concept — index of the first item
tags: concept, arrays, indexing
difficulty: starter
answer: 1

### prompt
In the playlist `["a", "b", "c"]`, what index does the first song `"a"` sit at?

### choices
- 0
- 1
- -1
- "a"

---

## concept_which_is_list
kind: mcq
title: Concept — which one is a list?
tags: concept, arrays
difficulty: easy
answer: 3

### prompt
Which of these creates a list?

### choices
- `{1, 2, 3}`
- `"[1, 2, 3]"`
- `[1, 2, 3]`
- `1, 2, 3`

---

## concept_aliasing
kind: mcq
title: Concept — two names, one list
tags: concept, arrays
difficulty: medium
answer: 2

### prompt
You run `b = a`, where `a` is a list. Then you run `a.append(5)`. What happens to `b`?

### choices
- `b` stays a separate copy and is unchanged
- `b` also shows the 5, because `b` and `a` are two names for the same list
- it raises an error, because two names can't share one list
- only `a` changes; `b` becomes `[5]`

---

## dice_list
kind: code_var
title: Store the dice rolls
tags: arrays
difficulty: starter
entry: dice
### prompt
Store these three dice rolls in a list called `dice`, in this exact order: 7, 3, 9.

Examples

    dice[0] → 7
    dice[2] → 9

Notes

- A list is written with square brackets and commas between the items.
- These are numbers, so they do not need quotes.

### starter
```python
dice = 
```

### solution
```python
dice = [7, 3, 9]
```

### check
dice == [7, 3, 9]

---

## list_average
kind: code_fn
title: Class average
tags: arrays
difficulty: easy
entry: list_average
### prompt
Create a function that takes a non-empty list of test scores and returns their average
(the sum divided by how many there are).

Examples

    list_average([2, 4])    → 3
    list_average([10])      → 10
    list_average([1, 2, 3]) → 2

Notes

- `sum()` adds up the list and `len()` counts it — no loop needed.
- The list always has at least one number, so you never divide by zero.

### starter
```python
def list_average(nums):
    
```

### solution
```python
def list_average(nums):
    return sum(nums) / len(nums)
```

### check
list_average([2, 4]) == 3
list_average([10]) == 10
list_average([1, 2, 3]) == 2
list_average([5, 15]) == 10

---

## first_and_last
kind: code_fn
title: Opener and closer
tags: arrays, indexing
difficulty: easy
entry: first_and_last
### prompt
Create a function that takes a playlist and returns a NEW two-item list holding just the
first track and the last track, in that order.

Examples

    first_and_last([1, 2, 3])           → [1, 3]
    first_and_last(["a", "b", "c", "d"]) → ["a", "d"]
    first_and_last([5])                 → [5, 5]

Notes

- Index `0` is the first item and index `-1` is the last item.
- If the list has one item, the first and last are the same item.

### starter
```python
def first_and_last(items):
    
```

### solution
```python
def first_and_last(items):
    return [items[0], items[-1]]
```

### check
first_and_last([1, 2, 3]) == [1, 3]
first_and_last(["a", "b", "c", "d"]) == ["a", "d"]
first_and_last([9, 9]) == [9, 9]
first_and_last([5]) == [5, 5]

---

## sort_desc
kind: code_fn
title: Leaderboard, highest first
tags: sorting
difficulty: medium
entry: sort_desc
### prompt
Create a function that takes a list of scores and returns a NEW list ranked from
highest to lowest.

Examples

    sort_desc([1, 3, 2])    → [3, 2, 1]
    sort_desc([5, 4])       → [5, 4]
    sort_desc([2, 9, 1, 5]) → [9, 5, 2, 1]

Notes

- `sorted(nums)` gives smallest-first; add `reverse=True` to flip it.
- Return the new list `sorted()` hands you.

### starter
```python
def sort_desc(nums):
    
```

### solution
```python
def sort_desc(nums):
    return sorted(nums, reverse=True)
```

### check
sort_desc([1, 3, 2]) == [3, 2, 1]
sort_desc([5, 4]) == [5, 4]
sort_desc([7]) == [7]
sort_desc([2, 9, 1, 5]) == [9, 5, 2, 1]

---

## make_sentence
kind: code_fn
title: Words into a text message
tags: arrays
difficulty: medium
entry: make_sentence
### prompt
Create a function that takes a list of words and returns them joined into one message
with a single space between each word.

Examples

    make_sentence(["hello", "there"]) → "hello there"
    make_sentence(["a", "b", "c"])    → "a b c"
    make_sentence(["solo"])           → "solo"

Notes

- `" ".join(words)` glues the words together with a space between them.
- You do not need a loop for this.

### starter
```python
def make_sentence(words):
    
```

### solution
```python
def make_sentence(words):
    return " ".join(words)
```

### check
make_sentence(["hello", "there"]) == "hello there"
make_sentence(["a", "b", "c"]) == "a b c"
make_sentence(["solo"]) == "solo"
make_sentence(["i", "am", "here"]) == "i am here"

---

## roll_count
kind: code_fn
title: How many of that face?
tags: arrays
difficulty: easy
entry: roll_count
### prompt
Create a function that takes a list of dice rolls and one face value, and returns how
many times that face came up.

Examples

    roll_count([1, 6, 6, 3], 6) → 2
    roll_count([1, 2, 3], 5)    → 0
    roll_count([4, 4, 4], 4)    → 3

Notes

- Lists have a `.count()` method: `rolls.count(face)` does the counting for you.
- A face that never came up should give 0, not an error.

### starter
```python
def roll_count(rolls, face):
    
```

### solution
```python
def roll_count(rolls, face):
    return rolls.count(face)
```

### check
roll_count([1, 6, 6, 3], 6) == 2
roll_count([1, 2, 3], 5) == 0
roll_count([4, 4, 4], 4) == 3
roll_count([2], 2) == 1
