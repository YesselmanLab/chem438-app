# Strings — indexing & slicing

Reaching into strings by position: single characters, slices, reversing, splitting, and joining.

---

## ticket_last_two
kind: code_fn
title: Ticket check characters
tags: strings, indexing, language_fundamentals
difficulty: easy
entry: last_two

### prompt
Every ticket code ends in a two-character check block. Create a function that takes
a ticket code as a string and returns its last two characters. If the code is only
one character long, return that one character.

Examples

    last_two("A7X9") → "X9"
    last_two("ZZ100") → "00"
    last_two("Q") → "Q"

Notes

- Negative positions count from the right-hand end of the string, so you never have
  to count the characters yourself.
- A slice can start at a negative position and run to the end.
- The code always has at least one character.
- Don't forget to return the result.

### walkthrough
The tempting first move is an index: code[-2]. Try it on "A7X9" and you get "X" —
a single character, not "X9". An index hands back one character. You want two, so
you need a slice.

Slices are written word[start:stop], and either end may be left out, which means
"go all the way". Negative positions count from the right: -1 is the last
character, -2 is the second-to-last. So "start two from the end, and run to the
end" is:

    "A7X9"[-2:]    is  "X9"
    "ZZ100"[-2:]   is  "00"

    def last_two(code):
        return code[-2:]

Now the case you were about to special-case with an if. What does "Q"[-2:] do?
There is no second-to-last character. An *index* out of range raises IndexError, but
a *slice* out of range does not — Python silently clamps it to the nearest real
position, so "Q"[-2:] is just "Q". That is exactly the answer the prompt asks for,
so the one-character rule needs no code at all.

Do not write code[-2:-1]. That stops *before* the last character and gives you "X",
not "X9". Leaving the stop empty is what carries the slice to the end.

### starter
```python
def last_two(code):
    
```

### solution
```python
def last_two(code):
    return code[-2:]
```

### check
last_two("A7X9") == "X9"
last_two("ZZ100") == "00"
last_two("Q") == "Q"
last_two("bus-pass") == "ss"
last_two("42") == "42"

---

## mcq_slice_end
kind: mcq
title: Where does a slice stop?
tags: strings, indexing, predict
difficulty: easy
answer: 1

### prompt
Read the code carefully and predict exactly what it prints.

    s = "playlist"
    print(s[2:5])

Notes

- Counting starts at 0, so s[0] is "p".
- A slice s[a:b] starts at index a. Think hard about whether index b is included.

### choices
- ayl
- ayli
- lay
- yli

---

## written_in_substring
kind: written
title: Why "cat" is in "concatenate"
tags: strings, concept, written
difficulty: easy

### prompt
In Python, the expression below evaluates to True, even though the word
"concatenate" has nothing to do with cats.

    "cat" in "concatenate"

In a sentence or two, explain in your own words why Python says True here. Then
say what this tells you about using `in` when what you actually want is to find a
whole word inside a sentence.

Notes

- Look at the letters of "concatenate" one stretch at a time.
- This is not auto-graded — your reasoning is the answer.

---

## plate_palindrome
kind: code_fn
title: Reversible license plate
tags: strings, indexing, logic
difficulty: medium
entry: is_reversible

### prompt
A license plate is "reversible" if it reads exactly the same forwards and
backwards. Create a function that takes a plate as a string and returns True if it
is reversible and False otherwise.

Examples

    is_reversible("ABA") → True
    is_reversible("XYZ") → False
    is_reversible("77") → True

Notes

- The slice plate[::-1] gives you the whole string reversed.
- Two strings can be compared with == just like two numbers.
- Return the boolean True or False, not the string "True".

### walkthrough
The wording ("reads the same forwards and backwards") tempts people into a loop
that walks from both ends at once. You don't need it. Python can hand you the
reversed string in one step, and compare it in one more.

The slice plate[::-1] means "take the whole string, stepping by -1" — that is,
walk it backwards:

    "ABA"[::-1]   is  "ABA"
    "XYZ"[::-1]   is  "ZYX"

So the plate is reversible exactly when the reversed copy equals the original:

    def is_reversible(plate):
        return plate == plate[::-1]

Here's the mistake waiting for you. Many students write:

    if plate == plate[::-1]:
        return True
    else:
        return False

That works, but notice what you did: `plate == plate[::-1]` is *already* True or
False. Wrapping a boolean in an if just to hand back the same boolean is extra
typing that can go wrong. Return the comparison itself.

One more trap, for when you meet this on a list instead of a string. Python has a
built-in called `reversed()`, and it looks like the obvious tool:

    reversed([1, 2, 1]) == [1, 2, 1]      is False — always

