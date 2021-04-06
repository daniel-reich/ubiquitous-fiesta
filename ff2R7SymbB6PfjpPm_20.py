
def get_budgets(lst):
  sum = 0
  for x in lst:
    for y , z in x.items():
      if y == "budget":
        sum += z
  return sum

