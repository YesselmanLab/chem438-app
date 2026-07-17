# Functions themselves
Parameters, arguments, defaults, return vs print, and calling one function from another.

---

## coffee_order_ticket
kind: code_fn
title: Write the coffee ticket
tags: functions, strings, language_fundamentals
see: 03_functions#multiple-parameters-and-argument-order
difficulty: starter
entry: order_ticket

### prompt
Write a function that takes a size and a drink and returns them joined by a single space.

Examples

    order_ticket("large", "latte") → "large latte"
    order_ticket("small", "mocha") → "small mocha"
    order_ticket("medium", "tea") → "medium tea"

Notes

- The two words are separated by exactly one space, and there is no space at the start or the end.
- The order of the parameters matters: the size comes first, then the drink.
- Don't forget to return the result.

### starter
```python
def order_ticket(size, drink):
    pass
```

### solution
```python
def order_ticket(size, drink):
    return size + " " + drink
```

### check
order_ticket("large", "latte") == "large latte"
order_ticket("small", "mocha") == "small mocha"
order_ticket("medium", "tea") == "medium tea"
order_ticket("extra large", "cold brew") == "extra large cold brew"

---

## seats_left_print_bug
kind: code_fn
title: The seat counter returns nothing
tags: functions, bugs, language_fundamentals
see: 03_functions#return-vs-print-the-most-important-distinction-in-this-course
difficulty: starter
entry: seats_left

### prompt
This function is supposed to hand back how many seats are still free, but the caller keeps getting None. Fix it.

    left = seats_left(100, 42)
    print(left)          # prints None, not 58

Examples

    seats_left(100, 42) → 58
    seats_left(50, 50) → 0
    seats_left(12, 3) → 9

Notes

- print shows a value on the screen; it does not hand the value back to whoever called the function.
- The arithmetic is already correct — only one word needs to change.

### starter
```python
def seats_left(capacity, taken):
    print(capacity - taken)
```

### solution
```python
def seats_left(capacity, taken):
    return capacity - taken
```

### check
seats_left(100, 42) == 58
seats_left(50, 50) == 0
seats_left(12, 3) == 9
seats_left(0, 0) == 0

### walkthrough
Run the broken version in your head. Python computes 100 - 42, gets 58, and passes it to
print, which draws "58" on the screen and then quietly evaluates to None. The function body
ends. A function that never runs a return statement hands back None — always.

So the 58 you see on the screen is real, but it is gone. It was displayed, not delivered.
That is why this line stores None:

    left = seats_left(100, 42)

This is the single most common beginner mix-up, and it hides because the number LOOKS right
when you test the function by itself. The moment you try to use the answer — store it, add
to it, compare it — you get None and a confusing TypeError.

The fix is one word:

    def seats_left(capacity, taken):
        return capacity - taken

Now nothing is printed, and that is correct. The caller decides whether to print. Rule of
thumb: a function that computes a value should return it and print nothing.

---

## mask_password
kind: code_fn
title: Mask the password
tags: functions, strings, language_fundamentals
see: 03_functions#default-arguments
difficulty: easy
entry: mask

### prompt
Write a function that returns a mask for a password: a string the same length as the password, made only of the masking character. The masking character should be "*" unless the caller supplies a different one.

Examples

    mask("hunter2") → "*******"
    mask("hunter2", "#") → "#######"
    mask("abc", ".") → "..."

Notes

- The mask must be exactly as long as the password.
- Give the second parameter a default value so it is optional at the call site.
- Multiplying a string by a number repeats it: "ab" * 3 is "ababab".

### starter
```python
def mask(password, char="*"):
    pass
```

### solution
```python
def mask(password, char="*"):
    return char * len(password)
```

### check
mask("hunter2") == "*******"
mask("hunter2", "#") == "#######"
mask("abc", ".") == "..."
mask("") == ""

### walkthrough
Start with the length. len("hunter2") is 7, so you need 7 copies of the masking character.
String repetition gives you that in one step: "*" * 7 is "*******". Combine the two:

    return char * len(password)

Now the interesting part — the default. Writing char="*" in the header means "if the caller
does not pass a second argument, use "*"". So mask("abc") and mask("abc", "*") do exactly
the same thing, and mask("abc", ".") overrides the default with ".".

The mistake waiting for you is putting the default first, like def mask(char="*", password).
Python rejects that outright: once a parameter has a default, every parameter after it must
have one too, otherwise Python could not tell which argument you meant. Required parameters
first, optional ones last.

One more trap: do not reach for a loop that appends a "*" per character. It works, but the
whole point of len plus repetition is that you already have the tools to say it in one line.
And check the empty password — len("") is 0, and char * 0 is "", which is exactly right.

---

## cut_the_deck
kind: code_fn
title: Cut the deck
tags: functions, arrays, indexing
see: 06_lists#slicing
difficulty: easy
entry: cut

### prompt
Cutting a deck means splitting it into two piles. Write a function that takes a list of cards and a number n, and returns the two piles as a tuple: first the pile holding the first n cards, then the pile holding everything after them.

