# Strings — more practice

Extra drills on strings: quotes, joining, repeating, length, indexing, slicing,
immutability, the common string methods, membership, converting between text and
numbers, and f-strings.

---

## p_repeat_ab
kind: mcq
title: Santa's laugh
tags: strings, predict, formatting
difficulty: easy
answer: 2

### prompt
What does this print?

    print("ho" * 3)

### code
print("ho" * 3)
### choices
- ho ho ho
- hohoho
- hohohoho
- ho3

---

## p_index_first_char
kind: mcq
title: The second letter, really
tags: strings, predict, indexing
difficulty: easy
answer: 2

### prompt
A username is stored below. What does this print?

    username = "pixel"
    print(username[1])

### code
username = "pixel"
print(username[1])
### choices
- p
- i
- x
- pi

---

## p_last_char_neg
kind: mcq
title: Grabbing the tail end
tags: strings, predict, indexing
difficulty: easy
answer: 2

### prompt
What does this print?

    print("taco"[-1])

### code
print("taco"[-1])
### choices
- t
- o
- c
- -1

---

## p_slice_1_4
kind: mcq
title: A slice of the weekday
tags: strings, predict, indexing
difficulty: easy
answer: 2

### prompt
What does this print?

    print("friday"[1:4])

### code
print("friday"[1:4])
### choices
- frid
- rid
- rida
- ri

---

## p_reverse_python
kind: mcq
title: Playing the word backwards
tags: strings, predict, indexing
difficulty: medium
answer: 2

### prompt
What does this print?

    print("stream"[::-1])

### code
print("stream"[::-1])
### choices
- stream
- maerts
- amerts
- maetrs

---

## p_len_with_space
kind: mcq
title: Does the space count?
tags: strings, predict
difficulty: easy
answer: 2

### prompt
You text your friend "good game". What does this print?

    print(len("good game"))

### code
print(len("good game"))
### choices
- 8
- 9
- 2
- 10

---

## p_split_comma
kind: mcq
title: Breaking up the guest list
tags: strings, predict, formatting
difficulty: medium
answer: 2

### prompt
What does this print?

    print("amy,ben,cam".split(","))

### code
print("amy,ben,cam".split(","))
### choices
- amy ben cam
- ['amy', 'ben', 'cam']
- ['amy,ben,cam']
- amybencam

---

## p_join_dash
kind: mcq
title: Building a phone number
tags: strings, predict, formatting
difficulty: medium
answer: 2

### prompt
What does this print?

    print("-".join(["555", "867", "5309"]))

### code
print("-".join(["555", "867", "5309"]))
### choices
- 5558675309
- 555-867-5309
- ['555', '867', '5309']
- -555-867-5309

---

## p_count_a
kind: mcq
title: How many A's in Alabama?
tags: strings, predict
difficulty: easy
answer: 2

### prompt
What does this print?

    print("alabama".count("a"))

### code
print("alabama".count("a"))
### choices
- 3
- 4
- 1
- 7

---

## p_in_word
kind: mcq
title: Hidden word inside a word
tags: strings, predict
difficulty: easy
answer: 1

### prompt
What does this print?

    print("app" in "happy")

### code
print("app" in "happy")
### choices
- True
- False
- app
- 1

---

## p_concat_5
kind: mcq
title: Two fives that don't add up
tags: strings, predict
difficulty: easy
answer: 2

### prompt
These look like numbers, but they're in quotes. What does this print?

    print("5" + "5")

### code
print("5" + "5")
### choices
- 10
- 55
- 25
- 5 5

---

## p_step_two
kind: mcq
title: Every other letter of PIZZA
tags: strings, predict, indexing
difficulty: medium
answer: 2

### prompt
What does this print?

    print("pizza"[::2])

### code
print("pizza"[::2])
### choices
- iz
- pza
- iza
- pizza

---

