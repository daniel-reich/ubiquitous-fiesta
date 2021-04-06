
def num_of_days(cost, savings, start):
    target = cost - savings
    total = 0
    monday = start
    n_days = 0
    while total < target:
        for d in range(7):
            add_on = monday + d
            total += add_on
            n_days += 1
            if total >= target:
                break
        monday += 1
    return n_days

