# Loops — for & range

Walking through strings and lists with `for`, and counting with `range`.

---

## count_vowels_in_phrase
kind: code_fn
title: Count the vowels
tags: loops, strings, functions
see: 07_loops#counting-with-a-condition
difficulty: easy
entry: count_vowels

### prompt
Create a function that counts how many characters of a phrase are vowels (a, e, i, o, u). Upper and lower case both count.

Examples

    count_vowels("banana") → 3
    count_vowels("Ohio") → 3
    count_vowels("rhythm") → 0

Notes

- "A" is a vowel just as much as "a".
- Spaces, digits and punctuation are never vowels.
- Don't forget to return the result.

### walkthrough
A `for` loop over a string hands you one character at a time:

    for ch in "cat":
        print(ch)      # c, then a, then t

So the plan is: start a counter at 0, look at each character, and add 1 when it is
a vowel. The test "is this a vowel?" is just `ch in "aeiou"` — the `in` operator
asks whether that one character appears anywhere in that little string.

The trap is case. "Ohio" starts with a capital O, and `"O" in "aeiou"` is False,
because Python compares characters exactly. Rather than writing out "aeiouAEIOU",
flatten the problem first with `phrase.lower()` and loop over that:

    def count_vowels(phrase):
        count = 0
        for ch in phrase.lower():
            if ch in "aeiou":
                count = count + 1
        return count

One more thing: `count = 0` must sit *above* the loop. Put it inside and you reset
your counter on every character, and the answer can never be bigger than 1.

### starter
```python
def count_vowels(phrase):
    
```

### solution
```python
def count_vowels(phrase):
    count = 0
    for ch in phrase.lower():
        if ch in "aeiou":
            count = count + 1
    return count
```

### check
count_vowels("banana") == 3
count_vowels("Ohio") == 3
count_vowels("rhythm") == 0
count_vowels("") == 0
count_vowels("AEIOU") == 5
count_vowels("hello world") == 3

---

## sum_page_numbers
kind: code_fn
title: Sum the page numbers
tags: loops, math, functions
see: 07_loops#range-stops-before-the-end
difficulty: easy
entry: sum_pages

### prompt
You photocopied every page from `first` to `last`. Create a function that returns the sum of all those page numbers, counting both the first and the last page.

Examples

    sum_pages(1, 5) → 15
    sum_pages(10, 12) → 33
    sum_pages(7, 7) → 7

Notes

- Both ends are included.
- `first` is never greater than `last`.

### walkthrough
`range(a, b)` produces the numbers starting at `a` and stopping *before* `b`. So
`range(1, 5)` is 1, 2, 3, 4 — the 5 never shows up. That is the single most common
off-by-one bug in Python, and it is exactly what this problem is about.

You want the pages 1 through 5 *inclusive*, so you have to ask for one past the end.
Then it is an ordinary accumulator: a running total created *before* the loop, and
one page added on each trip through it.

    def sum_pages(first, last):
        total = 0
        for page in range(first, last + 1):
            total = total + page
        return total

The `+ 1` is not a fudge factor — it is you saying "stop before last + 1", which is
the same as "include last". Check it against the edge case `sum_pages(7, 7)`:
`range(7, 8)` is just the number 7, so the answer is 7. If you had written
`range(7, 7)` you'd get nothing at all and the sum would be 0.

Once the `+ 1` makes sense to you, there is a shortcut: `sum` will run that same
accumulator loop for you, so `sum(range(first, last + 1))` does the whole job in one
line. Write the loop yourself first — the shortcut is only obvious once you have.

### starter
```python
def sum_pages(first, last):
    
```

### solution
```python
def sum_pages(first, last):
    total = 0
    for page in range(first, last + 1):
        total = total + page
    return total
```

### check
sum_pages(1, 5) == 15
sum_pages(10, 12) == 33
sum_pages(7, 7) == 7
sum_pages(1, 100) == 5050
sum_pages(2, 4) == 9

---

## mcq_range_step_countdown
kind: mcq
title: Predict the backwards countdown
tags: loops, predict, concept
see: 07_loops#range-a-b-step
difficulty: easy
answer: 1

### prompt
What does this print, one number per line?

    for n in range(10, 0, -3):
        print(n)

### choices
- 10, 7, 4, 1
- 10, 7, 4, 1, -2
- 1, 4, 7, 10
- 7, 4, 1

---

## number_the_playlist
kind: code_fn
title: Number the playlist
tags: loops, strings, formatting
see: 07_loops#enumerate
difficulty: medium
entry: number_playlist

### prompt
Create a function that takes a list of song titles and returns a list of numbered strings, starting the numbering at 1.

Examples

    number_playlist(["Hey Jude", "Yesterday"]) → ["1. Hey Jude", "2. Yesterday"]
    number_playlist(["Solo"]) → ["1. Solo"]
    number_playlist([]) → []

Notes

- The format is the number, a period, a single space, then the title.
- Return a new list — don't print anything.

