
def get_budgets(lst):
  budgets = []
  for i in lst:
    budgets.append(i["budget"])
  integers = [int(i) for i in budgets]
  return sum(integers)

