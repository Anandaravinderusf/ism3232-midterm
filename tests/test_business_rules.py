from business_rules import calculate_license_cost, get_seat_discount


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
