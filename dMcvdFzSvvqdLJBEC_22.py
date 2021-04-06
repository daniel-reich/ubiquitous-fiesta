
def num_of_days(cost, savings, start):
    amount_saved = 0 + savings
    deposit = start
    num_of_days = 1
    week_range = list(range(8, 1000, 7))
    while amount_saved < cost:
        if num_of_days in week_range:
            deposit = start + (week_range.index(num_of_days) + 1)
        amount_saved += deposit
        deposit += 1
        num_of_days += 1
    return num_of_days - 1