## p_fstring_name
kind: mcq
title: Welcome screen text
tags: strings, predict, formatting
difficulty: easy
answer: 2

### prompt
What does this print?

    name = "Zoe"
    print(f"Welcome, {name}!")

### code
name = "Zoe"
print(f"Welcome, {name}!")
### choices
- Welcome, {name}!
- Welcome, Zoe!
- Welcome, name!
- Welcome,Zoe!

---

## bug_greet_space
kind: code_fn
title: Names with no space between
tags: strings, bugs, formatting
difficulty: easy
entry: greet

### prompt
This should build a player's display name from a first and last name, with one
space between them. It runs, but the names come out mashed together. Fix it.

Examples

    greet("Sam", "Lee") → "Sam Lee"
    greet("Ann", "Kim") → "Ann Kim"

Notes

- Gluing two strings with + puts them directly next to each other with nothing
  in between.
- You have to add the space yourself.

### starter
```python
def greet(first, last):
    return first + last
```

### solution
```python
def greet(first, last):
    return first + " " + last
```

### check
greet("Sam", "Lee") == "Sam Lee"
greet("Ann", "Kim") == "Ann Kim"
greet("A", "B") == "A B"
greet("Jo", "Ng") == "Jo Ng"

---

## bug_price_label
kind: code_fn
title: The shop price tag crashes
tags: strings, bugs, formatting
difficulty: easy
entry: price_label

### prompt
This should build a shop price tag like "$5" from a whole-coin amount. The
amount arrives as an integer, and the code crashes. Fix it.

Examples

    price_label(5) → "$5"
    price_label(10) → "$10"

Notes

- You cannot add a string and an integer with +.
- str(n) turns a number into its text form so it can be glued to other text.

### starter
```python
def price_label(dollars):
    return "$" + dollars
```

### solution
```python
def price_label(dollars):
    return "$" + str(dollars)
```

### check
price_label(5) == "$5"
price_label(10) == "$10"
price_label(0) == "$0"
price_label(99) == "$99"

---

## bug_shout_upper
kind: code_fn
title: Caps lock that does nothing
tags: strings, bugs
difficulty: medium
entry: shout_it

### prompt
This should return a text message in all caps. It runs without error but returns
the message unchanged. Fix it.

Examples

    shout_it("hi") → "HI"
    shout_it("go") → "GO"

Notes

- word.upper() does not change word. It builds and returns a brand-new
  uppercase string.
- If you never use what it returns, the work is thrown away.

### starter
```python
def shout_it(word):
    word.upper()
    return word
```

### solution
```python
def shout_it(word):
    return word.upper()
```

### check
shout_it("hi") == "HI"
shout_it("go") == "GO"
shout_it("Wow") == "WOW"
shout_it("a") == "A"

---

## bug_cap_first
kind: code_fn
title: You can't overwrite one letter
tags: strings, bugs, indexing
difficulty: medium
entry: cap_first

### prompt
This should capitalize the first letter of a username. It tries to overwrite that
one character in place and crashes. Fix it.

Examples

    cap_first("cat") → "Cat"
    cap_first("dog") → "Dog"

Notes

- Strings are immutable: word[0] = "X" is not allowed and raises an error.
- Instead, build a new string from the uppercased first letter plus the rest,
  which you can get with word[1:].

### starter
```python
def cap_first(word):
    word[0] = word[0].upper()
    return word
```

### solution
```python
def cap_first(word):
    return word[0].upper() + word[1:]
```

### check
cap_first("cat") == "Cat"
cap_first("dog") == "Dog"
cap_first("a") == "A"
cap_first("python") == "Python"

---

## bug_last_char
kind: code_fn
title: One step past the end
tags: strings, bugs, indexing
difficulty: medium
entry: last_char

### prompt
This should return the last letter of a password. It uses the length as the
index and crashes. Fix it.

Examples

    last_char("cat") → "t"
    last_char("hi") → "i"

