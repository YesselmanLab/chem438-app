# Lists — basics & built-ins

Making lists, pulling items out by position, and letting Python's built-ins do the
counting, adding, and sorting for you.

---

## build_playlist
kind: code_var
title: Build a playlist
tags: arrays, language_fundamentals, types
see: 06_lists#making-a-list
difficulty: starter
entry: playlist

### prompt
Store three song titles in a list called `playlist`, in this exact order: "Blue Sky",
"Rewind", "Nightbus".

Examples

    playlist[0] → "Blue Sky"
    playlist[1] → "Rewind"
    playlist[2] → "Nightbus"

Notes

- A list is written with square brackets and commas between the items.
- Each title is text, so each one needs quotes around it.

### starter
```python
playlist = 
```

### solution
```python
playlist = ["Blue Sky", "Rewind", "Nightbus"]
```

### check
playlist == ["Blue Sky", "Rewind", "Nightbus"]

---

## topping_count
kind: code_fn
title: Count the toppings
tags: arrays, functions, language_fundamentals
see: 06_lists#length-len
difficulty: starter
entry: topping_count

### prompt
Create a function that takes a list of pizza topping names and returns how many
toppings are on the pizza.

Examples

    topping_count(["cheese", "basil"]) → 2
    topping_count(["ham", "olive", "corn", "chili"]) → 4
    topping_count([]) → 0

Notes

- `len()` counts the items in a list for you — you do not need a loop.
- Don't forget to return the result.

### starter
```python
def topping_count(toppings):
    
```

### solution
```python
def topping_count(toppings):
    return len(toppings)
```

### check
topping_count(["cheese", "basil"]) == 2
topping_count(["ham", "olive", "corn", "chili"]) == 4
topping_count([]) == 0
topping_count(["pineapple"]) == 1
topping_count(["a", "b", "c"]) == 3

---

## last_in_line
kind: code_fn
title: Last in line
tags: arrays, indexing, functions
see: 06_lists#negative-indexes
difficulty: starter
entry: last_in_line

### prompt
Create a function that takes a list of names waiting at a food truck, in order from
front to back, and returns the name of the person standing at the very back.

Examples

    last_in_line(["mia", "raj", "kim"]) → "kim"
    last_in_line(["ana", "bo"]) → "bo"
    last_in_line(["solo"]) → "solo"

Notes

- Index `-1` always means the last item, no matter how long the list is.
- The list always has at least one name in it.

### walkthrough
The tempting move is to count the list yourself and grab that spot:

    def last_in_line(queue):
        return queue[len(queue)]

That crashes with an IndexError, and the reason is worth burning in: a list of 3
names has indexes 0, 1, 2 — so `len(queue)` is 3, which is one past the end. This
is the off-by-one error, and it shows up everywhere. You could patch it with
`queue[len(queue) - 1]`, and that does work.

But Python gives you a shortcut. Negative indexes count backward from the end, so
`queue[-1]` is the last item, `queue[-2]` the one before it, and so on:

    def last_in_line(queue):
        return queue[-1]

Same answer, no arithmetic, nothing to get wrong.

### starter
```python
def last_in_line(queue):
    
```

### solution
```python
def last_in_line(queue):
    return queue[-1]
```

### check
last_in_line(["mia", "raj", "kim"]) == "kim"
last_in_line(["ana", "bo"]) == "bo"
last_in_line(["solo"]) == "solo"
last_in_line(["p", "q", "r", "s"]) == "s"

---

## over_budget
kind: code_fn
title: Blew the budget?
tags: arrays, logic, conditions
see: 06_lists#whole-list-math-sum-min-max
difficulty: easy
entry: over_budget

### prompt
Create a function that takes a list of prices from a receipt and a budget. Return
True if the prices add up to more than the budget, otherwise return False.

Examples

    over_budget([4, 5, 3], 10) → True
    over_budget([4, 5], 10) → False
    over_budget([10], 10) → False

Notes