### walkthrough
You need two things at once for each song: the title, and its position in the list.
A plain `for song in songs` gives you only the title. `enumerate` gives you both:

    for i, song in enumerate(["Hey Jude", "Yesterday"]):
        print(i, song)      # 0 Hey Jude,  then  1 Yesterday

Notice the numbers start at 0, because that's how Python indexes. But humans number
playlists from 1. The tempting fix is `i + 1` scattered through your code; the
cleaner one is to tell `enumerate` where to start:

    def number_playlist(songs):
        result = []
        for i, song in enumerate(songs, start=1):
            result.append(f"{i}. {song}")
        return result

The f-string does the gluing: `f"{i}. {song}"` drops the number in, then a literal
". ", then the title. Note the space after the period lives inside the quotes — if
you forget it you get "1.Hey Jude" and every check fails.

### starter
```python
def number_playlist(songs):
    
```

### solution
```python
def number_playlist(songs):
    result = []
    for i, song in enumerate(songs, start=1):
        result.append(f"{i}. {song}")
    return result
```

### check
number_playlist(["Hey Jude", "Yesterday"]) == ["1. Hey Jude", "2. Yesterday"]
number_playlist(["Solo"]) == ["1. Solo"]
number_playlist([]) == []
number_playlist(["a", "b", "c"]) == ["1. a", "2. b", "3. c"]

---

## mask_card_digits
kind: code_fn
title: Hide all but the last four
tags: loops, strings, indexing
see: 07_loops#enumerate
difficulty: medium
entry: mask_code

### prompt
Create a function that hides a code by replacing every character with `*`, except the last four, which stay as they are.

Examples

    mask_code("9876543210") → "******3210"
    mask_code("12345") → "*2345"
    mask_code("1234") → "1234"

Notes

- If the code is four characters or shorter, nothing is hidden.
- The result is the same length as the input.

### walkthrough
The question you must answer for each character is "am I in the last four?". To know
that, you need the character's *position*, not just the character — so loop with
`enumerate`, which hands you both:

    for i, ch in enumerate("12345"):
        ...    # i = 0, 1, 2, 3, 4 and ch = "1", "2", ...

Now do the arithmetic once, not per character. For a string of length 5, the last
four positions are 1, 2, 3, 4 — that is, every `i` where `i >= 5 - 4`. In general
the keeper positions are `i >= len(code) - 4`; everything else becomes a star.

    def mask_code(code):
        result = ""
        for i, ch in enumerate(code):
            if i >= len(code) - 4:
                result = result + ch
            else:
                result = result + "*"
        return result

The edge case to think about is a short code like "1234": `len(code) - 4` is 0, so
`i >= 0` is true for every character and nothing gets hidden — which is exactly the
behavior we asked for. The arithmetic handles it for free; you don't need a special
`if len(code) <= 4` branch.

### starter
```python
def mask_code(code):
    
```

### solution
```python
def mask_code(code):
    result = ""
    for i, ch in enumerate(code):
        if i >= len(code) - 4:
            result = result + ch
        else:
            result = result + "*"
    return result
```

### check
mask_code("9876543210") == "******3210"
mask_code("12345") == "*2345"
mask_code("1234") == "1234"
mask_code("12") == "12"
mask_code("") == ""
mask_code("abcdefgh") == "****efgh"

---

## fix_locker_numbers
kind: code_fn
title: The last locker is missing
tags: loops, bugs, arrays
see: 07_loops#range-stops-before-the-end
difficulty: easy
entry: locker_numbers

### prompt
`locker_numbers(n)` should return the list of locker numbers from 1 to `n`. Right now the hallway is missing its last locker — there is no locker `n`. Fix it.

Examples

    locker_numbers(3) → [1, 2, 3]
    locker_numbers(1) → [1]
    locker_numbers(0) → []

Notes

- The lockers are numbered starting at 1, like a real hallway.
- A hallway with 0 lockers is an empty list, not an error.

### starter
```python
def locker_numbers(n):
    lockers = []
    for i in range(1, n):
        lockers.append(i)
    return lockers
```

### solution
```python
def locker_numbers(n):
    lockers = []
    for i in range(1, n + 1):
        lockers.append(i)
    return lockers
```

### check
locker_numbers(3) == [1, 2, 3]
locker_numbers(1) == [1]
locker_numbers(0) == []
locker_numbers(5) == [1, 2, 3, 4, 5]

---

## fix_tip_total
kind: code_fn
title: The tip jar keeps emptying
tags: loops, bugs, functions
see: 07_loops#where-the-starting-value-goes
difficulty: medium
entry: total_tips

### prompt
`total_tips(tips)` should add up every tip in the list. Instead it always reports just the last one. Find out why and fix it.

Examples

    total_tips([3, 5, 2]) → 10
    total_tips([7]) → 7
    total_tips([]) → 0

Notes

- The bug is about *where* a line sits, not what it says.
- An empty list should give 0.

### walkthrough
Run the broken code in your head with `[3, 5, 2]`. First trip through the loop:
`total = 0`, then `total += 3` → 3. Second trip: `total = 0` *again* — that line is
inside the loop, so it runs every single time — then `total += 5` → 5. Third trip:
reset to 0, add 2 → 2. You return 2, the last tip. That matches the symptom exactly.

