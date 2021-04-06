
def get_budgets(lst):
  budgets =[sub["budget"] for sub in lst]
  return sum(budgets)

