"""
assignments.py — your saved assignments. Each one is just a SELECTION of problem
ids from bank.py, in the order students see them.

To make a new assignment: add an entry here (or use the visual builder,
builder.html, which writes the line for you to paste), then run:
    python build.py <assignment_id> --push "<grader-url>" --token "<token>"

Reuse is free: list the same problem id in as many assignments as you like.
"""

ASSIGNMENTS = {
    "lesson_01": dict(
        title="Lesson 1 — the basics",
        intro="Type your answer in each box. Run coding cells to test them, then "
              "submit the whole lesson for instant feedback.",
        problems=[
            "sum_total", "remainder_mod", "double_fix", "area_rect", "is_even",
            "mcq_str_plus_int", "mcq_floor_div", "written_plus_vs_star_hello",
        ],
    ),
    "lesson_02": dict(
        title="Lesson 2 — strings & functions",
        intro="More practice with text and writing your own functions.",
        problems=[
            "str_upper", "str_len", "shout", "first_letter",
            "mcq_len_cat", "mcq_concat_abcd", "written_plus_vs_star",
        ],
    ),
}