A variable that accumulates across a loop has to be created *once, before* the loop
starts. Inside the loop belongs only the work that changes each time:

    def total_tips(tips):
        total = 0
        for tip in tips:
            total += tip
        return total

Indentation is what says "before" versus "inside" in Python — moving `total = 0`
out one level is the entire fix. And notice the empty-list case falls out for free:
the loop body never runs, and you return the 0 you started with. If you had tried to
"fix" this by initializing `total = tips[0]`, an empty list would crash.

### starter
```python
def total_tips(tips):
    for tip in tips:
        total = 0
        total += tip
    return total
```

### solution
```python
def total_tips(tips):
    total = 0
    for tip in tips:
        total += tip
    return total
```

### check
total_tips([3, 5, 2]) == 10
total_tips([7]) == 7
total_tips([]) == 0
total_tips([1, 1, 1, 1]) == 4
total_tips([10, 0, 5]) == 15

---

## longest_same_letter_run
kind: code_fn
title: Longest streak of the same letter
tags: loops, strings, algorithms
see: 07_loops#finding-the-max-by-hand
difficulty: hard
entry: longest_run

### prompt
Create a function that returns the length of the longest streak of identical characters sitting next to each other in a string.

Examples

    longest_run("aaabbbbcc") → 4
    longest_run("abc") → 1
    longest_run("") → 0

Notes

- The characters in a streak must be consecutive.
- An empty string has no streak, so the answer is 0.

### walkthrough
The instinct is to count each letter's total, but that's a different question:
"abab" has two a's, yet its longest *streak* is 1, because they aren't next to each
other. You have to walk the string in order and watch for the moment it breaks.

Carry two numbers as you go. `current` is how long the streak you're standing in is;
`best` is the longest one you've finished so far. For each character, ask only one
thing: is this the same as the character just before me?

    def longest_run(text):
        best = 0
        current = 0
        for i, ch in enumerate(text):
            if i > 0 and ch == text[i - 1]:
                current = current + 1
            else:
                current = 1
            best = max(best, current)
        return best

Two details matter. First, `i > 0` guards the very first character — without it,
`text[i - 1]` is `text[-1]`, which is the *last* character of the string, and you'd
silently compare the wrong things. Second, update `best` on every character, not
only when the streak ends. Otherwise a string that ends mid-streak, like "aabbb",
never gets its final run counted.

Empty string: the loop never runs and `best` stays 0, which is the answer we want.

### starter
```python
def longest_run(text):
    
```

### solution
```python
def longest_run(text):
    best = 0
    current = 0
    for i, ch in enumerate(text):
        if i > 0 and ch == text[i - 1]:
            current = current + 1
        else:
            current = 1
        best = max(best, current)
    return best
```

### check
longest_run("aaabbbbcc") == 4
longest_run("abc") == 1
longest_run("") == 0
longest_run("a") == 1
longest_run("abab") == 1
longest_run("aabbb") == 3
longest_run("xxxxx") == 5

---

## sum_every_other_digit
kind: code_fn
title: Every other digit, from the right
tags: loops, indexing, strings
see: 07_loops#range-a-b-step
difficulty: hard
entry: alt_sum

### prompt
Create a function that takes a string of digits and adds up the rightmost digit, the digit two places to its left, the one two places left of that, and so on.

Examples

    alt_sum("1234") → 6
    alt_sum("13579") → 15
    alt_sum("7") → 7

Notes

- In "1234" you add 4 + 2. In "13579" you add 9 + 5 + 1.
- An empty string sums to 0.
- Each character of the string is a digit, so you'll need int() to do arithmetic.

### walkthrough
Counting from the right is easier if you walk the *indexes* backwards instead of the
characters. `range` takes three arguments — start, stop, step — and the step can be
negative:

    range(len(digits) - 1, -1, -2)

Read it piece by piece. Start at `len(digits) - 1`, the index of the last character
(for "1234" that's index 3, the "4"). Step by `-2`, so you skip every other one: 3,
1. Stop before `-1`, which means index 0 is still included — the classic mistake is
writing `range(len(digits) - 1, 0, -2)`, whose stop of 0 means index 0 gets skipped,
so `alt_sum("13579")` quietly loses the leading 1 and returns 14 instead of 15.

Then it's an ordinary accumulator, remembering that `digits[i]` is the *character*
"4", not the number 4 — `"4" + "2"` would give you "42".

    def alt_sum(digits):
        total = 0
        for i in range(len(digits) - 1, -1, -2):
            total = total + int(digits[i])
        return total

### starter
```python
def alt_sum(digits):
    
```

### solution
```python
def alt_sum(digits):
    total = 0
    for i in range(len(digits) - 1, -1, -2):
        total = total + int(digits[i])
    return total
```

### check
alt_sum("1234") == 6
alt_sum("13579") == 15
alt_sum("7") == 7
alt_sum("") == 0
alt_sum("00") == 0
alt_sum("987654") == 18
