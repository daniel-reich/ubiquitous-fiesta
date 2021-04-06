
def get_budgets(lst):
  b = 0
  for i in lst:
    l = lst.index(i)
    b += lst[l].get("budget")
  return b

