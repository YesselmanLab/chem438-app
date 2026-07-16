# Lists — methods & slicing

Reaching into lists from the end, and using the list methods that add, remove, count, and reorder items.

---

## written_sort_returns_none
kind: written
title: Why did my sorted list vanish?
tags: arrays, sorting, written
difficulty: easy

### prompt
A student wants their scores in order, so they write:

    scores = [88, 72, 95]
    ranked = scores.sort()
    print(ranked)

They expected `[72, 88, 95]`. Python printed `None`.

In a sentence or two, explain why `ranked` is `None`, and give the two different
ways to fix this so the sorted numbers actually get printed.

Notes

- Nothing crashed and nothing was lost — think about what `.sort()` hands back.
- One fix keeps using `.sort()`; the other uses a different tool.

---

## squeeze_in_a_guest
kind: code_fn
title: Squeeze in a guest
tags: arrays, bugs, functions
difficulty: medium
entry: seat_guest

### prompt
`seat_guest` should place `guest` into the third chair (index 2) of the seating
list and return the updated list. It doesn't work. Fix it.

Examples

    seat_guest(["ana", "ben", "cal"], "dee") → ["ana", "ben", "dee", "cal"]
    seat_guest(["ana", "ben"], "zed")        → ["ana", "ben", "zed"]
    seat_guest([], "solo")                   → ["solo"]

Notes

- `.insert()` takes the position first, then the item: `seats.insert(position, item)`.
- `.insert()` changes the list itself and hands back nothing.
- If the list is shorter than the position you asked for, `.insert()` just puts the item on the end. That's fine here.

### walkthrough
There are two mistakes stacked in that one line, and both are worth naming.

First, the arguments are backwards. `.insert()` is always
`insert(position, item)` — the number comes first. Writing
`seats.insert(guest, 2)` asks Python to insert the number 2 at position "dee",
which isn't a position at all.

Second, `.insert()` is a method that *changes the list in place*. It edits
`seats` and returns `None`. So `return seats.insert(2, guest)` would hand the
caller `None` even after the arguments were fixed — the insertion would happen,
and then you'd throw away the list and return nothing.

The rule to carry with you: methods that modify a list (`.insert`, `.append`,
`.sort`, `.remove`) return `None`. Do the modification on one line, then return
the list on the next:

    def seat_guest(seats, guest):
        seats.insert(2, guest)
        return seats

### starter
```python
def seat_guest(seats, guest):
    return seats.insert(guest, 2)
```

### solution
```python
def seat_guest(seats, guest):
    seats.insert(2, guest)
    return seats
```

### check
seat_guest(["ana", "ben", "cal"], "dee") == ["ana", "ben", "dee", "cal"]
seat_guest(["ana", "ben"], "zed") == ["ana", "ben", "zed"]
seat_guest([], "solo") == ["solo"]
seat_guest(["a", "b", "c", "d"], "x") == ["a", "b", "x", "c", "d"]

---

## race_placement
kind: code_fn
title: What place did they finish?
tags: arrays, indexing, functions
difficulty: easy
entry: placement

### prompt
`finishers` is a list of runners in the order they crossed the line. Create a
function that returns what place a given runner finished in, the way a person
would say it out loud: the first runner finished in place 1.

Examples

    placement(["ana", "ben", "cal"], "ana") → 1
    placement(["ana", "ben", "cal"], "cal") → 3
    placement(["ana", "ben", "cal"], "ben") → 2

Notes

- `.index(value)` gives you the position of a value, counting from 0.
- The name is guaranteed to be somewhere in the list, and appears at most once.
- Check your answer against the examples before you move on.

### starter
```python
def placement(finishers, name):
    
```

### solution
```python
def placement(finishers, name):
    return finishers.index(name) + 1
```

### check
placement(["ana", "ben", "cal"], "ana") == 1
placement(["ana", "ben", "cal"], "cal") == 3
placement(["ana", "ben", "cal"], "ben") == 2
placement(["solo"], "solo") == 1
placement(["w", "x", "y", "z"], "z") == 4

---

## back_of_the_line
kind: code_fn
title: Send them to the back
tags: arrays, functions, indexing
difficulty: medium
entry: send_to_back

### prompt
The person at the front of the coffee line couldn't decide what to order, so they
get sent to the very end. Create a function that takes the first person out of
the line, puts them on the end, and returns the updated line.

Examples

    send_to_back(["ana", "ben", "cal"]) → ["ben", "cal", "ana"]
    send_to_back(["ana", "ben"])        → ["ben", "ana"]
    send_to_back(["solo"])              → ["solo"]

Notes

- `line.pop(0)` removes the item at index 0 and gives it back to you.
- `.append(item)` adds an item to the end.
- A line with one person in it comes back unchanged.

### starter
```python
def send_to_back(line):
    
```

