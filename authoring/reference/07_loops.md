# Loops
unit: 7

## Why loops

You have four scores and you want to print each one. You could write it out by hand:

```python
scores = [8, 6, 10, 7]

print(scores[0])
print(scores[1])
print(scores[2])
print(scores[3])
# 8
# 6
# 10
# 7
```

That works. Now imagine 400 scores. Or imagine you don't know how many there are until the program runs. Copy-pasting falls apart fast, and every copy is another place to make a typo.

A loop says it once:

```python
scores = [8, 6, 10, 7]

for s in scores:
    print(s)
# 8
# 6
# 10
# 7
```

Same output, four lines shorter, and it works for 4 scores or 400 without changing a character. **Any time you catch yourself copy-pasting a line and changing one small thing, you want a loop.**

## `for` over a list

The shape of a `for` loop is always the same:

1. the word `for`
2. a **name** you invent for "the current item"
3. the word `in`
4. the thing to loop over
5. a **colon**, then an **indented** body

```python
playlist = ["Dreams", "Kids", "Alright"]

for song in playlist:
    print("Now playing: " + song)
# Now playing: Dreams
# Now playing: Kids
# Now playing: Alright
```

Read it out loud as: "for each song in playlist, print it." Python runs the indented body **once per item**, and each time, `song` holds the next item. Three items, three passes.

Just like `if`, the colon and the indentation are not decoration — they're what tells Python which lines belong to the loop:

```python
playlist = ["Dreams", "Kids", "Alright"]

for song in playlist:
    print(song)
print("Done")
# Dreams
# Kids
# Alright
# Done
```

`print(song)` is indented, so it's inside the loop and runs three times. `print("Done")` is not indented, so it's outside the loop and runs once, after the loop finishes.

## The loop variable

The name after `for` is yours to pick. `song`, `s`, `item`, `x` — Python doesn't care. Pick something that says what the item *is*, so the body reads like English.

It's an ordinary variable. Python reassigns it before each pass, and it's still around after the loop ends, holding the last value:

```python
for letter in ["a", "b", "c"]:
    print(letter)
print("after the loop, letter is", letter)
# a
# b
# c
# after the loop, letter is c
```

If the loop never runs — because the list is empty — the body is skipped entirely and nothing happens:

```python
for x in []:
    print("this never prints")
print("the loop is over")
# the loop is over
```

## Looping over a string

A string is a sequence of characters, so a `for` loop walks it one character at a time. You don't need `len()` or indexes:

```python
for ch in "cat":
    print(ch)
# c
# a
# t
```

Spaces are characters too — they get their own pass:

```python
for ch in "hi there":
    print("[" + ch + "]")
# [h]
# [i]
# [ ]
# [t]
# [h]
# [e]
# [r]
# [e]
```

## `range(n)`

Sometimes you want to do something a certain number of times and there's no list to loop over. That's what `range()` is for:

```python
for i in range(5):
    print(i)
# 0
# 1
# 2
# 3
# 4
```

`range(5)` gives you five numbers: **0, 1, 2, 3, 4**. It starts at 0 and stops *before* 5.

You don't have to use the number. If you just want the body to run n times, loop and ignore it:

```python
for i in range(3):
    print("beep")
# beep
# beep
# beep
```

When you truly don't use the loop variable, Python programmers conventionally name it `_`. It's a normal name that means "I'm not using this":

```python
for _ in range(2):
    print("knock knock")
# knock knock
# knock knock
```

## `range(a, b)`

Give `range()` two numbers and it starts at the first and stops before the second:

```python
for n in range(1, 5):
    print(n)
# 1
# 2
# 3
# 4
```

`range(1, 5)` is 1, 2, 3, 4. The start is **included**, the stop is **not**.

A handy trick for seeing what a range holds: wrap it in `list()`. A `range` doesn't print its numbers on its own.

```python
print(range(1, 5))
print(list(range(1, 5)))
# range(1, 5)
# [1, 2, 3, 4]
```

## Range stops before the end

This is the single most common `range` mistake, and it's worth burning into your memory now.

