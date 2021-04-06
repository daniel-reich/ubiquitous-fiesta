
def get_budgets(lst):
  budget_sum = 0
  for i in range(len(lst)):
    budget_sum += lst[i]["budget"]
    
  return budget_sum

