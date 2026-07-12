"""
lesson_01.py -- the ONE file you edit to author Lesson 1.

Each question is a dict. Question kinds:
  code_var : student defines a VARIABLE; we check its value.
             fields: prompt, starter, entry (var name), reference (code string).
  code_fn  : student writes a FUNCTION; we run it on `inputs` and check outputs.
             fields: prompt, starter, entry (fn name), inputs (list of arg-lists),
                     reference (a Python function that IS the correct answer).
             -> use several VARIED inputs; that's what stops hard-coding.
  mcq      : multiple choice. fields: prompt, choices (list), answer (index).
  written  : short answer read by you. fields: prompt.

You never type expected answers for code questions -- build.py computes them by
running your `reference` solution. Write a correct reference, run build.py, done.
"""

# --- reference solutions (the correct answers; never shipped to students) ---
def _double(x):
    return x * 2

def _area(length, width):
    return length * width

def _is_even(n):
    return n % 2 == 0


LESSON = {
    "id": "lesson_01",
    "title": "Lesson 1 — the basics",
    "intro": "Type your answer in each box. Run coding cells to test them, then "
             "submit the whole lesson for instant feedback.",
    "questions": [
        {
            "id": "q1", "kind": "code_var",
            "prompt": "Create a variable `a` equal to 7 and `b` equal to 5, then "
                      "store their sum in a variable `total`.",
            "starter": "a = \nb = \ntotal = ",
            "entry": "total",
            "reference": "a = 7\nb = 5\ntotal = a + b",
        },
        {
            "id": "q2", "kind": "code_var",
            "prompt": "Store the remainder of 17 divided by 5 in a variable `rem` "
                      "(use the % operator).",
            "starter": "rem = ",
            "entry": "rem",
            "reference": "rem = 17 % 5",
        },
        {
            "id": "q3", "kind": "code_fn",
            "prompt": "Fix the bug: `double` should return its input doubled.",
            "starter": "def double(x):\n    return x + 2      # <-- wrong, fix it",
            "entry": "double",
            "inputs": [[4], [10], [0], [7], [25]],   # varied -> hard-coding fails
            "reference": _double,
        },
        {
            "id": "q4", "kind": "code_fn",
            "prompt": "Write a function `area(length, width)` that returns the area "
                      "of a rectangle.",
            "starter": "def area(length, width):\n    ",
            "entry": "area",
            "inputs": [[3, 4], [5, 5], [2, 10], [7, 3], [1, 9]],
            "reference": _area,
        },
        {
            "id": "q5", "kind": "code_fn",
            "prompt": "Write a function `is_even(n)` that returns True if n is even, "
                      "False otherwise.",
            "starter": "def is_even(n):\n    ",
            "entry": "is_even",
            "inputs": [[4], [7], [0], [3], [10], [1]],
            "reference": _is_even,
        },
        {
            "id": "q6", "kind": "mcq",
            "prompt": "What is wrong with this code?\n\n    print(\"Total: \" + 5)",
            "choices": [
                "Nothing — it prints  Total: 5",
                "You can't join text and a number with + — the 5 must be str(5)",
                "print is spelled wrong",
                "It needs another set of parentheses",
            ],
            "answer": 1,
        },
        {
            "id": "q7", "kind": "mcq",
            "prompt": "What does this print?\n\n    print(7 // 2)",
            "choices": ["3.5", "3", "3.0", "1"],
            "answer": 1,
        },
        {
            "id": "q8", "kind": "written",
            "prompt": "Why does  \"hello\" + 2  cause an error, but  \"hello\" * 2  "
                      "works fine? (One or two sentences.)",
        },
    ],
}
