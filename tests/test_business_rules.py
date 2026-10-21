from business_rules import (
    calculate_license_cost,
    calculate_license_total,
    get_seat_discount,
    gets_trainer,
    needs_contract_review,
)


def test_license_cost():
    assert calculate_license_cost(40.00, 5) == 200.00


def test_license_cost_with_zero_seats():
    assert calculate_license_cost(40.00, 0) == 0.00


def test_discount_below_ten_seats():
    assert get_seat_discount(9) == 0.0


def test_discount_at_ten_seats():
    assert get_seat_discount(10) == 0.07


def test_discount_at_forty_nine_seats():
    assert get_seat_discount(49) == 0.07


def test_education_discount_at_fifty_seats():
    assert get_seat_discount(50, True) == 0.16


def test_non_education_discount_at_fifty_seats():
    assert get_seat_discount(50, False) == 0.07


def test_education_discount_below_fifty_seats():
    assert get_seat_discount(49, True) == 0.07


def test_license_total_with_onboarding():
    assert round(calculate_license_total(40, 5), 2) == 260.00


def test_license_total_with_discount():
    assert round(calculate_license_total(35, 12, True), 2) == 450.60


def test_onboarding_at_limit():
    assert round(calculate_license_total(400, 1), 2) == 460.00


def test_onboarding_above_limit():
    assert round(calculate_license_total(401, 1), 2) == 401.00


def test_contract_review_at_limit():
    assert needs_contract_review(5000) is False


def test_contract_review_above_limit():
    assert needs_contract_review(5000.01) is True


def test_trainer_below_both_limits():
    assert gets_trainer(24, 3000) is False


def test_trainer_at_seat_limit():
    assert gets_trainer(25, 3000) is True


def test_trainer_below_seat_limit():
    assert gets_trainer(24, 2999) is False


def test_trainer_above_total_limit():
    assert gets_trainer(24, 3000.01) is True


def test_trainer_at_total_limit():
    assert gets_trainer(24, 3000) is False