### solution
```python
def send_to_back(line):
    line.append(line.pop(0))
    return line
```

### check
send_to_back(["ana", "ben", "cal"]) == ["ben", "cal", "ana"]
send_to_back(["ana", "ben"]) == ["ben", "ana"]
send_to_back(["solo"]) == ["solo"]
send_to_back(["w", "x", "y", "z"]) == ["x", "y", "z", "w"]

---

## middle_score
kind: code_fn
title: The middle score
tags: arrays, sorting, algorithms
difficulty: hard
entry: middle_score

### prompt
Create a function that sorts a list of scores and returns the middle one. If
there is an even number of scores there is no single middle, so return the
average of the two middle scores instead.

Examples

    middle_score([3, 1, 2])    → 2
    middle_score([4, 1, 3, 2]) → 2.5
    middle_score([9])          → 9

Notes

- `sorted(scores)` gives you a new sorted list without disturbing the original.
- `len(s) % 2` is 1 when the length is odd and 0 when it is even.
- The list always has at least one score — you don't need to handle an empty list.

### walkthrough
Two things make this harder than it looks: the list isn't sorted yet, and the
"middle" of an even-length list doesn't exist.

Start by sorting. Use `sorted(scores)`, not `scores.sort()` — `sorted` gives you
a fresh list back, while `.sort()` returns `None` and rearranges the caller's
list behind their back.

    s = sorted(scores)

Now count. For an odd length, say 5, the middle is index 2 — and `5 // 2` is
exactly 2. That's the whole trick: floor division lands on the middle index for
free. Use `//`, not `/`, because `5 / 2` is `2.5` and Python refuses to index a
list with a float.

For an even length, say 4, there are two middle items, at indexes 1 and 2 —
that's `4 // 2 - 1` and `4 // 2`. Average them.

    def middle_score(scores):
        s = sorted(scores)
        if len(s) % 2:
            return s[len(s) // 2]
        return (s[len(s) // 2 - 1] + s[len(s) // 2]) / 2

`len(s) % 2` is 1 for odd lengths, and Python treats 1 as true — so that `if`
means "if the length is odd". Note the even case uses `/` on purpose: the average
of 2 and 3 should be 2.5, not 2.

### starter
```python
def middle_score(scores):
    
```

### solution
```python
def middle_score(scores):
    s = sorted(scores)
    if len(s) % 2:
        return s[len(s) // 2]
    return (s[len(s) // 2 - 1] + s[len(s) // 2]) / 2
```

### check
middle_score([3, 1, 2]) == 2
middle_score([4, 1, 3, 2]) == 2.5
middle_score([9]) == 9
middle_score([10, 20]) == 15.0
middle_score([5, 100, 7, 6, 8]) == 7

---

## purge_the_playlist
kind: code_fn
title: Purge every copy
tags: arrays, loops, functions
difficulty: hard
entry: purge

### prompt
One song got added to the playlist too many times. Create a function that removes
every copy of `song` from `playlist` and returns the playlist. The song might
appear many times, once, or not at all.

Examples

    purge(["a", "b", "a", "c"], "a") → ["b", "c"]
    purge(["a", "b"], "z")           → ["a", "b"]
    purge(["a", "a", "a"], "a")      → []

Notes

- `playlist.remove(value)` deletes only the FIRST copy it finds, and raises an error if the value isn't there.
- Return the playlist itself, not a new list.

### walkthrough
The obvious first attempt is `playlist.remove(song)`, and it half works: the
playlist gets shorter, but the extra copies are still sitting there. `.remove()`
deletes the first match and stops. It also raises a `ValueError` if the song
isn't in the list at all, which is why you can't just call it and hope.

Both problems have the same answer: check before you remove, and keep going until
there's nothing left to check for.

    def purge(playlist, song):
        while song in playlist:
            playlist.remove(song)
        return playlist

Read the `while` line as the sentence it is: "as long as the song is still in the
playlist, remove one copy." When the last copy goes, `song in playlist` becomes
`False` and the loop stops on its own. If the song was never there, the condition
is `False` on the first look and the loop body never runs — the not-there case
handles itself.

The tempting alternative — a `for` loop over `playlist` that removes as it goes —
is a classic trap. Deleting items from a list while you're iterating over it
shifts everything left under the loop's feet, and it silently skips elements.
Don't modify a list you're looping over.

### starter
```python
def purge(playlist, song):
    
```

### solution
```python
def purge(playlist, song):
    while song in playlist:
        playlist.remove(song)
    return playlist
```

### check
purge(["a", "b", "a", "c"], "a") == ["b", "c"]
purge(["a", "b"], "z") == ["a", "b"]
purge(["a", "a", "a"], "a") == []
purge([], "a") == []
purge(["hit", "dud", "hit", "dud", "hit"], "dud") == ["hit", "hit", "hit"]
