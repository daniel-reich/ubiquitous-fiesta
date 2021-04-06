
def million_in_month(first_month, multiplier):
  count = 1
  total = first_month
  while total < 1000000:
    count += 1
    first_month *= multiplier
    total += first_month
  return count

