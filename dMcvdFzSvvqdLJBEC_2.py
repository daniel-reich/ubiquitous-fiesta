
def num_of_days(cost, savings, start):
    amt = savings
    days = 0
    while True:
        for i in range(7):
            amt += start + i
            days += 1
            if amt >= cost:
                return days
        start += 1

