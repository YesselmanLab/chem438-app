"""
assignments.py — your saved assignments. Each one is just a SELECTION of problem
ids from bank.py, in the order students see them.

To make a new assignment: add an entry here (or use the visual builder,
builder.html, which writes the line for you to paste), then run:
    python build.py <assignment_id> --push "<grader-url>" --token "<token>"

Reuse is free: list the same problem id in as many assignments as you like.

Two fields control the course schedule:

    unit  — the material this assignment covers (see UNITS in build.py)
    open  — whether students can see it yet

Opening an assignment also unlocks every PRACTICE CHALLENGE covering its unit and
every earlier unit. So releasing Homework 2 (unit 2, strings) gives students all
the unit-1 and unit-2 challenges to practise on, and keeps units 3+ locked.

To release the next assignment: flip `open` to True here, then
    python build.py --all && git add -A && git commit -m "open hw2" && git push
"""

ASSIGNMENTS = {
    # A full demo homework, composed by picking problems out of the bank.
    # Mixes all four kinds: define-a-variable, write-a-function, fix-a-bug,
    # multiple choice, and one written answer.
    "homework_01": dict(
        title="Homework 1 — Python basics",
        unit=3,          # spans basics, strings and booleans (is_even)
        open=True,
        intro="Nine questions on variables, arithmetic, strings, and functions. "
              "Write your answer, hit Run to test it, then Submit the whole "
              "assignment for a score. The written question is read by your instructor.",
        problems=[
            # --- variables & arithmetic ---
            "sum_total",
            "remainder_mod",
            "str_upper",
            # --- writing & fixing functions ---
            "double_fix",
            "area_rect",
            "is_even",
            # --- concepts: read code, don't write it ---
            "mcq_str_plus_int",
            "mcq_floor_div",
            # --- explain in your own words ---
            "written_plus_vs_star_hello",
        ],
    ),
    "lesson_01": dict(
        title="Lesson 1 — the basics",
        unit=3,          # is_even needs comparisons
        open=True,
        intro="Type your answer in each box. Run coding cells to test them, then "
              "submit the whole lesson for instant feedback.",
        problems=[
            "sum_total", "remainder_mod", "double_fix", "area_rect", "is_even",
            "mcq_str_plus_int", "mcq_floor_div", "written_plus_vs_star_hello",
        ],
    ),
    "lesson_02": dict(
        title="Lesson 2 — strings & functions",
        unit=2,
        open=False,     # <-- closed, so you can see the locking work
        intro="More practice with text and writing your own functions.",
        problems=[
            "str_upper", "str_len", "shout", "first_letter",
            "mcq_len_cat", "mcq_concat_abcd", "written_plus_vs_star",
        ],
    ),
}