Examples

    cut([1, 2, 3, 4, 5], 2) → ([1, 2], [3, 4, 5])
    cut([1, 2, 3, 4, 5], 0) → ([], [1, 2, 3, 4, 5])
    cut(["a", "b", "c"], 1) → (["a"], ["b", "c"])

Notes

- A function can return more than one value at once — separate them with a comma, which builds a tuple. Returning a list of two lists is not the same thing.
- Slicing a list with a colon gives you part of it; you need the part before position n and the part from n onward.
- The two piles together must contain every original card, in order.

### starter
```python
def cut(cards, n):
    pass
```

### solution
```python
def cut(cards, n):
    return cards[:n], cards[n:]
```

### check
cut([1, 2, 3, 4, 5], 2) == ([1, 2], [3, 4, 5])
cut([1, 2, 3, 4, 5], 0) == ([], [1, 2, 3, 4, 5])
cut(["a", "b", "c"], 1) == (["a"], ["b", "c"])
cut([7], 1) == ([7], [])

### walkthrough
Take cut([1, 2, 3, 4, 5], 2). You want ([1, 2], [3, 4, 5]). Think of n as a cut line that sits
BETWEEN two cards, not on top of one. With n = 2 the line sits after 1 and 2, so everything to
its left is the first pile and everything to its right is the second.

That is exactly what the two slices say. cards[:2] means "from the start up to but not
including position 2", giving [1, 2]. cards[2:] means "from position 2 to the end", giving
[3, 4, 5]. The "up to but not including" is the whole reason they tile perfectly: the card at
position n is the LAST card excluded by the first slice and the FIRST card included by the
second. No gap, no overlap, no card counted twice — and that is true for any n. So:

    return cards[:n], cards[n:]

Check the ends, because that is where slicing surprises people. With n = 0 the first slice is
empty and the second is the whole deck — nothing was cut off. With n equal to the length, the
second slice is empty. Neither raises an error; an out-of-range slice quietly gives you what
exists rather than crashing the way cards[10] would.

The mistake to name: writing return [cards[:n], cards[n:]]. Those square brackets make ONE
list containing two lists, which is a different value from the two piles returned side by
side. The comma alone is what hands back two things — no brackets needed.

## mcq_function_with_no_return
kind: mcq
title: What does the cheer print?
tags: functions, predict, concept
see: 03_functions#a-function-that-returns-nothing-gives-you-none
difficulty: easy
answer: 3

### prompt
Read this program carefully and predict everything it prints.

    def cheer(name):
        print(name + " wins!")

    result = cheer("Ana")
    print(result)

What appears on the screen?

Notes

- cheer has no return statement.
- Count both print calls — the one inside the function and the one at the bottom.

### choices
- Ana wins!
- Ana wins! then Ana wins!
- Ana wins! then None
- None then Ana wins!
- Nothing — the program raises an error

---

## can_afford_cart
kind: code_fn
title: Can you afford the cart?
tags: functions, logic, conditions
see: 03_functions#calling-one-function-from-another
difficulty: medium
entry: can_afford

### prompt
You are given line_total(price, qty), which returns the cost of one line of a shopping cart: the price times the quantity, plus a flat $1 handling fee charged once per line. Write can_afford(p1, q1, p2, q2, wallet) that returns True when the two line totals together cost no more than what is in the wallet, and False otherwise.

Examples

    can_afford(3, 2, 5, 1, 20) → True
    can_afford(3, 2, 5, 1, 13) → True
    can_afford(3, 2, 5, 1, 12) → False

Notes

- Call line_total instead of working the cost out yourself — it already knows about the handling fee, and the fee is charged on each of the two lines.
- "No more than" includes spending exactly what you have.
- A comparison already produces True or False, so you do not need an if statement.

### starter
```python
def line_total(price, qty):
    return price * qty + 1

def can_afford(p1, q1, p2, q2, wallet):
    pass
```

### solution
```python
def line_total(price, qty):
    return price * qty + 1

def can_afford(p1, q1, p2, q2, wallet):
    return line_total(p1, q1) + line_total(p2, q2) <= wallet
```

### check
can_afford(3, 2, 5, 1, 20) is True
can_afford(3, 2, 5, 1, 13) is True
can_afford(3, 2, 5, 1, 12) is False
can_afford(0, 0, 0, 0, 2) is True
can_afford(0, 0, 0, 0, 1) is False
can_afford(100, 1, 1, 1, 50) is False

### walkthrough
The cart costs line_total(p1, q1) + line_total(p2, q2). The question "can I afford it?" is
just that total compared against the wallet:

    return line_total(p1, q1) + line_total(p2, q2) <= wallet

Two things worth naming. First, the comparison <= already evaluates to True or False, so
writing

    if total <= wallet:
        return True
    else:
        return False

is not wrong, only long-winded. Return the comparison itself.

