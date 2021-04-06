
def million_in_month(first_month, multiplier):
  month = 1
  savings = first_month
  while savings < 1000000:
    month += 1
    first_month *= multiplier
    savings += first_month
  return month