Notes

- Indexing starts at 0, so a 3-letter word has its last character at index 2,
  not 3.
- word[len(word)] is always one step too far.

### starter
```python
def last_char(word):
    return word[len(word)]
```

### solution
```python
def last_char(word):
    return word[len(word) - 1]
```

### check
last_char("cat") == "t"
last_char("hi") == "i"
last_char("a") == "a"
last_char("python") == "n"

---

## wrong_score_concat
kind: mcq
title: XP that won't glue on
tags: strings, bugs, formatting
difficulty: easy
answer: 2

### prompt
What is wrong with this code?

    xp = 10
    print("XP: " + xp)

### choices
- Nothing, it prints "XP: 10"
- You can't add a string and an integer; you need str(xp)
- xp must be written in quotes when it is created
- print can only be given one thing at a time

---

## wrong_upper_lost
kind: mcq
title: The shout that got lost
tags: strings, bugs
difficulty: medium
answer: 2

### prompt
This code prints "sam", not "SAM". Why?

    name = "sam"
    name.upper()
    print(name)

### choices
- .upper() changes name, but print quietly undoes it
- .upper() returns a new string; the result was never stored back in name
- Strings cannot be turned into capital letters
- You must write name = upper(name) with no dot

---

## wrong_index_range
kind: mcq
title: Reaching past the last letter
tags: strings, bugs, indexing
difficulty: easy
answer: 3

### prompt
A username "cat" has three letters. What happens when this runs?

    username = "cat"
    print(username[3])

### choices
- It prints "t"
- It prints an empty string
- It raises an error because the last valid index is 2, not 3
- It prints "cat"

---

## concept_first_index
kind: mcq
title: Where does counting start?
tags: strings, concept, indexing
difficulty: easy
answer: 2

### prompt
In Python, what is the index of the first character of a string?

### choices
- 1
- 0
- -1
- It depends on the string

---

## concept_slice_excludes
kind: mcq
title: Which letters does a slice grab?
tags: strings, concept, indexing
difficulty: medium
answer: 2

### prompt
The slice word[1:4] gives you the characters at which index positions?

### choices
- 1, 2, 3, and 4
- 1, 2, and 3 (it stops before 4)
- 2, 3, and 4
- Only 1 and 4

---

## concept_str_vs_int
kind: mcq
title: "5" versus 5
tags: strings, concept
difficulty: easy
answer: 2

### prompt
What is the difference between "5" and 5 in Python?

### choices
- There is no difference; Python treats them the same
- "5" is a string (text) and 5 is an integer (a number)
- "5" is larger than 5
- 5 is a string and "5" is a number

---

## concept_replace_new
kind: mcq
title: Does .replace() edit the original?
tags: strings, concept
difficulty: medium
answer: 2

### prompt
After you run word.replace("a", "o"), is the original string stored in word
changed?

### choices
- Yes, it edits word in place
- No, it returns a new string and leaves word unchanged
- Only if the letter appears more than once
- It deletes word entirely

---

## concept_immutable
kind: mcq
title: What "immutable" means
tags: strings, concept, indexing
difficulty: medium
answer: 2

### prompt
Which statement about Python strings is true?

### choices
- You can change a single character with word[0] = "X"
- Strings are immutable: you can't change a character in place, you build a new string instead
- Strings grow and shrink in place like lists
- Calling len() rewrites the string

---

## concept_len_counts
kind: mcq
title: What does len() actually count?
tags: strings, concept
difficulty: easy
answer: 2

### prompt
What does len("hi there") count?

### choices
- Only the letters, so 6
- Every character including the space, so 8
- The number of words, so 2
- The number of vowels, so 3

---

## ends
kind: code_fn
title: A two-letter monogram
tags: strings, indexing
difficulty: easy
entry: ends

### prompt
Write a function that takes a word and returns a two-character string made of its
first and last character.