Second, the temptation is to type p1 * q1 + p2 * q2 and skip line_total entirely. Look at what
that costs you. line_total(3, 2) is not 6, it is 7 — six dollars of goods plus the $1 handling
fee. Two lines means the fee is charged twice, so can_afford(3, 2, 5, 1, 12) is really 7 + 6 =
13 against a wallet of 12, which is False. A student who multiplies by hand gets 11 and answers
True. Same shape of code, wrong answer.

That is the real lesson: the helper knows a rule you do not have to re-derive, and re-deriving
it is how you get it wrong. Call the helper and the fee comes along for free — including the
fact that it lands once per line, not once per cart.

Watch the boundary too: with a total of 13 and a wallet of 13 the answer is True, because
"no more than" means <=, not <. Off-by-one at the boundary is the classic way to fail this.

---

## topping_never_added
kind: code_fn
title: The topping never sticks
tags: functions, bugs, strings
see: 03_functions#local-variables-why-names-don-t-leak-out
difficulty: hard
entry: build

### prompt
build is supposed to add a topping to an order and hand back the finished order, but the topping never sticks — build("pizza", "cheese") gives back "pizza". Fix both functions.

    def add_topping(order, topping):
        order = order + " with " + topping

    def build(base, topping):
        o = base
        add_topping(o, topping)
        return o

Examples

    build("pizza", "cheese") → "pizza with cheese"
    build("toast", "jam") → "toast with jam"
    build("salad", "nuts") → "salad with nuts"

Notes

- Reassigning a parameter inside a function does not change the caller's variable.
- add_topping must hand the new string back, and build must capture what it hands back.

### starter
```python
def add_topping(order, topping):
    order = order + " with " + topping

def build(base, topping):
    o = base
    add_topping(o, topping)
    return o
```

### solution
```python
def add_topping(order, topping):
    return order + " with " + topping

def build(base, topping):
    o = base
    o = add_topping(o, topping)
    return o
```

### check
build("pizza", "cheese") == "pizza with cheese"
build("toast", "jam") == "toast with jam"
build("salad", "nuts") == "salad with nuts"
build("rice", "") == "rice with "

### walkthrough
There are two separate bugs here, and fixing only one of them still fails.

Bug one is inside add_topping. The name order is a local parameter — a fresh label that
happens to point at the same string the caller passed in. The line

    order = order + " with " + topping

builds a brand-new string and re-points the LOCAL label at it. The caller's variable o still
points at the old string. Nothing outside the function changed, and add_topping returns None
because it has no return. The fix: hand the new string back.

    return order + " with " + topping

Bug two is inside build. Even with add_topping fixed, this line throws the answer away:

    add_topping(o, topping)

It computes "pizza with cheese" and drops it on the floor, then build returns the untouched
o. Calling a function does not modify your variables; you have to catch the result.

    o = add_topping(o, topping)

The mental model to keep: assignment to a parameter re-labels, it does not reach back into
the caller. So the only way information travels back out of a function is through return —
and the only way it lands anywhere is if the caller stores it.

---

## word_value_loop
kind: code_fn
title: Score the word
tags: functions, loops, strings
see: 07_loops#the-accumulator-inside-a-function
difficulty: medium
entry: word_value

### prompt
You are given letter_value(ch), which returns 1 for a vowel and 2 for any other letter. Write word_value(word) that returns the total value of every letter in the word.

Examples

    word_value("cab") → 5
    word_value("aei") → 3
    word_value("xyz") → 6

Notes

- Start a running total at 0, add each letter's value to it inside the loop, and return the total only after the loop has finished.
- Use letter_value instead of deciding what a vowel is yourself.
- An empty word scores 0.

### starter
```python
def letter_value(ch):
    if ch in "aeiou":
        return 1
    return 2

def word_value(word):
    pass
```

### solution
```python
def letter_value(ch):
    if ch in "aeiou":
        return 1
    return 2

def word_value(word):
    total = 0
    for ch in word:
        total += letter_value(ch)
    return total
```

### check
word_value("cab") == 5
word_value("aei") == 3
word_value("xyz") == 6
word_value("") == 0
word_value("a") == 1

### walkthrough
Trace "cab" by hand before you write anything. Start total at 0. The letter "c" is not a
vowel, so letter_value("c") is 2 and total becomes 2. Then "a" is a vowel, worth 1, so total
becomes 3. Then "b" is worth 2, so total becomes 5. Return 5. That trace IS the algorithm:

    total = 0
    for ch in word:
        total += letter_value(ch)
    return total

Now the mistake almost everyone makes here, and it is about indentation. If you put the
return inside the loop:

    for ch in word:
        total += letter_value(ch)
        return total

then the very first pass hits return and the function quits after ONE letter — word_value("cab")
gives 2. The return belongs at the same indentation as the for, so it runs only once the loop
has finished.

The other half of the pattern is where total lives. It must be created BEFORE the loop. Put
total = 0 inside the loop and you reset it on every letter, and you end up with the value of
the last letter instead of the sum.

Finally, notice why "" scoring 0 falls out for free: the loop body simply never runs, and you
return the 0 you started with. When the accumulator is set up correctly, the empty case
handles itself.
