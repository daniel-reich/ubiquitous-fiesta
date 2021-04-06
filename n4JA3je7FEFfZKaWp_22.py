
def million_in_month(first_month, multiplier):
    month = 1
    total_earnings = 0
    while total_earnings < 10**6:
        first_month *= multiplier
        total_earnings += first_month
        month += 1
    return month

