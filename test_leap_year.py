from leap_year import is_leap_year
def test_is_leap_year_divisible_by_4():
    assert is_leap_year (2020) is True
    
def test_is_not_leap_year ():
    assert is_leap_year (2023) is False  