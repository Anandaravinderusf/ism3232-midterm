# business_rules.py
# Cloudstep Software - Business Rules

MIN_DISCOUNT_SEATS = 10
MIN_EDUCATION_SEATS = 50

STANDARD_DISCOUNT = 0.07
EDUCATION_DISCOUNT = 0.16
NO_DISCOUNT = 0.0

ONBOARDING_FEE = 60.00
ONBOARDING_LIMIT = 400.00
CONTRACT_REVIEW_LIMIT = 5000.00

TRAINER_SEAT_LIMIT = 25
TRAINER_TOTAL_LIMIT = 3000.00


def calculate_license_cost(seat_price: float, seats: int) -> float:
    """
    Return the license cost before discounts.
    """
    return seat_price * seats


def get_seat_discount(seats: int, education: bool = False) -> float:
    """
    Return the discount rate based on seats and customer type.
    """
    if seats >= MIN_EDUCATION_SEATS and education:
        return EDUCATION_DISCOUNT
    elif seats >= MIN_DISCOUNT_SEATS:
        return STANDARD_DISCOUNT
    else:
        return NO_DISCOUNT


def calculate_license_total(
    seat_price: float, seats: int, education: bool = False
) -> float:
    """
    Return the discounted license cost with any onboarding fee.
    """
    cost = calculate_license_cost(seat_price, seats)
    discount = get_seat_discount(seats, education)
    discounted_cost = cost * (1 - discount)

    if discounted_cost <= ONBOARDING_LIMIT:
        discounted_cost += ONBOARDING_FEE

    return discounted_cost


def needs_contract_review(total: float) -> bool:
    """
    Return whether the license total needs contract review.
    """
    return total > CONTRACT_REVIEW_LIMIT


def gets_trainer(seats: int, total: float) -> bool:
    """
    Return True if an order qualifies for a dedicated trainer.
    """
    return seats >= TRAINER_SEAT_LIMIT or total > TRAINER_TOTAL_LIMIT


def total_licensed(orders: list) -> float:
    """Return the combined license total for all orders."""
    total = 0.0

    for order in orders:
        license_total = calculate_license_total(
            order["seat_price"], order["seats"], order["education"]
        )
        total += license_total

    return total


def largest_license(orders: list) -> str:
    """
    Return the company with the largest license total.
    """
    largest_company = ""
    largest_total = 0.0

    for order in orders:
        license_total = calculate_license_total(
            order["seat_price"], order["seats"], order["education"]
        )

        if largest_company == "" or license_total > largest_total:
            largest_total = license_total
            largest_company = order["company"]

    return largest_company


def format_license_line(
    company: str, total: float, contract_review: bool, trainer: bool
) -> str:
    """
    Return a formatted report line for one company.
    """
    review_text = "yes" if contract_review else "no"
    trainer_text = "yes" if trainer else "no"

    return (
        f"{company}: ${total:.2f} | "
        f"contract review: {review_text} | trainer: {trainer_text}"
    )
