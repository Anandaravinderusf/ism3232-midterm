
# Terminal Record: Cloudstep Software

## 1. Building the project

These are the terminal commands used to create and connect the project.

```bash
cd ~
mkdir ism3232-midterm
cd ism3232-midterm
git init
git branch -M main
python3 -m venv .venv
source .venv/bin/activate
pip install pytest ruff
pip freeze > requirements.txt
touch business_rules.py main.py
mkdir -p tests
touch tests/__init__.py tests/test_business_rules.py
printf '.venv/\n__pycache__/\n*.pyc\n.pytest_cache/\n.ruff_cache/\n' > .gitignore
git add .
git commit -m "Initialize midterm project and Python environment"
git remote add origin https://github.com/Anandaravinderusf/ism3232-midterm.git
git push -u origin main
touch commands.md
touch README.md
```

## 2. The virtual environment

Command:

```bash
which python3
```

Output:

```text
/Users/ananda/ism3232-midterm/.venv/bin/python3
```

The output shows that Python is running from the `.venv/bin` folder inside my midterm project, which confirms that the virtual environment is active.

## 3. The project structure

Command:

```bash
tree -L 2
```

Output:

```text
.
├── README.md
├── __pycache__
│   └── business_rules.cpython-314.pyc
├── business_rules.py
├── commands.md
├── main.py
├── requirements.txt
└── tests
    ├── __init__.py
    ├── __pycache__
    └── test_business_rules.py

4 directories, 8 files
```

The `.venv` folder exists on my computer but is excluded from GitHub by `.gitignore` because the virtual environment can be recreated from `requirements.txt`.

## 4. Every function and test

Command:

```bash
rg 'def '
```

Output:

```text
business_rules.py
19:def calculate_license_cost(seat_price: float, seats: int) -> float:
26:def get_seat_discount(seats: int, education: bool = False) -> float:
38:def calculate_license_total(
54:def needs_contract_review(total: float) -> bool:
61:def gets_trainer(seats: int, total: float) -> bool:
68:def total_licensed(orders: list) -> float:
81:def largest_license(orders: list) -> str:
100:def format_license_line(

tests/test_business_rules.py
13:def test_license_cost():
17:def test_license_cost_with_zero_seats():
21:def test_discount_below_ten_seats():
25:def test_discount_at_ten_seats():
29:def test_discount_at_forty_nine_seats():
33:def test_education_discount_at_fifty_seats():
37:def test_non_education_discount_at_fifty_seats():
41:def test_education_discount_below_fifty_seats():
45:def test_license_total_with_onboarding():
49:def test_license_total_with_discount():
53:def test_onboarding_at_limit():
57:def test_onboarding_above_limit():
61:def test_contract_review_at_limit():
65:def test_contract_review_above_limit():
69:def test_trainer_below_both_limits():
73:def test_trainer_at_seat_limit():
77:def test_trainer_below_seat_limit():
81:def test_trainer_above_total_limit():
85:def test_trainer_at_total_limit():
89:def test_total_licensed_multiple_orders():
97:def test_total_licensed_empty_list():
101:def test_largest_license():
109:def test_largest_license_tie():
117:def test_largest_license_empty_list():
121:def test_format_license_line_no_review_no_trainer():
126:def test_format_license_line_with_review_and_trainer():
131:def test_format_license_line_trainer_only():
```

The `business_rules.py` file defines 8 functions, and `tests/test_business_rules.py` defines 27 pytest tests.

## 5. Which files print

Command:

```bash
rg -l 'print'
```

Output:

```text
main.py
```

`main.py` is the Python file that prints the order report. `business_rules.py` is not in the list because its functions return values instead of printing them.

## 6. The commit history

Command:

```bash
git log --oneline
```

Output:

```text
c22f14c (HEAD -> main, origin/main, origin/HEAD) Build Cloudstep order report and summary
7ed8a48 Add formatted license report lines with tests
7badbfa Add license aggregation and largest order functions with tests
639468d Add dedicated trainer eligibility and boundary tests
705b55b Add license total and contract review rules with tests
bdcb5f5 Add license cost and seat discount rules with tests
dbc58f8 Initialize midterm project and Python environment
```

There were 7 commits in the repository before committing this terminal record. The history shows the project being built in stages, beginning with project setup and continuing through the business rules, tests, and final report.
