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
            "hello_438",
            "cb_eq_vs_assign",
            "nickname_filled",
            "pb_not_true",
            "trim_username",
            "seats_left_print_bug",
            "cf_else",
            "whole_dollars_only",
            "pb_greater",
            "thermostat_gap",
            "cf_indent",
            "keep_playing_flag",
            "mcq_four_vs_string_four",
            "cart_total_from_text",
            "g2_fix_print_not_return",
            "pb_str_case",
            "g2_fix_missing_return",
            "pb_eq",
            "va_is_positive",
            "cb_and_both",
            "mcq_precedence_power",
            "fix_remove_dashes",
        ],
    ),
    "homework_02": dict(
        title="Homework 2 — more Python basics",
        unit=5, open=True, mode="challenges",
        intro="Another 22 challenges across variables, strings, functions and logic — "
              "more predict-the-output, spot-the-bug and write-it-yourself. Solve in any "
              "order; each checks itself.",
        problems=[
            "playlist_title",
            "pizza_slices_each",
            "coffee_order_ticket",
            "g2_make_greeting",
            "free_shipping",
            "wa_pass_or_fail",
            "loading_bar",
            "calculate_exponent",
            "fix_both_on",
            "g2_default_two_ways",
            "g2_concept_local_variable",
            "p_len_with_space",
            "g2_concept_def_runs",
            "g2_print_f3f4",
            "concept_first_index",
            "fix_matches_secret",
            "mcq_slice_end",
            "g2_multiple_returns",
            "cf_elif_only_first",
            "mcq_floor_div",
            "p_true_div_seven_two",
            "wf_missing_colon",
        ],
    ),
    "homework_03": dict(
        title="Homework 3 — even more practice",
        unit=5, open=True, mode="challenges",
        intro="A third set of 22. If you can breeze through these, you've got the basics "
              "cold. Predict, fix, and write.",
        problems=[
            "g2_wrong_arg_count",
            "tri_area",
            "shout",
            "g2_code_after_return",
            "g2_final_price",
            "crowd_chant",
            "sum_total",
            "p_floor_div_seven_two",
            "wrong_index_range",
            "elevator_direction",
            "pf_temp_elif",
            "letters_in_banana",
            "football_points",
            "g2_wrong_missing_colon",
            "p_last_char_neg",
            "concept_augmented_meaning",
            "g2_print_vs_return_none",
            "p_mod_ten_three",
            "mcq_function_with_no_return",
            "g2_concept_which_is_call",
            "concept_float_value",
            "p_in_word",
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

    # ─────────────────────────────────────────────────────────────────────────
    # SCIENCE-STACK HOMEWORKS — each is a Colab notebook (in notebooks/), because
    # these libraries can't run in the browser. The app teaches the concept, hands
    # off to the notebook, and records a check-in keyed to a value the notebook
    # prints. Upload each notebook to Colab, paste its share link into `url`, then
    # flip open=True to release it. Check-in answers are computed + verified.
    # ─────────────────────────────────────────────────────────────────────────
    "hw_pandas": dict(
        title="Data with pandas",
        unit=12, open=False, mode="notebook",
        url="https://colab.research.google.com/",   # notebooks/hw_pandas_basics.ipynb
        intro="Real data lives in tables. pandas is how Python handles them — loading, "
              "filtering, sorting, and summarising a spreadsheet in a few lines. Work "
              "through the notebook, then check in.",
        preview="import pandas as pd\n\n"
                "df = pd.DataFrame({\"Sample\": [\"S1\",\"S2\"], \"Purity\": [98.2, 88.4]})\n"
                "print(df[df[\"Purity\"] >= 95])   # just the pure ones",
        checkin=dict(question="In the notebook, how many samples in samples.csv have a "
                              "Purity of at least 95? (the check-in cell prints it)",
                     expected=4, tol=0.5),
    ),
    "hw_pandas_group": dict(
        title="Grouping & merging data",
        unit=12, open=False, mode="notebook",
        url="https://colab.research.google.com/",   # notebooks/hw_pandas_group.ipynb
        intro="The two moves that turn a table into an answer: grouping (one row per "
              "category) and merging (joining two tables). Work through the notebook, "
              "then check in.",
        preview="df.groupby(\"lab\")[\"yield_pct\"].mean()   # each lab's average yield",
        checkin=dict(question="The check-in cell groups samples by lab and prints the "
                              "highest lab-average yield (1 decimal). What is it?",
                     expected=38.3, tol=0.2),
    ),
    "hw_plotting": dict(
        title="Plotting your data",
        unit=13, open=False, mode="notebook",
        url="https://colab.research.google.com/",   # notebooks/hw_plotting.ipynb
        intro="A plot is how you SEE data. matplotlib draws lines, scatters, bars and "
              "histograms — and this homework is as much about choosing the RIGHT plot "
              "and reading one honestly as drawing it. Work through it, then check in.",
        preview="import matplotlib.pyplot as plt\n\n"
                "plt.plot(months, yields)\n"
                "plt.xlabel(\"month\"); plt.ylabel(\"yield %\")   # a plot with no labels is useless\n"
                "plt.show()",
        checkin=dict(question="The notebook plots 12 months of reaction yields. How many "
                              "months had a yield above the average? (the check-in prints it)",
                     expected=6, tol=0.5),
    ),
    "hw_numpy": dict(
        title="Numbers at scale — NumPy",
        unit=14, open=False, mode="notebook",
        url="https://colab.research.google.com/",   # notebooks/hw_numpy.ipynb
        intro="NumPy does math on whole arrays at once — no loop needed — and it's what "
              "pandas, plotting and every science library is built on. Work through the "
              "notebook, then check in.",
        preview="import numpy as np\n\n"
                "readings = np.array([100, 112, 98, 120])\n"
                "print(readings[readings > 100].mean())   # mean of just the high ones",
        checkin=dict(question="The check-in builds 50 seeded readings, keeps those above "
                              "100, and prints their mean (2 decimals). What is it?",
                     expected=111.67, tol=0.2),
    ),
    "hw_regression": dict(
        title="Fitting data — regression",
        unit=15, open=False, mode="notebook",
        url="https://colab.research.google.com/",   # notebooks/hw_regression.ipynb
        intro="Fitting a line to data — and, more importantly, reading what the fit MEANS: "
              "the slope in real units, R² as how much the line explains, and when a line "
              "is the wrong model. Work through the notebook, then check in.",
        preview="from scipy import stats\n\n"
                "fit = stats.linregress(x, y)\n"
                "print(fit.slope, fit.rvalue**2)   # slope, and R²",
        checkin=dict(question="The check-in fits a line to a seeded dataset and prints the "
                              "fitted slope (2 decimals). What is it?",
                     expected=1.88, tol=0.03),
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
    "hw_structures": dict(
        title="Protein structures",
        unit=17, open=False, mode="notebook",
        url="https://colab.research.google.com/",   # notebooks/hw_structures.ipynb
        intro="A protein structure is a list of atoms with 3D coordinates — and once you "
              "load one, it's just a pandas DataFrame, so everything you already know "
              "applies. You'll load lysozyme from the PDB and measure it. Work through the "
              "notebook, then check in.",
        preview="from biopandas.pdb import PandasPdb\n\n"
                "atoms = PandasPdb().fetch_pdb(\"1AKI\").df[\"ATOM\"]\n"
                "print(len(atoms[atoms[\"element_symbol\"] == \"C\"]))   # carbon atoms",
        checkin=dict(question="The check-in cell counts the carbon atoms in the 1AKI "
                              "structure. How many are there?",
                     expected=613, tol=0.5),
    ),
}