> **Misconception: `range(1, 10)` includes 10.** It does not. `range` always stops *before* the stop number. `range(1, 10)` gives you 1 through 9 — nine numbers, not ten. Nothing errors; you just silently lose the last one.

Proof:

```python
print(list(range(1, 10)))
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

If you want 1 through 10, ask for `range(1, 11)`:

```python
print(list(range(1, 11)))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

Why would anyone design it that way? Because it makes `range(len(...))` line up perfectly with a list's indexes. A list of 3 items has indexes 0, 1, 2 — and `range(3)` is exactly 0, 1, 2:

```python
letters = ["a", "b", "c"]
print(len(letters))
print(list(range(len(letters))))
# 3
# [0, 1, 2]
```

```python
letters = ["a", "b", "c"]
for i in range(len(letters)):
    print(i, letters[i])
# 0 a
# 1 b
# 2 c
```

Two more consequences that follow from the same rule:

- `range(n)` always gives exactly **n** numbers. `range(5)` gives 5 numbers.
- `range(a, b)` gives exactly **b - a** numbers. `range(3, 7)` gives 4 numbers.

```python
print(len(range(5)))
print(len(range(3, 7)))
# 5
# 4
```

## `range(a, b, step)`

A third number is the **step** — how far to jump each time:

```python
for n in range(0, 10, 2):
    print(n)
# 0
# 2
# 4
# 6
# 8
```

Still stops before 10. Step counts by 5s:

```python
print(list(range(0, 26, 5)))
# [0, 5, 10, 15, 20, 25]
```

A **negative** step counts down. The stop rule doesn't change — it still stops *before* the stop number:

```python
for n in range(5, 0, -1):
    print(n)
print("Liftoff!")
# 5
# 4
# 3
# 2
# 1
# Liftoff!
```

`range(5, 0, -1)` is 5, 4, 3, 2, 1 — it stops before 0, so 0 never appears. If you want to reach 0, count down to `-1`:

```python
print(list(range(5, -1, -1)))
# [5, 4, 3, 2, 1, 0]
```

> **Watch out: a range that goes the wrong way is empty, not an error.** `range(5, 0)` asks to count *up* from 5 to 0, which is impossible, so you get zero numbers and your loop body never runs. No error message, no output — just silence. If a loop mysteriously does nothing, print `list(your_range)` and look at it.

```python
print(list(range(5, 0)))
for n in range(5, 0):
    print("this never prints")
# []
```

## `enumerate()`

Often you want both the item *and* its position. You could do it with `range(len(...))` and index in by hand, but there's a cleaner way built for exactly this:

```python
playlist = ["Dreams", "Kids", "Alright"]

for i, song in enumerate(playlist):
    print(i, song)
# 0 Dreams
# 1 Kids
# 2 Alright
```

`enumerate()` hands you **two** things each pass, so you name two variables: the position first, the item second. Positions start at 0, like every index in Python.

For a numbered list a human will read, you want to start at 1. `enumerate` takes a `start`:

```python
playlist = ["Dreams", "Kids", "Alright"]

for i, song in enumerate(playlist, start=1):
    print(f"{i}. {song}")
# 1. Dreams
# 2. Kids
# 3. Alright
```

Compare the two ways of getting a position. Both work; the second is what you'll see in real code:

```python
names = ["ada", "alan"]

for i in range(len(names)):
    print(i, names[i])

for i, name in enumerate(names):
    print(i, name)
# 0 ada
# 1 alan
# 0 ada
# 1 alan
```

## The accumulator pattern

This is the most important thing on this page. Learn this pattern and half of programming opens up.

The idea: a loop can only look at one item at a time. So to compute something about *all* of them — a total, a count, a longest word — you keep a variable **outside** the loop that remembers the answer so far, and you update it a little on every pass.

It's always three steps:

1. **Before** the loop, create the variable with a starting value.
2. **Inside** the loop, update it.
3. **After** the loop, use it.

```python
prices = [3, 5, 2]

total = 0
for p in prices:
    total += p
print(total)
# 10
```

`total += p` is shorthand for `total = total + p` — "make total its old value plus p."

Watch it happen. Print `total` on every pass and you can see it grow:

