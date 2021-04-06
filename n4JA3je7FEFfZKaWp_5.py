
def million_in_month(first_month, multiplier):
  count = 1
  salary = first_month*multiplier
  tot = first_month
​
  while tot < 10**6:
    tot += salary
    salary *= multiplier
    count += 1
​
  return count

