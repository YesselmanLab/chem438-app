# Week 2 — strings & functions

---

## shout
kind: code_fn
title: shout(word)
tags: strings, functions, week2
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
tags: strings, methods, week2
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

### prompt
With strings, what does  +  do, and what does  *  do? Give a short example of each.
