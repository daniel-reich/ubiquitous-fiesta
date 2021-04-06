
def leap_year(yr):
    return yr in (list(filter(lambda y: y % 100, range(1000, 3000, 4))) + list(range(1200, 3000, 400)))

