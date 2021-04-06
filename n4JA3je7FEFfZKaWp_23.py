
def million_in_month(first_month, multiplier):
    total = first_month
    month = 0
    while total < 1000000:
        month += 1
        total += first_month * pow(multiplier, month)
    return month + 1

