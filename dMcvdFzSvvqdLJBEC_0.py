
def num_of_days(cost, savings, start):
    total, days = 0, 0
    cost -= savings
    while total < cost:
        i = start + days/7 if not days%7 else i + 1
        total += i
        days += 1
    return days