- `sum()` adds up every number in a list.
- Spending exactly the budget is not over it.

### walkthrough
Two things to get right here. First, `sum()` does the adding for you — no loop
needed:

    sum([4, 5, 3])   # 12

Second, and this is where beginners lose a mark: comparing already gives you a
boolean. So you do not need an if-statement at all:

    def over_budget(prices, budget):
        return sum(prices) > budget

The long version with `if ...: return True / else: return False` is not wrong, just
noisy. What IS wrong is using `>=`. Read the task again: spending exactly your
budget is not blowing it. `over_budget([10], 10)` must be False, and `>=` would
return True. Whenever a task says "more than", that is a strict `>`.

### starter
```python
def over_budget(prices, budget):
    
```

### solution
```python
def over_budget(prices, budget):
    return sum(prices) > budget
```

### check
over_budget([4, 5, 3], 10) is True
over_budget([4, 5], 10) is False
over_budget([10], 10) is False
over_budget([], 5) is False
over_budget([100, 1], 50) is True

---

## vote_tally
kind: code_fn
title: Count the votes
tags: arrays, functions, algorithms
see: 06_lists#count-how-many
difficulty: easy
entry: vote_tally

### prompt
Create a function that takes a list of votes (each vote is a name) and one name, and
returns how many times that name was voted for.

Examples

    vote_tally(["ana", "bo", "ana"], "ana") → 2
    vote_tally(["ana", "bo", "ana"], "bo") → 1
    vote_tally(["ana", "bo"], "kim") → 0

Notes

- Lists have a `.count()` method: `votes.count(name)` does the counting for you.
- A name nobody voted for should give 0, not an error.

### walkthrough
`.count()` is a method, not a plain function, so it hangs off the list itself with a
dot:

    def vote_tally(votes, name):
        return votes.count(name)

Two mistakes worth naming. The first is writing `count(votes, name)` — there is no
bare `count()` built-in, and you get a NameError. Compare it to `len(votes)`, which
IS a plain function: `len` goes in front with the list in parentheses, `.count`
goes after the list with a dot. There is no rule you can derive here; you just have
to learn which is which.

The second is worrying about the missing name. If nobody voted for "kim", you might
expect `.count("kim")` to complain. It doesn't — it just returns 0, because it found
zero of them. That is exactly the answer you want, so there is no if-statement to
write.

### starter
```python
def vote_tally(votes, name):
    
```

### solution
```python
def vote_tally(votes, name):
    return votes.count(name)
```

### check
vote_tally(["ana", "bo", "ana"], "ana") == 2
vote_tally(["ana", "bo", "ana"], "bo") == 1
vote_tally(["ana", "bo"], "kim") == 0
vote_tally([], "ana") == 0
vote_tally(["c", "c", "c", "c"], "c") == 4

---

## seating_order
kind: code_fn
title: Alphabetical seating
tags: arrays, sorting, functions
see: 06_lists#sorting-sort-vs-sorted
difficulty: easy
entry: seating_order

### prompt
Create a function that takes a list of guest names and returns a new list with the
names in alphabetical order.

Examples

    seating_order(["raj", "ana", "kim"]) → ["ana", "kim", "raj"]
    seating_order(["zoe", "bo"]) → ["bo", "zoe"]
    seating_order(["solo"]) → ["solo"]

Notes

- `sorted()` hands you back a brand new sorted list.
- All the names are lowercase.

### walkthrough
There are two ways to sort in Python and they behave very differently:

    names.sort()      # rearranges names in place, returns None
    sorted(names)     # leaves names alone, hands back a NEW sorted list

The classic beginner bug is mixing them up:

    def seating_order(names):
        return names.sort()

That returns `None` every single time, because `.sort()` sorts the list but gives
back nothing. The task asks for a new list, so use `sorted()` and return what it
gives you:

    def seating_order(names):
        return sorted(names)

Rule of thumb: if a method changes the thing in place, it usually returns None.

