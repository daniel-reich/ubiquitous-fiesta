
def over_time(lst):
    start, end, rate, mult = lst
    if start <= 17:
        if end > 17:
            regular = (17 - start) * rate
            overtime = (end - 17) * rate * mult
        else:
            regular = (end - start) * rate
            overtime = 0
    else:
        regular = 0
        overtime = (end - start) * rate * mult
    return '${:.2f}'.format(round(regular + overtime + 0.001, 2))