```python
prices = [3, 5, 2]

total = 0
for p in prices:
    total += p
    print("added", p, "and total is now", total)
print("final total:", total)
# added 3 and total is now 3
# added 5 and total is now 8
# added 2 and total is now 10
# final total: 10
```

Trace it in your head, pass by pass:

- Before the loop: `total` is 0.
- Pass 1: `p` is 3. `total` becomes 0 + 3 = 3.
- Pass 2: `p` is 5. `total` becomes 3 + 5 = 8.
- Pass 3: `p` is 2. `total` becomes 8 + 2 = 10.
- Loop ends. `total` is 10.

### Where the starting value goes

> **Misconception: putting `total = 0` inside the loop.** This is the number one accumulator bug. If the reset line is indented into the loop, it runs *again on every pass* — wiping out everything you've added so far. Your total ends up being just the last item. No error, no warning, wrong answer.

The broken version. Look only at the indentation — everything else is identical to the working one:

```python
prices = [3, 5, 2]

for p in prices:
    total = 0
    total += p
print(total)
# 2
```

10 was the right answer; it says 2 — the last price. Every pass threw away the running total and started over.

Print it as it goes and the bug is obvious:

```python
prices = [3, 5, 2]

for p in prices:
    total = 0
    total += p
    print("total is now", total)
# total is now 3
# total is now 5
# total is now 2
```

The total never grows past a single item. The fix is one level of indentation — move the reset **above** the loop:

```python
prices = [3, 5, 2]

total = 0
for p in prices:
    total += p
print(total)
# 10
```

**The rule: the accumulator is created once, before the loop. It is only *updated* inside.** If the line that sets it back to its starting value is indented, it's in the wrong place.

### The starting value must match the type

Not every accumulator starts at 0. It starts at whatever "nothing yet" means for the thing you're building:

- adding up numbers: start at `0`
- building a string: start at `""`
- building a list: start at `[]`
- multiplying numbers: start at `1` (starting at 0 would keep it 0 forever)

```python
letters = ["p", "y", "t", "h", "o", "n"]

word = ""
for ch in letters:
    word += ch
print(word)
# python
```

```python
numbers = [2, 3, 4]

product = 1
for n in numbers:
    product *= n
print(product)
# 24
```

Predict this one before you run it — what happens if you start the product at 0 instead of 1?

```python
numbers = [2, 3, 4]

product = 0
for n in numbers:
    product *= n
print(product)
```

Every pass multiplies by 0, so it stays 0 forever:

```
0
```

### The accumulator inside a function

Everything above works the same inside a function — with one new trap.

> **Misconception: putting `return` inside the loop.** `return` doesn't just hand back a value, it **ends the function immediately**. If it's indented into the loop, the function quits during the very first pass and the loop never gets to pass 2.

```python
def total_of(prices):
    total = 0
    for p in prices:
        total += p
        return total

print(total_of([3, 5, 2]))
# 3
```

It returned 3 — the first price. The loop added 3, hit `return`, and the function was over. Prices 5 and 2 were never even looked at.

The fix is the same kind of fix as before: indentation. `return` belongs **after** the loop, at the same indentation as the `for`:

```python
def total_of(prices):
    total = 0
    for p in prices:
        total += p
    return total

print(total_of([3, 5, 2]))
print(total_of([10, 10]))
print(total_of([]))
# 10
# 20
# 0
```

Notice the empty list gives 0 for free — the loop just never ran, so `total` kept its starting value. That's another reason the starting value lives outside the loop.

Line them up side by side. The only difference is where `return` sits:

```python
def wrong(prices):
    total = 0
    for p in prices:
        total += p
        return total          # inside the loop: quits on pass 1

def right(prices):
    total = 0
    for p in prices:
        total += p
    return total              # after the loop: quits when the loop is done

print(wrong([3, 5, 2]))
print(right([3, 5, 2]))
# 3
# 10
```

(Python does have `sum()` built in, so you'd never really write `total_of` — but the pattern behind it is the thing you'll use forever.)

## Counting with a condition

Counting is an accumulator that goes up by 1 instead of by the item — and only when an `if` says so:

```python
scores = [8, 6, 10, 7, 9]

passed = 0
for s in scores:
    if s >= 7:
        passed += 1
print(passed)
# 4
```

