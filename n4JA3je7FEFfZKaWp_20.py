
def million_in_month(first_month, multiplier):
  months,total = 0,0
  while total < 10**6:
    total += first_month
    months += 1
    first_month *= multiplier
  return months

