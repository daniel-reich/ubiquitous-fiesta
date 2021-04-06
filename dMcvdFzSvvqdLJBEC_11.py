
def num_of_days(cost, savings, start):
    week, days, bank = 0, 0, savings
    while bank <= cost:
        daily = start + week
        for day in range(7):
            days += 1
            bank += daily
            if bank >= cost:
                return days
            daily += 1
        week += 1
    return days