The `if` is inside the loop, and `passed += 1` is inside the `if`. Read the indentation: for each score, *if* it's 7 or more, bump the counter.

```python
word = "programming"

count = 0
for ch in word:
    if ch in "aeiou":
        count += 1
print("vowels:", count)
# vowels: 3
```

You can count and total at the same time — just keep two accumulators:

```python
scores = [8, 6, 10, 7, 9]

total = 0
passed = 0
for s in scores:
    total += s
    if s >= 7:
        passed += 1
print("total:", total)
print("passed:", passed)
print("average:", total / len(scores))
# total: 40
# passed: 4
# average: 8.0
```

Predict this before you run it. How many of these are longer than 3 letters?

```python
words = ["hi", "tree", "a", "birds", "ok", "cat"]

count = 0
for w in words:
    if len(w) > 3:
        count += 1
print(count)
```

Only `"tree"` and `"birds"` clear the bar — `"cat"` is exactly 3, and `>` is not `>=`:

```
2
```

## Building a list in a loop

Same pattern, but the accumulator is a list that starts empty and grows with `.append()`:

```python
names = ["ada", "grace", "alan"]

shouty = []
for n in names:
    shouty.append(n.upper())
print(shouty)
# ['ADA', 'GRACE', 'ALAN']
```

`.append(x)` adds `x` to the end of the list. It changes the list in place — it does not give you a new one, so never write `shouty = shouty.append(...)`.

Add an `if` and you're **filtering** — keeping only the items you want:

```python
numbers = [4, 9, 12, 3, 20]

big = []
for n in numbers:
    if n > 5:
        big.append(n)
print(big)
# [9, 12, 20]
```

Transform and filter at once:

```python
words = ["hi", "elephant", "cat", "hippopotamus"]

long_words = []
for w in words:
    if len(w) > 3:
        long_words.append(w.upper())
print(long_words)
print(len(long_words))
# ['ELEPHANT', 'HIPPOPOTAMUS']
# 2
```

## Finding the max by hand

To find the biggest item you can't just look at one at a time and know — so you keep a "best so far" and replace it whenever you see something better:

```python
scores = [8, 6, 10, 7]

best = scores[0]
for s in scores:
    if s > best:
        best = s
print(best)
# 10
```

Notice the starting value: **the first item**, not 0. That matters more than it looks.

> **Watch out: starting `best = 0` breaks on negative numbers.** The "best so far" has to start as something that's actually in the list. If you start at 0 and every item is below 0, nothing ever beats it, and you return a number that was never in your data.

```python
temps = [-5, -12, -3]

best = 0
for t in temps:
    if t > best:
        best = t
print(best)
# 0   <- wrong: 0 isn't even in the list
```

Start at the first item and it's right:

```python
temps = [-5, -12, -3]

best = temps[0]
for t in temps:
    if t > best:
        best = t
print(best)
# -3
```

The same pattern finds the *longest* — you just compare something other than the item itself. This is why the pattern is worth knowing even though `max()` exists:

```python
words = ["hi", "elephant", "cat"]

longest = words[0]
for w in words:
    if len(w) > len(longest):
        longest = w
print(longest)
# elephant
```

Want to know *where* the best one was, not just what it was? Use `enumerate` and remember the index too:

```python
scores = [8, 6, 10, 7]

best = scores[0]
best_i = 0
for i, s in enumerate(scores):
    if s > best:
        best = s
        best_i = i
print("best score:", best)
print("at position:", best_i)
# best score: 10
# at position: 2
```

## `break`

`break` leaves the loop **immediately** — no more passes, even if there are items left:

```python
numbers = [3, 7, 12, 5, 9]

for n in numbers:
    print("checking", n)
    if n > 10:
        print("found one bigger than 10:", n)
        break
print("done")
# checking 3
# checking 7
# checking 12
# found one bigger than 10: 12
# done
```

It never checked 5 or 9. That's the point — once you've found what you're searching for, there's no reason to keep looking.

`break` only exits the loop it's in, and execution continues on the first line after the loop.

## `continue`