Examples

    ends("cat") → "ct"
    ends("hello") → "ho"
    ends("a") → "aa"

Notes

- word[0] is the first character; word[-1] is the last.
- For a one-letter word the first and last character are the same.
- Return the string, do not print it.

### starter
```python
def ends(word):
    
```

### solution
```python
def ends(word):
    return word[0] + word[-1]
```

### check
ends("cat") == "ct"
ends("hello") == "ho"
ends("a") == "aa"
ends("python") == "pn"

---

## yell
kind: code_fn
title: Shout it with a bang
tags: strings, formatting
difficulty: easy
entry: yell

### prompt
Write a function that takes a word and returns it in all capital letters with a
single "!" added to the end.

Examples

    yell("go") → "GO!"
    yell("wow") → "WOW!"

Notes

- word.upper() returns an uppercase copy of the word.
- You can glue the "!" on with +.
- Return the result.

### starter
```python
def yell(word):
    
```

### solution
```python
def yell(word):
    return word.upper() + "!"
```

### check
yell("go") == "GO!"
yell("wow") == "WOW!"
yell("Stop") == "STOP!"
yell("a") == "A!"

---

## chant
kind: code_fn
title: Chant it n times
tags: strings, formatting
difficulty: easy
entry: chant

### prompt
Write a function that takes a word and a whole number n, and returns the word
repeated n times with nothing in between.

Examples

    chant("go", 3) → "gogogo"
    chant("ab", 2) → "abab"
    chant("hi", 0) → ""

Notes

- Multiplying a string by a number repeats it.
- Repeating 0 times gives an empty string.
- Return the result.

### starter
```python
def chant(word, n):
    
```

### solution
```python
def chant(word, n):
    return word * n
```

### check
chant("go", 3) == "gogogo"
chant("ab", 2) == "abab"
chant("x", 1) == "x"
chant("hi", 0) == ""

---

## tag_line
kind: code_fn
title: Stitch a label to a score
tags: strings, formatting
difficulty: easy
entry: tag_line

### prompt
Write a function that takes a label (a string) and a score (a whole number) and
returns a string in the form "label: score".

Examples

    tag_line("score", 10) → "score: 10"
    tag_line("age", 5) → "age: 5"

Notes

- An f-string lets you drop a number straight into text: f"{label}: {score}".
- You do not have to convert the number by hand inside an f-string.
- Return the result.

### starter
```python
def tag_line(label, score):
    
```

### solution
```python
def tag_line(label, score):
    return f"{label}: {score}"
```

### check
tag_line("score", 10) == "score: 10"
tag_line("age", 5) == "age: 5"
tag_line("x", 0) == "x: 0"
tag_line("hp", 100) == "hp: 100"

---

## slugify
kind: code_fn
title: Turn a title into a URL slug
tags: strings, formatting
difficulty: medium
entry: slugify

### prompt
Write a function that turns a blog-post title into a "slug" for its web address:
all lowercase, with every space replaced by a dash "-".

Examples

    slugify("Hello World") → "hello-world"
    slugify("Two Words") → "two-words"

Notes

- text.lower() gives a lowercase copy.
- text.replace(" ", "-") swaps every space for a dash.
- You can do one after the other on the same line.

### starter
```python
def slugify(text):
    
```

### solution
```python
def slugify(text):
    return text.lower().replace(" ", "-")
```

### check
slugify("Hello World") == "hello-world"
slugify("Two Words") == "two-words"
slugify("Python") == "python"
slugify("A B C") == "a-b-c"

---

## letters_in_banana
kind: code_var
title: Let Python count the letters
tags: strings
difficulty: easy
entry: n

### prompt
Store the number of letters in the word "banana" in a variable called n.

Notes

- len("banana") counts the characters for you.
- Save that number into n; you do not need to type the number yourself.

### starter
```python
n = 
```

### solution
```python
n = len("banana")
```

### check
n == 6
