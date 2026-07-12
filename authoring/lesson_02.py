"""lesson_02.py — Lesson 2: strings & simple functions. (Same format as lesson_01.)"""

def _shout(word):
    return word.upper() + "!"

def _first_letter(word):
    return word[0]


LESSON = {
    "id": "lesson_02",
    "title": "Lesson 2 — strings & functions",
    "intro": "More practice with text and writing your own functions.",
    "questions": [
        {
            "id": "q1", "kind": "code_var",
            "prompt": "Store the word \"python\" in ALL CAPS in a variable `caps`.",
            "starter": "caps = ",
            "entry": "caps",
            "reference": 'caps = "python".upper()',
        },
        {
            "id": "q2", "kind": "code_var",
            "prompt": "Store the number of letters in \"chemistry\" in a variable `n` "
                      "(use the len() function).",
            "starter": "n = ",
            "entry": "n",
            "reference": 'n = len("chemistry")',
        },
        {
            "id": "q3", "kind": "code_fn",
            "prompt": "Write a function `shout(word)` that returns the word in "
                      "uppercase with an exclamation mark, e.g. shout(\"hi\") -> \"HI!\".",
            "starter": "def shout(word):\n    ",
            "entry": "shout",
            "inputs": [["hi"], ["mole"], ["acid"], ["yes"], ["bond"]],
            "reference": _shout,
        },
        {
            "id": "q4", "kind": "code_fn",
            "prompt": "Write a function `first_letter(word)` that returns the first "
                      "letter of a word. (Hint: word[0].)",
            "starter": "def first_letter(word):\n    ",
            "entry": "first_letter",
            "inputs": [["cat"], ["atom"], ["python"], ["salt"]],
            "reference": _first_letter,
        },
        {
            "id": "q5", "kind": "mcq",
            "prompt": "What does this print?\n\n    print(len(\"cat\"))",
            "choices": ["2", "3", "4", "an error"],
            "answer": 1,
        },
        {
            "id": "q6", "kind": "mcq",
            "prompt": "What does this print?\n\n    print(\"ab\" + \"cd\")",
            "choices": ["abcd", "ab cd", "cdab", "an error"],
            "answer": 0,
        },
        {
            "id": "q7", "kind": "written",
            "prompt": "With strings, what does  +  do, and what does  *  do? "
                      "Give a short example of each.",
        },
    ],
}
