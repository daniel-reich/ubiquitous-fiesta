
def get_budgets(lst):
  sum = 0
  for element in lst:
    value = element.get("budget")
    sum = sum+value
  return sum