`continue` skips the **rest of this pass** and jumps straight to the next item. The loop keeps going:

```python
for n in range(1, 8):
    if n % 2 == 0:
        continue
    print(n)
# 1
# 3
# 5
# 7
```

Every even number hits `continue`, so its `print` is skipped — but the loop moves on to the next number instead of stopping.

The difference in one sentence: **`break` ends the whole loop; `continue` ends only the current lap.** Same loop, one word changed:

```python
for n in [1, 2, 3, 4]:
    if n == 3:
        break
    print(n)
print("now the same loop with continue")
for n in [1, 2, 3, 4]:
    if n == 3:
        continue
    print(n)
# 1
# 2
# now the same loop with continue
# 1
# 2
# 4
```

`continue` is often just an `if` turned inside out. These two do the same thing — use whichever reads better:

```python
names = ["ada", "", "grace"]

for n in names:
    if n == "":
        continue
    print(n)

for n in names:
    if n != "":
        print(n)
# ada
# grace
# ada
# grace
```

## `while`

A `for` loop runs once per item. A `while` loop runs **as long as a condition is True** — use it when you don't know in advance how many passes you need.

```python
count = 3
while count > 0:
    print(count)
    count -= 1
print("Go!")
# 3
# 2
# 1
# Go!
```

Read it as: "while count is greater than 0, do this." Python checks the condition, runs the body, checks again, runs again... and the moment the check is `False`, it stops and moves on.

Every correct `while` loop has three parts, and if you're missing one you have a bug:

1. something **set up before** the loop (`count = 3`)
2. a **condition** that can become `False`
3. something **inside the body that changes** what the condition looks at (`count -= 1`)

Here's a job a `for` loop can't easily do: keep doubling until you pass 100. You don't know how many passes that takes until you run it.

```python
value = 1
passes = 0
while value < 100:
    value *= 2
    passes += 1
print("value:", value)
print("passes:", passes)
# value: 128
# passes: 7
```

Rule of thumb: if you know the items or the count, use `for`. If you're waiting for a condition to flip, use `while`.

### The infinite loop

> **Misconception: the condition updates itself.** It does not. Python re-checks the condition, but nothing changes `count` unless *you* write the line that changes it. Forget it and the condition stays `True` forever — the loop never ends, your program hangs, and you have to force-stop it.

This is the bug. Do **not** run it — `count` is never changed, so `count > 0` is `True` forever:

```
count = 3
while count > 0:
    print(count)

# 3
# 3
# 3
# 3
# ... forever, until you stop it yourself
```

The fix is the missing line — the one that moves `count` toward the condition being `False`:

```python
count = 3
while count > 0:
    print(count)
    count -= 1
# 3
# 2
# 1
```

If you do hang your program, stop it — the Run button will offer a stop, and in a terminal it's Ctrl+C. Then look at your loop and ask the one diagnostic question: **which line in the body changes the thing the condition tests?** If you can't point at it, that's your bug.

A subtler version: the body changes *a* variable, just not the one the condition tests.

```
i = 0
total = 0
while i < 3:
    total += i
    total += 1

# nothing prints, and it never ends: `i` stays 0 forever
```

Sometimes an infinite loop is on purpose — `while True` never stops on its own, so you `break` out of it:

```python
n = 0
while True:
    n += 1
    if n * n > 50:
        break
print(n)
# 8
```

That's a deliberate infinite loop with a deliberate exit. If you write `while True`, make sure you can point at the `break`.

## Modifying a list while looping

> **Misconception: it's safe to remove items from the list you're looping over.** It is not. The loop keeps its place by position, so when you delete an item everything after it shifts back one — and the loop's next step jumps straight over the item that moved into the empty slot. It skips items. It does not crash, so you may not notice.

```python
numbers = [1, 2, 2, 3]

for n in numbers:
    if n == 2:
        numbers.remove(n)
print(numbers)
# [1, 2, 3]
```

Both 2s were supposed to go, and one survived. Here's why:

- Position 0 holds 1. Not a 2, keep going.
- Position 1 holds 2. Remove it. The list is now `[1, 2, 3]` — the second 2 slid down into position 1, the slot the loop has *already passed*.
- The loop moves to position 2, which now holds 3. The second 2 was never examined.
- Position 3 doesn't exist anymore. The loop ends.

