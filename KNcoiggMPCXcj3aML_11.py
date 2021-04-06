
def number_of_days(coordinate):
    x, y = coordinate
    z = abs(x) + abs(y)
    days, travel = 0, 0
    while travel < z:
        days += 1
        if days % 6:
            travel += 1
    return days

