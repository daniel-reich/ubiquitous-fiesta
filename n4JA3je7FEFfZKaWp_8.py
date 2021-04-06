
def million_in_month(first_month, multiplier):
    #goal = 10**6# or 1000000;
    count = 0
    T = 0;
    while T < 1000000:
      T += first_month
      first_month *= multiplier
      count += 1
    return count

