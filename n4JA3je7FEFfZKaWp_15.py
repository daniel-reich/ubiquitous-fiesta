
def million_in_month(first_month, multiplier):
    #goal = 10**6# or 1000000;
    months = 1
    constant_val = first_month
    while first_month < 1000000:
      first_month = first_month * multiplier
      first_month += constant_val
      months += 1
    return months