The fix: **don't edit the list you're looping over — build a new one.**

```python
numbers = [1, 2, 2, 3]

kept = []
for n in numbers:
    if n != 2:
        kept.append(n)
print(kept)
# [1, 3]
```

If you need the original variable to hold the result, assign the new list back to it afterwards:

```python
numbers = [1, 2, 2, 3]

kept = []
for n in numbers:
    if n != 2:
        kept.append(n)
numbers = kept
print(numbers)
# [1, 3]
```

The same warning applies to `.append()` inside a loop over that same list — you'd be adding items the loop then has to visit, which is a genuine infinite loop.

## Nested loops

A loop can live inside another loop. The **inner loop runs all the way through, for every single pass of the outer loop**:

```python
sizes = ["S", "M"]
colors = ["red", "blue", "green"]

for size in sizes:
    for color in colors:
        print(size, color)
# S red
# S blue
# S green
# M red
# M blue
# M green
```

2 sizes × 3 colors = 6 lines. That multiplication is the thing to remember: nesting doesn't add work, it **multiplies** it. Two loops over 1,000 items each is a million passes.

The indentation tells you which loop a line belongs to:

```python
for size in ["S", "M"]:
    print("size:", size)
    for color in ["red", "blue"]:
        print("   ", size, color)
    print("   finished size", size)
# size: S
#     S red
#     S blue
#    finished size S
# size: M
#     M red
#     M blue
#    finished size M
```

`print("size:", size)` is indented once, so it runs per size (twice). The line inside the inner loop is indented twice, so it runs per size *per color* (four times).

Each loop needs its **own** variable name — here `i` for the outer and `j` for the inner. `i` holds still while `j` runs all the way through:

```python
for i in range(2):
    for j in range(3):
        print(i, j)
# 0 0
# 0 1
# 0 2
# 1 0
# 1 1
# 1 2
```

Reuse the same name for both and the inner loop overwrites it, so the outer loop loses track of where it was:

```python
for i in range(2):
    for i in range(3):
        pass
    print("outer thinks i is", i)
# outer thinks i is 2
# outer thinks i is 2
```

The outer loop should have seen `i` as 0 then 1. Instead it's 2 both times — whatever the inner loop left behind.

> **Watch out: `break` inside a nested loop only breaks the inner loop.** It does not escape both. The outer loop keeps right on going.

```python
for i in range(3):
    for j in range(3):
        if j == 1:
            break
        print(i, j)
# 0 0
# 1 0
# 2 0
```

## Worked example: a receipt

Several ideas at once: `enumerate` to pair up two lists, an accumulator for the total, a counter, and an f-string to format money.

```python
items = ["apple", "bread", "milk", "eggs"]
prices = [1.25, 3.50, 2.75, 4.00]

total = 0
expensive = 0
for i, item in enumerate(items):
    price = prices[i]
    total += price
    if price > 3:
        expensive += 1
    print(f"{item}: ${price:.2f}")

print(f"Items: {len(items)}")
print(f"Over $3: {expensive}")
print(f"Total: ${total:.2f}")
print(f"Average: ${total / len(items):.2f}")
# apple: $1.25
# bread: $3.50
# milk: $2.75
# eggs: $4.00
# Items: 4
# Over $3: 2
# Total: $11.50
# Average: $2.88
```

Everything that had to survive across passes — `total`, `expensive` — was created above the loop. Everything that only matters this pass — `item`, `price` — lives inside.

## Worked example: analysing a sentence

A total, a counter, a max-by-hand, and a list being built — four accumulators sharing one loop.

```python
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()

total_letters = 0
long_count = 0
longest = words[0]
capitalised = []

for w in words:
    total_letters += len(w)
    if len(w) > 3:
        long_count += 1
    if len(w) > len(longest):
        longest = w
    capitalised.append(w.capitalize())

print("words:", len(words))
print("letters:", total_letters)
print("longer than 3:", long_count)
print("longest word:", longest)
print("average length:", round(total_letters / len(words), 2))
print(" ".join(capitalised))
# words: 9
# letters: 35
# longer than 3: 5
# longest word: quick
# average length: 3.89
# The Quick Brown Fox Jumps Over The Lazy Dog
```

