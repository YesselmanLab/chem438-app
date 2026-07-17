# Lists
unit: 6

## Why lists exist

Say you want to keep three test scores. With what you know so far, that's three variables:

```python
score1 = 88
score2 = 92
score3 = 79
print(score1, score2, score3)    # 88 92 79
```

That works for three. It falls apart for thirty. You can't ask "how many scores do I have?" or "what's the biggest one?" — the values aren't connected to each other, they just happen to have similar names.

A **list** holds many values under one name:

```python
scores = [88, 92, 79]
print(scores)          # [88, 92, 79]
print(type(scores))    # <class 'list'>
```

One name, one thing to pass around — and Python can now answer questions about the whole group at once.

```python
print(len(scores))    # 3
print(max(scores))    # 92
print(sum(scores))    # 259
```

## Making a list

Square brackets, values separated by commas.

```python
colors = ["red", "green", "blue"]
prices = [4, 2.5, 10]
print(colors)    # ['red', 'green', 'blue']
print(prices)    # [4, 2.5, 10]
```

The values are called **items** or **elements**. They don't have to be the same type, and a list can be empty:

```python
mixed = ["coffee", 4, True]
empty = []
print(mixed)         # ['coffee', 4, True]
print(empty)         # []
print(len(empty))    # 0
```

`list()` turns other things into a list. On a string, you get one item per character:

```python
print(list("abc"))    # ['a', 'b', 'c']
```

Notice that `print(colors)` shows the quotes around each string — that's Python showing you the list *structure*. Printing one item on its own has no quotes:

```python
print(colors)       # ['red', 'green', 'blue']
print(colors[0])    # red
```

## Length: len()

`len()` counts the items — not the characters inside them. `"green"` is 5 characters, but it's still just **one** item.

```python
print(len(colors))    # 3

words = ["a", "bb", "ccc"]
print(len(words))       # 3
print(len(words[2]))    # 3   <- len of the item "ccc", not of the list
```

## Indexing: getting one item out

Same square brackets as strings, and the same rule: **counting starts at 0**.

```python
playlist = ["intro", "verse", "chorus", "outro"]
print(playlist[0])    # intro
print(playlist[1])    # verse
print(playlist[3])    # outro
```

Here's the list with its positions written out:

```
item:  "intro"  "verse"  "chorus"  "outro"
pos:      0        1         2        3
neg:     -4       -3        -2       -1
```

### Negative indexes

Negative positions count backward from the end. `-1` is always the last item, however long the list is — you don't need to know the length to grab it.

```python
print(playlist[-1])    # outro
print(playlist[-2])    # chorus
```

**Predict the output before you run this:**

```python
seats = ["A1", "A2", "B1", "B2", "B3"]
print(seats[2])
print(seats[-1])
```

`seats[2]` is `"B1"` — position 0 is `"A1"`, 1 is `"A2"`, 2 is `"B1"`. And `seats[-1]` is `"B3"`, the last one. Run it and check.

### IndexError: off by one

A list of 4 items has positions 0, 1, 2, 3. There is no position 4.

```python
playlist = ["intro", "verse", "chorus", "outro"]
print(playlist[4])
# IndexError: list index out of range
```

> **Common mistake: `lst[len(lst)]` to get the last item.** `len(playlist)` is `4`, and `playlist[4]` doesn't exist — the last item is at `len(playlist) - 1`. This off-by-one is the single most common list error. Just use `playlist[-1]` instead and stop thinking about it.

```python
playlist = ["intro", "verse", "chorus", "outro"]
print(len(playlist))              # 4
print(playlist[len(playlist) - 1])    # outro
print(playlist[-1])               # outro
```

## Lists are mutable

This is the big difference from strings. You cannot change a character inside a string:

```python
word = "python"
word[0] = "P"
# TypeError: 'str' object does not support item assignment
```

But you **can** change an item inside a list. Lists are **mutable** — changeable in place.

