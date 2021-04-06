
def million_in_month(salary, multiplier):
  bank, months = salary, 1
  while bank < 1000000:
    salary *= multiplier
    bank += salary
    months += 1
  return months

