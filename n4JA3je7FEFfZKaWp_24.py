
def million_in_month(first_month, multiplier):
  sum = 0
  months = 1
  while sum < 1000000:
    m = multiplier ** months
    sum += m * first_month
    months += 1
  return months