```python
colors = ["red", "green", "blue"]
colors[0] = "purple"
print(colors)    # ['purple', 'green', 'blue']
```

No new list was made. The list `colors` points at was edited. That one fact is behind almost everything else on this page — including the two traps at the bottom.

```python
scores = [88, 92, 79]
scores[1] = 100
print(scores)    # [88, 100, 79]
```

## Slicing

`start:stop` gives you a **new list** with a range of items: from `start`, up to but **not including** `stop`.

```python
letters = ["a", "b", "c", "d", "e"]
print(letters[1:4])    # ['b', 'c', 'd']
print(letters[:2])     # ['a', 'b']
print(letters[3:])     # ['d', 'e']
print(letters[-2:])    # ['d', 'e']
```

Positions 1, 2, 3 — not 4. Same rule as string slicing. Leaving a side blank means "from the start" or "to the end".

Slicing never errors on a bad range — it just gives you what's there:

```python
print(letters[2:99])    # ['c', 'd', 'e']
print(letters[9:12])    # []
```

> **Watch out:** slicing gives back a **list**, even when it's one item long. `letters[0]` is the item; `letters[0:1]` is a list containing that item. They are not equal.

```python
print(letters[0])                    # a
print(letters[0:1])                  # ['a']
print(letters[0] == letters[0:1])    # False
```

## Adding items

### .append() — one item on the end

```python
cart = ["milk", "eggs"]
cart.append("bread")
print(cart)    # ['milk', 'eggs', 'bread']
```

`.append()` changes `cart` in place. It adds exactly one item, always at the end.

> **Common mistake: `cart = cart.append("bread")`.** `.append()` mutates the list and hands back **nothing** (`None`). Assigning that `None` back over your variable throws the list away.

```python
cart = ["milk", "eggs"]
print(cart.append("bread"))    # None   <- append returns None, not the list
print(cart)                    # ['milk', 'eggs', 'bread']
```

The wrong version and the right version, side by side:

```python
cart = ["milk", "eggs"]
cart = cart.append("bread")    # WRONG — saves the None, loses the list
print(cart)                    # None

cart = ["milk", "eggs"]
cart.append("bread")           # RIGHT — just call it, no =
print(cart)                    # ['milk', 'eggs', 'bread']
```

### .insert() — put an item at a position

```python
queue = ["ana", "ben", "cid"]
queue.insert(1, "zoe")
print(queue)    # ['ana', 'zoe', 'ben', 'cid']
```

`queue.insert(1, "zoe")` means "make `"zoe"` be at position 1" — everything from there on shifts right. `insert(0, x)` puts an item at the front.

### + and .extend() — add several

`+` joins two lists into a **new** list, leaving both originals alone:

```python
a = [1, 2]
b = [3, 4]
print(a + b)    # [1, 2, 3, 4]
print(a)        # [1, 2]
```

`.extend()` does it in place — it dumps the other list's items onto the end:

```python
a = [1, 2]
a.extend([3, 4])
print(a)    # [1, 2, 3, 4]
```

> **Watch out:** `.append()` adds one item; `.extend()` adds each item of a list. Appending a list gives you a list *inside* your list.

```python
a = [1, 2]
a.append([3, 4])
print(a)         # [1, 2, [3, 4]]
print(len(a))    # 3   <- the last item is itself a list
```

## Removing items

### .remove() — by value

```python
cart = ["milk", "eggs", "bread"]
cart.remove("eggs")
print(cart)    # ['milk', 'bread']
```

`.remove()` takes the **value**, not the position, and deletes the first match. If the value isn't there, it raises:

```python
cart = ["milk", "bread"]
cart.remove("cheese")
# ValueError: list.remove(x): x not in list
```

Check first with `in` if you're not sure it's there.

### .pop() — by position, and hand it back

```python
stack = ["a", "b", "c"]
last = stack.pop()
print(last)     # c
print(stack)    # ['a', 'b']
```

With no argument, `.pop()` removes the **last** item and returns it. Give it a position to pop that one instead:

