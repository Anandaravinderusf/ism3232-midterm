
# ISM3232 Midterm: Cloudstep Software

- **Name:** Ananda Ravinder
- **Version:** EPSILON
- **Date:** October 21, 2026

## What This Program Does

This program processes software license orders for Cloudstep Software. It calculates each customer's license cost, applies the correct discount, and adds an onboarding fee when required. It also determines whether an order needs contract review or a dedicated trainer. Finally, it prints a report showing all eight orders and a summary of the results.

## Business Rules

1. The license cost is calculated by multiplying the price per seat by the number of seats.
2. Orders with fewer than 10 seats receive no discount. Orders with 10 through 49 seats receive a 7% discount.
3. Education customers ordering 50 or more seats receive a 16% discount. Non-education customers with 50 or more seats receive the standard 7% discount.
4. A $60 onboarding fee is added when the discounted license cost is $400 or less.
5. License totals greater than $5,000 require a contract review.
6. Orders with 25 or more seats, or a license total greater than $3,000, receive a dedicated trainer.

## How to Run

Open a terminal in the project folder and run:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 main.py
```

The program prints the Cloudstep Software order report, including each customer's license total, contract review status, and trainer eligibility. It also displays the total number of orders, total licensed amount, average license total, largest license, contract reviews needed, and trainers assigned.

## How to Test

Run the following commands with the virtual environment activated:

```bash
ruff format --check .
ruff check .
pytest -v
```

The project includes 27 pytest tests covering all eight business functions, discount rules, onboarding fees, contract review requirements, trainer eligibility, and boundary conditions. The tests also verify license totals, the largest order, and report formatting.

## Files in This Repository

- `business_rules.py` — Contains the eight functions that implement Cloudstep Software's business rules.
- `main.py` — Contains the customer orders and prints the complete order report.
- `commands.md` — Records the terminal commands, project structure, function definitions, tests, and Git commit history.
- `README.md` — Explains the project, business rules, setup instructions, testing process, and files.
- `requirements.txt` — Lists the Python packages needed for the project.
- `.gitignore` — Prevents virtual environments, Python cache files, and other unnecessary files from being committed.
- `tests/__init__.py` — Marks the tests directory as a Python package.
- `tests/test_business_rules.py` — Contains the 27 pytest tests for the business functions.

## AI Use Statement

I did not use AI on this exam.
