def is_leap_year(year: int) -> bool:
    if not isinstance(year, int):
        raise TypeError("Year must be an integer")

    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False