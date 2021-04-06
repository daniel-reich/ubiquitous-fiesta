
def num_of_days(cost, savings, start):
    days = 0
    while True:
        for i in range(start, start + 7):
            days += 1
            savings += i
            if savings  >= cost:
                return days
        start += 1