```python
stack = ["a", "b", "c"]
first = stack.pop(0)
print(first)    # a
print(stack)    # ['b', 'c']
```

`.pop()` is the one remover that gives you something back. `.remove()` and `.clear()` return `None`:

```python
cart = ["milk", "eggs"]
print(cart.pop())             # eggs
print(cart.remove("milk"))    # None
print(cart)                   # []
```

### .clear() — empty it out

```python
cart = ["milk", "eggs"]
cart.clear()
print(cart)    # []
```

## Searching a list

### in — is it there?

`in` asks whether a value is an item of the list. You get `True` or `False`.

```python
cart = ["milk", "eggs", "bread"]
print("eggs" in cart)      # True
print("cheese" in cart)    # False
print("cheese" not in cart)    # True
```

This is the safe way to guard a `.remove()`:

```python
cart = ["milk", "eggs", "bread"]
if "eggs" in cart:
    cart.remove("eggs")
print(cart)    # ['milk', 'bread']
```

> **Watch out:** `in` matches whole items, not pieces of them. `"egg" in ["eggs"]` is `False` — `"egg"` is not an item of that list, even though it's part of one.

```python
print("egg" in ["eggs"])     # False
print("egg" in "eggs")       # True   <- on a STRING, `in` looks for a substring
```

### .index() — where is it?

```python
cart = ["milk", "eggs", "bread"]
print(cart.index("bread"))    # 2
```

It gives the position of the first match, and raises if the value isn't there:

```python
cart = ["milk", "eggs", "bread"]
print(cart.index("cheese"))
# ValueError: 'cheese' is not in list
```

### .count() — how many?

```python
rolls = [3, 6, 1, 6, 6, 2]
print(rolls.count(6))    # 3
print(rolls.count(4))    # 0
```

`.count()` returns `0` for something that isn't there, so it never raises.

## Sorting: .sort() vs sorted()

Two ways to sort, and telling them apart matters more than any other pair on this page.

`sorted(lst)` returns a **new** sorted list and leaves the original alone:

```python
scores = [88, 92, 79]
ranked = sorted(scores)
print(ranked)    # [79, 88, 92]
print(scores)    # [88, 92, 79]   <- untouched
```

`lst.sort()` sorts the list **in place** and returns `None`:

```python
scores = [88, 92, 79]
scores.sort()
print(scores)    # [79, 88, 92]
```

> **THE classic trap: `x = lst.sort()`.** `.sort()` returns `None`. If you assign its result to a name, you get `None` — and if you assign it back over the original name, your list is gone for good.

```python
scores = [88, 92, 79]
print(scores.sort())      # None   <- .sort() hands back nothing

scores = [88, 92, 79]
scores = scores.sort()    # WRONG — the list is destroyed
print(scores)             # None
```

The rule that saves you: **`.sort()` — no `=`. `sorted()` — always `=`.**

```python
scores = [88, 92, 79]
scores.sort()              # RIGHT: mutate, no =
print(scores)              # [79, 88, 92]

others = [5, 1, 3]
ranked = sorted(others)    # RIGHT: new list, with =
print(ranked)              # [1, 3, 5]
print(others)              # [5, 1, 3]
```

Both take `reverse=True` for biggest-first:

```python
scores = [88, 92, 79]
print(sorted(scores, reverse=True))    # [92, 88, 79]
```

Strings sort alphabetically — but capitals come before lowercase, because Python compares character codes. And `sorted()` works on any group of values, not just lists; it always gives back a **list**:

```python
names = ["ben", "Ana", "cid"]
print(sorted(names))    # ['Ana', 'ben', 'cid']
print(sorted("cab"))    # ['a', 'b', 'c']
```

> **Watch out:** you can't sort a mixed list of numbers and strings — Python has no idea whether `3` comes before `"apple"`.

```python
print(sorted([3, "apple"]))
# TypeError: '<' not supported between instances of 'str' and 'int'
```