### starter
```python
def seating_order(names):
    
```

### solution
```python
def seating_order(names):
    return sorted(names)
```

### check
seating_order(["raj", "ana", "kim"]) == ["ana", "kim", "raj"]
seating_order(["zoe", "bo"]) == ["bo", "zoe"]
seating_order(["solo"]) == ["solo"]
seating_order([]) == []
seating_order(["c", "a", "b", "a"]) == ["a", "a", "b", "c"]

---

## username_taken_fix
kind: code_fn
title: Fix the username checker
tags: bugs, arrays, logic
see: 06_lists#in-is-it-there
difficulty: easy
entry: is_taken

### prompt
This function should report whether `username` already appears in `taken`, a list of
usernames that are in use. It crashes with a TypeError. Fix it.

Examples

    is_taken("mia", ["mia", "raj"]) → True
    is_taken("zoe", ["mia", "raj"]) → False
    is_taken("bo", []) → False

Notes

- `in` reads left to right: the item you are looking for goes first, then the list.
- Don't forget to return the result.

### walkthrough
The starter says:

    return taken in username

Read that out loud the way Python reads it: "is `taken` inside `username`?" — that
asks Python to search the string "mia" for a whole list. Python won't even try: it
raises `TypeError: 'in <string>' requires string as left operand, not list`. Every
call crashes, not just the ones that should be True.

`in` is not symmetric. The order matters, and it is always:

    thing_you_are_looking_for in collection_you_are_searching

So the fix is to swap the two:

    return username in taken

Whenever you write `in`, say the sentence in your head: "is the needle in the
haystack?" Needle first, haystack second.

### starter
```python
def is_taken(username, taken):
    return taken in username
```

### solution
```python
def is_taken(username, taken):
    return username in taken
```

### check
is_taken("mia", ["mia", "raj"]) is True
is_taken("zoe", ["mia", "raj"]) is False
is_taken("bo", []) is False
is_taken("raj", ["raj"]) is True
is_taken("a", ["b", "c", "a"]) is True

---

## priciest_is_free
kind: code_fn
title: The priciest item is free
tags: arrays, math, algorithms
see: 06_lists#whole-list-math-sum-min-max
difficulty: medium
entry: basket_total

### prompt
A store is running a promo: fill a basket and the single most expensive item in it
costs nothing. Create a function that takes a list of prices and returns what you
actually pay.

Examples

    basket_total([4, 9, 2]) → 6
    basket_total([5, 5]) → 5
    basket_total([12]) → 0

Notes

- The basket always has at least one item.
- Only ONE item is free, even if two items tie for most expensive.

### walkthrough
Add everything up, then take off the priciest item — that is the whole thing:

    def basket_total(prices):
        return sum(prices) - max(prices)

The trap is the tie. If the basket is `[5, 5]`, students often reason "the most
expensive price is 5, so remove all the 5s" and land on 0. But the promo frees one
ITEM, not one PRICE. `max([5, 5])` is just the number 5, and subtracting it once
removes exactly one item's worth — you pay 5. That is the right answer.

Check the single-item case too: `[12]` gives `12 - 12 = 0`. One item, and it is the
most expensive one, so the whole basket is free. The formula handles it without any
special-casing.

### starter
```python
def basket_total(prices):
    
```

### solution
```python
def basket_total(prices):
    return sum(prices) - max(prices)
```

### check
basket_total([4, 9, 2]) == 6
basket_total([5, 5]) == 5
basket_total([12]) == 0
basket_total([1, 2, 3, 4]) == 6
basket_total([10, 1, 1]) == 2

---

## mcq_index_vs_position
kind: mcq
title: Which spot is which?
tags: indexing, arrays, predict
see: 06_lists#negative-indexes
difficulty: medium
answer: 1

### prompt
What does this print?

    queue = ["mia", "raj", "kim", "lee"]
    print(queue[2], queue[-3])

### choices
- kim raj
- raj kim
- kim kim
- lee raj