That is not a bug in your logic. `reversed()` doesn't hand you a list; it hands
back a lazy "I'll go backwards when you ask" object, and such an object is never
equal to a list. You have to ask for the list: `list(reversed(x)) == x`. The [::-1]
slice sidesteps the whole problem, which is one reason to prefer it.

### starter
```python
def is_reversible(plate):
    
```

### solution
```python
def is_reversible(plate):
    return plate == plate[::-1]
```

### check
is_reversible("ABA") is True
is_reversible("XYZ") is False
is_reversible("77") is True
is_reversible("A") is True
is_reversible("AB") is False

---

## count_words_in_message
kind: code_fn
title: How many words in the message
tags: strings, arrays, language_fundamentals
difficulty: easy
entry: word_count

### prompt
Create a function that takes a text message as a string and returns how many words
it contains. Words are separated by one or more spaces.

Examples

    word_count("call me back") → 3
    word_count("hello") → 1
    word_count("running    late    sorry") → 3

Notes

- An empty message contains 0 words.
- Splitting a string turns it into a list of its words, and extra spaces between
  words should not change the count.
- Don't forget to return the result.

### walkthrough
The instinct almost everyone has first is to count the spaces and add one: three
words have two spaces between them, so surely

    def word_count(message):
        return message.count(" ") + 1

Check it against the examples before you trust it. "call me back" has two spaces →
3. Correct. Now "running    late    sorry": that is four spaces between each pair,
eight spaces in all, so this returns 9. And "" has no spaces at all, so it returns
1 — an empty message with one word in it. The rule "words are separated by spaces"
is true, but counting the separators is not the same as counting the words.

Let Python find the words instead. message.split() with no argument splits on any
run of whitespace and throws the blanks away:

    "call me back".split()              is  ["call", "me", "back"]
    "running    late    sorry".split()  is  ["running", "late", "sorry"]
    "".split()                          is  []

Every awkward case handled: runs of spaces collapse, and the empty message gives an
empty list. Then len() of that list is the count:

    def word_count(message):
        return len(message.split())

Note the no-argument part. message.split(" ") splits on each single space, keeping
the empty strings between doubled spaces — and it lands you right back in the
counting-separators trap.

### starter
```python
def word_count(message):
    
```

### solution
```python
def word_count(message):
    return len(message.split())
```

### check
word_count("call me back") == 3
word_count("hello") == 1
word_count("running    late    sorry") == 3
word_count("see you at the front door soon") == 7
word_count("") == 0

---

## fix_find_decaf
kind: code_fn
title: The broken decaf detector
tags: strings, bugs, conditions
difficulty: medium
entry: has_decaf

### prompt
A cafe app reads the note a customer typed with their order and reports whether
they asked for decaf. The code below looks reasonable and is badly wrong. Fix it.

Examples

    has_decaf("one decaf latte") → True
    has_decaf("large latte") → False
    has_decaf("decaf") → True

Notes

- order.find("decaf") returns the index where "decaf" starts, or -1 if it isn't
  there at all.
- Ask yourself what index a match at the very start of the string gets, and
  whether Python treats that number as true or false.

### walkthrough
Start by printing what .find() actually gives back, because the bug lives there:

    "one decaf latte".find("decaf")   is  4
    "decaf".find("decaf")             is  0
    "large latte".find("decaf")       is  -1

Now read the broken line: `if order.find("decaf"):`. That asks "is this number
truthy?" — not "did we find it?". In Python, every number is truthy except 0. So:

- "decaf" found at index 0 → 0 → falsy → the function says False. Wrong.
- "decaf" not found at all → -1 → truthy (it is not zero!) → says True. Wrong.

This is the classic .find() trap: the two answers get swapped exactly backwards
for the not-found case, and an order that *starts* with "decaf" quietly slips
through. The fix is to compare against the sentinel value instead of leaning on
truthiness:

    def has_decaf(order):
        return order.find("decaf") != -1

If -1 feels fiddly, `return "decaf" in order` does the same job and is what most
Python programmers would actually write. Either one passes.

### starter
```python
def has_decaf(order):
    if order.find("decaf"):
        return True
    return False
```

### solution
```python
def has_decaf(order):
    return order.find("decaf") != -1
```

### check
has_decaf("one decaf latte") is True
has_decaf("large latte") is False
has_decaf("decaf") is True
has_decaf("") is False
has_decaf("two decafs please") is True

---

## format_bus_route
kind: code_fn
title: Build the route string
tags: strings, arrays, formatting
difficulty: easy
entry: route_label

### prompt
Create a function that takes a list of bus stop names and returns a single string
showing the route, with the stops joined by an arrow " -> ".

Examples

    route_label(["Oak", "Elm", "Pine"]) → "Oak -> Elm -> Pine"
    route_label(["Main", "5th"]) → "Main -> 5th"
    route_label(["Depot"]) → "Depot"