## Reversing: .reverse() vs reversed()

Same split as sorting. `.reverse()` mutates and returns `None`:

```python
letters = ["a", "b", "c"]
letters.reverse()
print(letters)    # ['c', 'b', 'a']
```

`reversed(lst)` does **not** give you a list. It gives you a lazy object — a promise to hand items back one at a time, later.

```python
letters = ["a", "b", "c"]
print(reversed(letters))
```

That prints something like this — not your items:

```
<list_reverseiterator object at 0x104a2f550>
```

> **Common mistake: expecting `reversed()` to return a list.** It returns a `list_reverseiterator`, which prints as that unhelpful gibberish. Wrap it in `list()` to get an actual list.

```python
letters = ["a", "b", "c"]
print(list(reversed(letters)))    # ['c', 'b', 'a']
print(letters)                    # ['a', 'b', 'c']   <- original untouched
print(letters[::-1])              # ['c', 'b', 'a']   <- or just slice it
```

That last line is the simplest way to get a reversed copy — the same slice you already know from strings.

**Predict the output before you run this:**

```python
nums = [3, 1, 2]
result = nums.sort()
print(result)
print(nums)
```

`result` is `None` (that's `.sort()` again), and `nums` is now `[1, 2, 3]`.

```python
nums = [3, 1, 2]
result = nums.sort()
print(result)    # None
print(nums)      # [1, 2, 3]
```

## Whole-list math: sum(), min(), max()

These take the whole list and give back one value. None of them change the list.

```python
scores = [88, 92, 79]
print(sum(scores))    # 259
print(min(scores))    # 79
print(max(scores))    # 92
print(len(scores))    # 3
```

An average is `sum()` divided by `len()` — no special function needed:

```python
average = sum(scores) / len(scores)
print(average)             # 86.33333333333333
print(f"{average:.1f}")    # 86.3
```

`min()` and `max()` work on strings too — alphabetically:

```python
names = ["ben", "ana", "cid"]
print(min(names))    # ana
print(max(names))    # cid
```

> **Watch out:** `sum()` needs numbers. On strings it raises, even though `+` joins strings just fine.

```python
print(sum(["a", "b"]))
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

Use `"".join()` for that — the next section.

## Strings and lists: .split() and .join()

These two are the bridge between text and lists. `.split()` cuts a string into a list:

```python
sentence = "the quick brown fox"
words = sentence.split()
print(words)         # ['the', 'quick', 'brown', 'fox']
print(len(words))    # 4
```

Give it a separator to split on something other than spaces:

```python
line = "milk,eggs,bread"
print(line.split(","))    # ['milk', 'eggs', 'bread']
```

`.join()` goes the other way — a list of strings back into one string. It's called **on the glue**, with the list as the argument:

```python
items = ["milk", "eggs", "bread"]
print(", ".join(items))    # milk, eggs, bread
print("-".join(items))     # milk-eggs-bread
print("".join(items))      # milkeggsbread
```

> **Common mistake: `items.join(", ")` — backwards.** The glue string goes first: `", ".join(items)`. Lists have no `.join()` method at all.

```python
items = ["milk", "eggs", "bread"]
print(items.join(", "))
# AttributeError: 'list' object has no attribute 'join'
```

> **Watch out:** `.join()` only takes strings. A list of numbers raises.

```python
print(", ".join([1, 2, 3]))
# TypeError: sequence item 0: expected str instance, int found
```

Together they let you rearrange text:

```python
sentence = "the quick brown fox"
words = sentence.split()
words.sort()
print(" ".join(words))    # brown fox quick the
```

## Two names, one list

This is the trap that produces the strangest bugs. A list variable does not hold the list — it holds a **pointer to** the list. Copying the variable copies the pointer, not the list.

```python
a = [1, 2, 3]
b = a
b.append(4)
print(b)         # [1, 2, 3, 4]
print(a)         # [1, 2, 3, 4]   <- a changed too!
print(a is b)    # True           <- one list, two names
```

> **Common mistake: thinking `b = a` makes a copy.** It doesn't. `a` and `b` are two names for the **same** list. Change it through either name and both see it, because there's only one list. `is` asks "are these the very same object?" — not just equal, but identical — and here it says `True`.

To get a real, independent copy, slice the whole thing with `[:]`, or call `.copy()`. They do the same job:

```python
a = [1, 2, 3]
b = a[:]
b.append(4)
print(a)         # [1, 2, 3]      <- safe
print(b)         # [1, 2, 3, 4]
print(a is b)    # False          <- two different lists now
```

```python
a = [1, 2, 3]
b = a.copy()
print(a == b)    # True    <- same contents, so equal
print(a is b)    # False   <- but not the same list
```

A copy is still **equal** to the original. It just isn't the *same object* — and that's the whole point.

The same thing bites when a list goes into a function. The function gets the pointer, so it edits your list:

```python
def add_bonus(numbers):
    numbers.append(0)

scores = [88, 92]
add_bonus(scores)
print(scores)    # [88, 92, 0]   <- the function changed it
```

If you don't want that, copy inside the function and return the copy:

```python
def add_bonus(numbers):
    result = numbers[:]
    result.append(0)
    return result

scores = [88, 92]
new_scores = add_bonus(scores)
print(scores)        # [88, 92]
print(new_scores)    # [88, 92, 0]
```

## An empty list is falsy

An empty list counts as `False` in an `if`. Any list with items in it counts as `True`.

```python
print(bool([]))           # False
print(bool([1, 2]))       # True
print(bool([0]))          # True   <- one item, so True, even though the item is 0
```

That gives you the plain way to check for emptiness:

```python
cart = []
if not cart:
    print("Your cart is empty")

cart = ["milk"]
if cart:
    print(f"You have {len(cart)} item(s)")
# Your cart is empty
# You have 1 item(s)
```

`if cart:` reads better than `if len(cart) > 0:` and means the same thing.

## Worked example: a receipt

Take a line of text, pull out the prices, and total them.

```python
line = "coffee:4,bagel:3,juice:5"
parts = line.split(",")
print(parts)       # ['coffee:4', 'bagel:3', 'juice:5']

first = parts[0].split(":")
print(first)       # ['coffee', '4']
print(first[1])    # 4
```

Splitting twice gets you down to the pieces. But `first[1]` is the string `"4"`, not the number `4`, so it needs `int()` before any math:

```python
prices = [int(parts[0].split(":")[1]),
          int(parts[1].split(":")[1]),
          int(parts[2].split(":")[1])]
names = [parts[0].split(":")[0], parts[1].split(":")[0], parts[2].split(":")[0]]
print(prices)              # [4, 3, 5]
print(names)               # ['coffee', 'bagel', 'juice']
print(", ".join(names))    # coffee, bagel, juice
print(f"{len(names)} items, ${sum(prices)} total")    # 3 items, $12 total
```

Repeating yourself three times like that is clumsy — a loop will fix it in the next unit. The list tools do the real work: `.split()` to break the text apart, `int()` to make the pieces countable, `sum()` to total them, `.join()` to print them back out.

## Worked example: top scores

```python
scores = [72, 95, 88, 61, 95, 79]
ranked = sorted(scores, reverse=True)
print(ranked)        # [95, 95, 88, 79, 72, 61]
print(ranked[:3])    # [95, 95, 88]
print(scores)        # [72, 95, 88, 61, 95, 79]   <- sorted() left it alone
```

```python
print(max(scores))              # 95
print(scores.count(95))         # 2   <- two people tied for the top
print(scores.index(95))         # 1   <- the FIRST one is at position 1
print(sum(scores) / len(scores))    # 81.66666666666667
```

Drop the lowest score, then re-average — and copy first, so the original survives:

```python
kept = scores[:]
kept.remove(min(kept))
print(kept)                     # [72, 95, 88, 95, 79]
print(scores)                   # [72, 95, 88, 61, 95, 79]
print(sum(kept) / len(kept))    # 85.8
```

## Worked example: cleaning a guest list

```python
raw = "ana, ben, ana, cid, ben"
guests = raw.split(", ")
print(guests)         # ['ana', 'ben', 'ana', 'cid', 'ben']
print(len(guests))    # 5
```

Remove the duplicates one at a time. `.remove()` deletes only the **first** match, which is exactly what you want here:

```python
guests.remove("ana")
guests.remove("ben")
print(guests)                # ['ana', 'cid', 'ben']
print(sorted(guests))        # ['ana', 'ben', 'cid']
print(" & ".join(sorted(guests)))    # ana & ben & cid
```

## Quick reference — what's available

### Making and measuring

- `[]` or `list()` — a new empty list
- `[1, 2, 3]` — a list with items in it
- `list("abc")` — turn a string (or other group) into a list
- `len(lst)` — how many items
- `lst[:]` or `lst.copy()` — an independent copy
- `bool(lst)` — `False` when empty, `True` otherwise

### Getting items out

- `lst[0]` — the first item; `lst[-1]` — the last item
- `lst[1:4]` — a new list, positions 1 to 3 (stop is excluded)
- `lst[:2]` / `lst[2:]` — from the start / to the end
- `lst[::-1]` — a reversed copy

### Changing a list (mutates, returns None)

- `lst.append(x)` — add one item to the end
- `lst.insert(i, x)` — put `x` at position `i`, shift the rest right
- `lst.extend(other)` — add every item of `other` to the end
- `lst.remove(x)` — delete the first `x` (raises `ValueError` if absent)
- `lst.clear()` — delete everything
- `lst.sort()` — sort in place (`reverse=True` for biggest-first)
- `lst.reverse()` — flip in place
- `lst[0] = x` — replace the item at position 0

### Changing a list (returns something)

- `lst.pop()` — remove and return the last item
- `lst.pop(i)` — remove and return the item at position `i`
- `a + b` — a new list, both lists' items

### Asking questions

- `x in lst` / `x not in lst` — is it an item? `True` or `False`
- `lst.index(x)` — position of the first `x` (raises `ValueError` if absent)
- `lst.count(x)` — how many `x` (never raises; `0` if absent)
- `a is b` — are these the very same list, not just equal?

### Whole-list tools (never change the list)

- `sorted(lst)` — a new sorted list (`reverse=True` for biggest-first)
- `reversed(lst)` — a lazy object; wrap in `list()` to see it
- `sum(lst)` — total (numbers only)
- `min(lst)` / `max(lst)` — smallest / biggest
- `sum(lst) / len(lst)` — the average

### Strings and lists

- `text.split()` — split on spaces into a list
- `text.split(",")` — split on a separator
- `", ".join(lst)` — glue a list of strings into one string (glue goes first)

### The two rules worth memorizing

- `.sort()`, `.append()`, `.reverse()`, `.remove()`, `.insert()`, `.extend()`, `.clear()` return `None` — never write `lst = lst.sort()`.
- `b = a` gives a second name for the same list. `b = a[:]` gives a copy.

Most of them together:

```python
inventory = "hammer,nails,tape,nails,glue".split(",")
print(inventory)               # ['hammer', 'nails', 'tape', 'nails', 'glue']
print(len(inventory))          # 5
print(inventory.count("nails"))    # 2
print("tape" in inventory)     # True

backup = inventory[:]
inventory.append("screws")
inventory.remove("glue")
inventory.sort()
print(inventory)               # ['hammer', 'nails', 'nails', 'screws', 'tape']
print(backup)                  # ['hammer', 'nails', 'tape', 'nails', 'glue']
print(" | ".join(inventory))   # hammer | nails | nails | screws | tape

sizes = [3, 5, 4]
print(sorted(sizes))           # [3, 4, 5]
print(sum(sizes))              # 12
print(max(sizes))              # 5
```
