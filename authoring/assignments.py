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
    # Homework 1 is a SERIES OF CHALLENGES, not one big submit-at-the-end form.
    # Students solve each one on its own and it ticks off; the homework is done
    # when all ten are green. mode="challenges" is what does that.
    "homework_01": dict(
        title="Homework 1 — Python basics",
        # covers variables, math, strings, functions and if/else — i.e. units 1-5.
        # Anything beyond (lists, loops, dicts) stays hidden until a later homework.
        unit=5,
        open=True,
        mode="challenges",
        intro="Ten challenges to get you going. Solve them in any order — each one "
              "checks itself the moment you hit Submit, and you can retry as many "
              "times as you like. No penalty for a wrong answer, so experiment.",
        problems=[
            # 1-2: the ramp in. One line each, impossible to get lost.
            "hello_438",            # how a challenge works, start to finish
            "pizza_slices_each",    # assign one variable
            # 3-5: your first functions
            "sum_total",
            "addition",
            "next_num",
            # 6: read the examples, find the pattern yourself
            "convert_minutes",
            # 7-8: read broken code and fix it — the print-vs-return trap first
            "seats_left_print_bug",
            "double_fix",
            # 9-10: read code without writing any
            "mcq_four_vs_string_four",
            "mcq_floor_div",
        ],
    ),
    "lesson_01": dict(
        title="Lesson 1 — the basics",
        unit=4,          # is_even needs comparisons
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
        unit=3,          # shout/first_letter are functions, not just strings
        open=False,     # <-- closed, so you can see the locking work
        intro="More practice with text and writing your own functions.",
        problems=[
            "str_upper", "str_len", "shout", "first_letter",
            "mcq_len_cat", "mcq_concat_abcd", "written_plus_vs_star",
        ],
    ),

    # A Colab-notebook homework, for material that can't run in the browser.
    # The notebook (notebooks/hw_molecules_rdkit.ipynb) is the homework; the app
    # teaches the concept, hands off, and records the check-in.
    # ── After you upload the notebook to Colab, paste its share link into `url`. ──
    "hw_molecules": dict(
        title="Homework 7 — Working with molecules",
        unit=16,
        open=False,               # release once the earlier units are done
        mode="notebook",
        url="https://colab.research.google.com/",   # <-- replace with your notebook's Colab link
        intro="Your first computational-chemistry homework. You'll use RDKit — a real "
              "cheminformatics toolkit — to turn text descriptions of molecules into "
              "objects you can measure. It runs in Google Colab (free, nothing to install). "
              "Open it, work through the problems, then come back and check in.",
        preview="from rdkit import Chem\n"
                "from rdkit.Chem import Descriptors\n\n"
                "caffeine = Chem.MolFromSmiles(\"CN1C=NC2=C1C(=O)N(C(=O)N2C)C\")\n"
                "print(round(Descriptors.MolWt(caffeine), 1))   # 194.2",
        checkin=dict(
            question="Run the check-in cell at the end of the notebook. What molecular "
                     "weight did it print for caffeine (to 1 decimal)?",
            expected=194.2, tol=0.1, unit="g/mol",
        ),
    ),
}