Note `longest` came out as `"quick"` even though `"brown"` and `"jumps"` are also 5 letters. The test is `>`, not `>=`, so a later tie never replaces the current best — the **first** longest wins. If you wanted the last one to win, you'd use `>=`. Neither is more correct; just know which one you asked for.

## Worked example: a guessing loop

A `while` loop with a `break`, plus a counter — the shape of nearly every "keep trying until it works" program.

```python
secret = 7
guesses = [3, 9, 5, 7, 2]

i = 0
tries = 0
found = False
while i < len(guesses):
    guess = guesses[i]
    tries += 1
    if guess == secret:
        found = True
        break
    if guess < secret:
        print(guess, "is too low")
    else:
        print(guess, "is too high")
    i += 1

print("found:", found)
print("tries:", tries)
# 3 is too low
# 9 is too high
# 5 is too low
# found: True
# tries: 4
```

The three `while` parts are all there: `i = 0` above the loop, `i < len(guesses)` as the condition, `i += 1` in the body. `found = False` is an accumulator too — it starts as "no" and only flips to "yes" if something in the loop says so. That's a very common little pattern.

## Quick reference — what's available

### Loop forms

- `for item in things:` — run the body once per item
- `for ch in "text":` — run the body once per character
- `for i in range(n):` — run the body n times, with `i` counting 0 to n-1
- `for _ in range(n):` — run the body n times, ignoring the number
- `for i, item in enumerate(things):` — position and item together
- `while condition:` — repeat as long as the condition is True
- `while True:` — repeat forever; you must `break` out
- `break` — leave the loop immediately
- `continue` — skip the rest of this pass, go to the next one

### `range()`

- `range(n)` — 0 up to n-1, that's n numbers
- `range(a, b)` — a up to b-1, stops BEFORE b
- `range(a, b, step)` — count by `step`
- `range(a, b, -1)` — count down; still stops before b
- `range(len(things))` — every index of `things`
- `list(range(...))` — see the actual numbers a range holds
- `len(range(...))` — how many numbers it holds

### Patterns to memorise

- total: `total = 0` before, `total += x` inside
- product: `product = 1` before, `product *= x` inside
- count: `count = 0` before, `count += 1` inside an `if`
- string: `text = ""` before, `text += ch` inside
- list: `out = []` before, `out.append(x)` inside
- filter: `out = []` before, `if test: out.append(x)` inside
- max by hand: `best = things[0]` before, `if x > best: best = x` inside
- flag: `found = False` before, `found = True` inside an `if`

### Built-ins that loop for you

- `sum(numbers)` — add them all up
- `len(things)` — how many
- `max(things)` / `min(things)` — largest / smallest
- `sorted(things)` — a new sorted list; `sorted(things, reverse=True)` for biggest first
- `reversed(things)` — loop back to front
- `zip(a, b)` — loop over two lists side by side
- `"sep".join(list_of_strings)` — glue a list of strings into one string
- `things.append(x)` — add one item to the end of a list

### Them all together

```python
scores = [7, 9, 4, 10, 6]

total = 0
best = scores[0]
passed = []
for s in scores:
    total += s
    if s > best:
        best = s
    if s >= 6:
        passed.append(s)

print("total by hand:", total, "and by sum():", sum(scores))
print("best by hand:", best, "and by max():", max(scores))
print("passed:", passed)
print("average:", round(total / len(scores), 2))

for rank, s in enumerate(sorted(scores, reverse=True), start=1):
    print(f"{rank}. {s}")

names = ["ada", "grace"]
ages = [36, 45]
for name, age in zip(names, ages):
    print(f"{name} is {age}")

print("-".join(["a", "b", "c"]))
# total by hand: 36 and by sum(): 36
# best by hand: 10 and by max(): 10
# passed: [7, 9, 10, 6]
# average: 7.2
# 1. 10
# 2. 9
# 3. 7
# 4. 6
# 5. 4
# ada is 36
# grace is 45
# a-b-c
```
