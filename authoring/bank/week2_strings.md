# Week 2 — strings & functions

---

## hello_name
kind: code_fn
title: Name greeting
tags: formatting, language_fundamentals, strings, week2
see: 02_strings#joining-strings-with
difficulty: easy
entry: hello_name

### prompt
Create a function that takes a name and returns a greeting in the form of a string.

Examples

    hello_name("Gerald") → "Hello Gerald!"
    hello_name("Tiffany") → "Hello Tiffany!"
    hello_name("Ed") → "Hello Ed!"

Notes

- The input is always a name (as a string).
- Don't forget the exclamation mark!

### walkthrough
You're building one string out of three pieces: the word "Hello ", the name you
were handed, and "!". The `+` operator glues strings together:

    def hello_name(name):
        return "Hello " + name + "!"

Watch the spaces — they only exist if you type them. "Hello" + "Ed" gives
"HelloEd", so the space has to live inside the quotes: "Hello " with a trailing
space. This is the single most common way this problem goes wrong.

### starter
```python
def hello_name(name):
    
```

### solution
```python
def hello_name(name):
    return "Hello " + name + "!"
```

### check
hello_name("Gerald") == "Hello Gerald!"
hello_name("Tiffany") == "Hello Tiffany!"
hello_name("Ed") == "Hello Ed!"
hello_name("Ana") == "Hello Ana!"

---

## give_me_something
kind: code_fn
title: Return something to me!
tags: language_fundamentals, strings, week2
see: 02_strings#joining-strings-with
difficulty: easy
entry: give_me_something

### prompt
Write a function that returns the string "something" joined with a space " " and
the given argument `a`.

Examples

    give_me_something("is better than nothing") → "something is better than nothing"
    give_me_something("Bob Jane") → "something Bob Jane"
    give_me_something("something") → "something something"

Notes

- Assume an input is given.

### starter
```python
def give_me_something(a):
    
```

### solution
```python
def give_me_something(a):
    return "something " + a
```

### check
give_me_something("is better than nothing") == "something is better than nothing"
give_me_something("Bob Jane") == "something Bob Jane"
give_me_something("something") == "something something"
give_me_something("else") == "something else"

---

## name_string
kind: code_fn
title: Basic variable assignment (fix the code)
tags: bugs, language_fundamentals, strings, week2
see: 09_errors#forgetting-the-quotes-around-text
difficulty: easy
entry: name_string

### prompt
A student learning Python was trying to write a function. Their code should join
a passed string `name` with the string "Chem438" and store it in a variable
called `result`. They need your help to fix this code.

Examples

    name_string("Mubashir") → "MubashirChem438"
    name_string("Matt") → "MattChem438"
    name_string("python") → "pythonChem438"

Notes

- Don't forget to return the result.

### walkthrough
Run the broken code first and read the error — that's a skill worth building, not
a step to skip. Python says `NameError: name 'Chem438' is not defined`.

That message is the whole clue. Without quotes, Python reads `Chem438` as the
name of a variable, goes looking for one, and finds nothing. Text needs quotes:

    def name_string(name):
        result = name + "Chem438"
        return result

The bug is one pair of quotes. Getting comfortable reading an error and letting
it point you at the line will save you more time this semester than anything else.

### starter
```python
def name_string(name):
    result = name + Chem438
    return result
```

### solution
```python
def name_string(name):
    result = name + "Chem438"
    return result
```

### check
name_string("Mubashir") == "MubashirChem438"
name_string("Matt") == "MattChem438"
name_string("python") == "pythonChem438"
name_string("") == "Chem438"

---

## to_str
kind: code_fn
title: Return an integer as a string
tags: language_fundamentals, strings, week2
see: 02_strings#converting-between-strings-and-numbers
difficulty: easy
entry: to_str

### prompt
Create a function that takes an integer and returns it as a string.

Examples

    to_str(77) → "77"
    to_str(532) → "532"
    to_str(0) → "0"

Notes

- This is the mirror image of the `string_int` challenge, which goes the other
  way. Python keeps text and numbers strictly apart, and these two built-ins are
  how you cross between them.
- Don't forget to `return` the result.

### starter
```python
def to_str(num):
    
```

### solution
```python
def to_str(num):
    return str(num)
```

### check
to_str(77) == "77"
to_str(532) == "532"
to_str(0) == "0"
to_str(12) == "12"

---

## bool_to_string
kind: code_fn
title: Boolean to string conversion
tags: conditions, logic, strings, week2
see: 02_strings#converting-between-strings-and-numbers
difficulty: easy
entry: bool_to_string

### prompt
Create a function that takes a boolean variable `flag` and returns it as a string.

Examples

    bool_to_string(True) → "True"
    bool_to_string(False) → "False"

Notes

- The same `str()` that turns a number into text turns a boolean into text too.

### starter
```python
def bool_to_string(flag):
    
```

### solution
```python
def bool_to_string(flag):
    return str(flag)
```

### check
bool_to_string(True) == "True"
bool_to_string(False) == "False"

---

## shout
kind: code_fn
title: shout(word)
tags: strings, functions, week2
see: 02_strings#changing-case
entry: shout

### prompt
Write a function `shout(word)` that returns the word in uppercase with an exclamation mark, e.g. shout("hi") -> "HI!".

### starter
```python
def shout(word):
    
```

### solution
```python
def shout(word):
    return word.upper() + "!"
```

### check
shout("hi") == "HI!"
shout("mole") == "MOLE!"
shout("acid") == "ACID!"
shout("yes") == "YES!"
shout("bond") == "BOND!"

---

## first_letter
kind: code_fn
title: first_letter(word)
tags: strings, functions, indexing, week2
see: 02_strings#indexing-grabbing-one-character
entry: first_letter

### prompt
Write a function `first_letter(word)` that returns the first letter of a word. (Hint: word[0].)

### starter
```python
def first_letter(word):
    
```

### solution
```python
def first_letter(word):
    return word[0]
```

### check
first_letter("cat") == "c"
first_letter("atom") == "a"
first_letter("python") == "p"
first_letter("salt") == "s"

---

## str_upper
kind: code_var
title: Uppercase a string
tags: strings, week2
see: 02_strings#changing-case
entry: caps

### prompt
Store the word "python" in ALL CAPS in a variable `caps`.

### starter
```python
caps = 
```

### solution
```python
caps = "python".upper()
```

### check
caps == "PYTHON"

---

## str_len
kind: code_var
title: Length of a string
tags: strings, week2
see: 02_strings#length-len
entry: n

### prompt
Store the number of letters in "chemistry" in a variable `n` (use the len() function).

### starter
```python
n = 
```

### solution
```python
n = len("chemistry")
```

### check
n == 9

---

## mcq_len_cat
kind: mcq
title: Predict — len('cat')
tags: concept, predict, strings, week2
see: 02_strings#length-len
answer: 2

### prompt
What does this print?

    print(len("cat"))

### choices
- 2
- 3
- 4
- an error

---

## mcq_concat_abcd
kind: mcq
title: Predict — 'ab' + 'cd'
tags: concept, predict, strings, week2
see: 02_strings#joining-strings-with
answer: 1

### prompt
What does this print?

    print("ab" + "cd")

### choices
- abcd
- ab cd
- cdab
- an error

---

## written_plus_vs_star
kind: written
title: Explain — + vs * on strings
tags: concept, written, strings, week2
see: 02_strings#joining-strings-with

### prompt
With strings, what does  +  do, and what does  *  do? Give a short example of each.
