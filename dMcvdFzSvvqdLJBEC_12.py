
def num_of_days(cost, savings, start):
    n = 21 + (7 * start)
    total = cost - savings
    a = 7/2
    b = - 7/2 + n
    weeks = (- b + (b ** 2 - 4 * a * -total)**0.5) / (2 * a)
    return int(weeks * 7) + (weeks % 1 != 0)

