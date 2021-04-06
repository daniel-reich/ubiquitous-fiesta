
def num_of_days(cost, savings, start):
    day_in_week = 1
    start_this_week = start
    cost_sav = cost - savings
    total_days = 0
    while True:
        if cost_sav <= 0:
            return total_days
            break
        elif day_in_week == 1:
            cost_sav = cost_sav - (start_this_week)
            day_in_week += 1
            total_days += 1
        elif day_in_week > 1 and day_in_week < 7:
            cost_sav = cost_sav - (start_this_week + day_in_week - 1)
            day_in_week += 1
            total_days += 1
        elif day_in_week == 7:
            cost_sav = cost_sav - (start_this_week + day_in_week - 1)
            day_in_week = 1
            start_this_week += 1
            total_days += 1

