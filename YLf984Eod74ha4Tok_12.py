
def leap_year(yr):
    return (bool(yr % 4) + bool(yr % 100) + bool(yr % 400) + 1) % 2