Notes

- join builds one string out of a list, using the string you call it on as the glue
  between the items.
- Notice there is no arrow before the first stop or after the last one.
- An empty list of stops should give back an empty string.
- Return the string — do not print it.

### starter
```python
def route_label(stops):
    
```

### solution
```python
def route_label(stops):
    return " -> ".join(stops)
```

### check
route_label(["Oak", "Elm", "Pine"]) == "Oak -> Elm -> Pine"
route_label(["Main", "5th"]) == "Main -> 5th"
route_label(["Depot"]) == "Depot"
route_label(["A", "B", "C", "D"]) == "A -> B -> C -> D"
route_label([]) == ""

---

## club_acronym
kind: code_fn
title: Acronym for the club name
tags: strings, loops, indexing
difficulty: hard
entry: acronym

### prompt
Clubs make acronyms by taking the first letter of each important word and skipping
the little ones. Create a function that takes a club name and returns the uppercase
first letters of every word that is 3 or more letters long.

Examples

    acronym("friends of the reading room") → "FTRR"
    acronym("board game night") → "BGN"
    acronym("cat in a box") → "CB"

Notes

- Words are separated by single spaces.
- Skip any word shorter than 3 letters — "of", "a" and "in" contribute nothing,
  but "the" is 3 letters long, so it stays.
- The answer is one string, not a list.

### walkthrough
Three small jobs, in order: break the name into words, pick the words you want,
take one letter from each — then glue the letters back into a string.

Step one, split it:

    "cat in a box".split()   is  ["cat", "in", "a", "box"]

Step two, keep only words with len(w) >= 3. That drops "in" and "a", leaving
["cat", "box"].

Step three, take w[0] from each and uppercase it: "C", "B".

Step four — the step people forget — glue them. If you stop at a list you return
["C", "B"], not "CB". "".join(...) with an *empty* separator sticks them together
with nothing in between:

    def acronym(name):
        letters = []
        for w in name.split():
            if len(w) >= 3:
                letters.append(w[0].upper())
        return "".join(letters)

Once that makes sense, the same logic compresses into one line:

    return "".join(w[0].upper() for w in name.split() if len(w) >= 3)

Write the loop version first. The one-liner is a reward for understanding it, not
a shortcut around it.

### starter
```python
def acronym(name):
    
```

### solution
```python
def acronym(name):
    return "".join(w[0].upper() for w in name.split() if len(w) >= 3)
```

### check
acronym("friends of the reading room") == "FTRR"
acronym("board game night") == "BGN"
acronym("cat in a box") == "CB"
acronym("Sunday Morning Run Club") == "SMRC"
acronym("in a of") == ""

---

## middle_chars
kind: code_fn
title: The middle of the password
tags: strings, indexing, math
difficulty: hard
entry: middle

### prompt
Create a function that takes a word and returns its middle. If the word has an odd
number of letters, return the single middle character. If it has an even number,
return the two middle characters.

Examples

    middle("cat") → "a"
    middle("code") → "od"
    middle("x") → "x"

Notes

- len(word) tells you which case you are in.
- // is integer division: 7 // 2 is 3, not 3.5.
- The word always has at least one character.

### walkthrough
The trap here is thinking of this as two unrelated problems. It's one slice with
carefully chosen bounds — but let's find them by hand first.

Write out "code" (length 4) with its indices: c=0, o=1, d=2, e=3. You want "od",
which is word[1:3]. Now "cat" (length 3): c=0, a=1, t=2. You want "a", which is
word[1:2].

So the start is 1 in both cases and the stop is 3 then 2. Hunt for formulas:

    start:  (3 - 1) // 2 = 1   and   (4 - 1) // 2 = 1     → (len - 1) // 2
    stop:   3 // 2 + 1  = 2    and   4 // 2 + 1  = 3      → len // 2 + 1

One slice covers both:

    def middle(word):
        return word[(len(word) - 1) // 2 : len(word) // 2 + 1]

Why does this work? Integer division silently rounds down, and for odd lengths the
start and stop land one apart (one character), while for even lengths they land two
apart (two characters). The floor is doing the if/else for you.

The mistake to name: writing len(word) / 2. That gives 2.0, a float, and Python
refuses to index with a float — TypeError. Slices need ints, so use //.

If the single-slice version feels like magic, an if/else on len(word) % 2 is a
perfectly good answer. Get it right first, clever second.

### starter
```python
def middle(word):
    
```

### solution
```python
def middle(word):
    return word[(len(word) - 1) // 2 : len(word) // 2 + 1]
```

### check
middle("cat") == "a"
middle("code") == "od"
middle("x") == "x"
middle("ab") == "ab"
middle("testing") == "t"
middle("abcdef") == "cd"
