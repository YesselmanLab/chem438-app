"""
bank.py — the PROBLEM BANK. Write a problem once here; reuse it in any assignment.

Each entry is one problem keyed by a short id you choose. An assignment (see
assignments.py) is just a list of these ids — so building an assignment is
"pick the problems you want." Add problems here freely; they show up in the
visual builder (builder.html) automatically after `python build.py --bank`.

Problem fields:
  kind        code_var | code_fn | mcq | written
  title       short label (shown in the builder + gradebook)
  prompt      what the student sees
  tags        list of strings for filtering in the builder (topic/week/skill)
  difficulty  "easy" | "medium" | "hard"  (just a label for you)
  -- code_var: starter, entry (variable name), reference (code string)
  -- code_fn : starter, entry (function name), inputs (list of arg-lists),
               reference (a Python function = the correct answer)
  -- mcq     : choices (list), answer (index)
  -- written : (nothing extra; read by a human)
You never type expected answers for code — build.py runs your reference.
"""

# ---- reference solutions (never shipped to students) ----
def _double(x): return x * 2
def _area(length, width): return length * width
def _is_even(n): return n % 2 == 0
def _shout(word): return word.upper() + "!"
def _first_letter(word): return word[0]


BANK = {
    # ---------- arithmetic & variables ----------
    "sum_total": dict(
        kind="code_var", title="Sum two variables", tags=["arithmetic", "variables", "week1"], difficulty="easy",
        prompt="Create a variable `a` equal to 7 and `b` equal to 5, then store their sum in a variable `total`.",
        starter="a = \nb = \ntotal = ", entry="total", reference="a = 7\nb = 5\ntotal = a + b"),
    "remainder_mod": dict(
        kind="code_var", title="Remainder with %", tags=["arithmetic", "operators", "week1"], difficulty="easy",
        prompt="Store the remainder of 17 divided by 5 in a variable `rem` (use the % operator).",
        starter="rem = ", entry="rem", reference="rem = 17 % 5"),

    # ---------- functions (code_fn) ----------
    "double_fix": dict(
        kind="code_fn", title="Fix the double function", tags=["functions", "debug", "week1"], difficulty="easy",
        prompt="Fix the bug: `double` should return its input doubled.",
        starter="def double(x):\n    return x + 2      # <-- wrong, fix it",
        entry="double", inputs=[[4], [10], [0], [7], [25]], reference=_double),
    "area_rect": dict(
        kind="code_fn", title="Rectangle area", tags=["functions", "arithmetic", "week1"], difficulty="easy",
        prompt="Write a function `area(length, width)` that returns the area of a rectangle.",
        starter="def area(length, width):\n    ",
        entry="area", inputs=[[3, 4], [5, 5], [2, 10], [7, 3], [1, 9]], reference=_area),
    "is_even": dict(
        kind="code_fn", title="is_even", tags=["functions", "logic", "week1"], difficulty="easy",
        prompt="Write a function `is_even(n)` that returns True if n is even, False otherwise.",
        starter="def is_even(n):\n    ",
        entry="is_even", inputs=[[4], [7], [0], [3], [10], [1]], reference=_is_even),
    "shout": dict(
        kind="code_fn", title="shout(word)", tags=["strings", "functions", "week2"], difficulty="easy",
        prompt="Write a function `shout(word)` that returns the word in uppercase with an "
               "exclamation mark, e.g. shout(\"hi\") -> \"HI!\".",
        starter="def shout(word):\n    ",
        entry="shout", inputs=[["hi"], ["mole"], ["acid"], ["yes"], ["bond"]], reference=_shout),
    "first_letter": dict(
        kind="code_fn", title="first_letter(word)", tags=["strings", "functions", "indexing", "week2"], difficulty="easy",
        prompt="Write a function `first_letter(word)` that returns the first letter of a word. (Hint: word[0].)",
        starter="def first_letter(word):\n    ",
        entry="first_letter", inputs=[["cat"], ["atom"], ["python"], ["salt"]], reference=_first_letter),

    # ---------- strings (code_var) ----------
    "str_upper": dict(
        kind="code_var", title="Uppercase a string", tags=["strings", "methods", "week2"], difficulty="easy",
        prompt="Store the word \"python\" in ALL CAPS in a variable `caps`.",
        starter="caps = ", entry="caps", reference='caps = "python".upper()'),
    "str_len": dict(
        kind="code_var", title="Length of a string", tags=["strings", "week2"], difficulty="easy",
        prompt="Store the number of letters in \"chemistry\" in a variable `n` (use the len() function).",
        starter="n = ", entry="n", reference='n = len("chemistry")'),

    # ---------- concept: multiple choice ----------
    "mcq_str_plus_int": dict(
        kind="mcq", title="What's wrong: text + number", tags=["concept", "debug", "types", "week1"], difficulty="easy",
        prompt="What is wrong with this code?\n\n    print(\"Total: \" + 5)",
        choices=["Nothing — it prints  Total: 5",
                 "You can't join text and a number with + — the 5 must be str(5)",
                 "print is spelled wrong", "It needs another set of parentheses"], answer=1),
    "mcq_floor_div": dict(
        kind="mcq", title="Predict: 7 // 2", tags=["concept", "predict", "operators", "week1"], difficulty="easy",
        prompt="What does this print?\n\n    print(7 // 2)",
        choices=["3.5", "3", "3.0", "1"], answer=1),
    "mcq_len_cat": dict(
        kind="mcq", title="Predict: len('cat')", tags=["concept", "predict", "strings", "week2"], difficulty="easy",
        prompt="What does this print?\n\n    print(len(\"cat\"))",
        choices=["2", "3", "4", "an error"], answer=1),
    "mcq_concat_abcd": dict(
        kind="mcq", title="Predict: 'ab' + 'cd'", tags=["concept", "predict", "strings", "week2"], difficulty="easy",
        prompt="What does this print?\n\n    print(\"ab\" + \"cd\")",
        choices=["abcd", "ab cd", "cdab", "an error"], answer=0),

    # ---------- concept: written ----------
    "written_plus_vs_star_hello": dict(
        kind="written", title="Explain: hello + 2 vs hello * 2", tags=["concept", "written", "types", "week1"], difficulty="easy",
        prompt="Why does  \"hello\" + 2  cause an error, but  \"hello\" * 2  works fine? (One or two sentences.)"),
    "written_plus_vs_star": dict(
        kind="written", title="Explain: + vs * on strings", tags=["concept", "written", "strings", "week2"], difficulty="easy",
        prompt="With strings, what does  +  do, and what does  *  do? Give a short example of each."),
}
