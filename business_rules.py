# business_rules.py
# Cloudstep Software - Business Rules

MIN_DISCOUNT_SEATS = 10
MIN_EDUCATION_SEATS = 50

STANDARD_DISCOUNT = 0.07
EDUCATION_DISCOUNT = 0.16
NO_DISCOUNT = 0.0


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
