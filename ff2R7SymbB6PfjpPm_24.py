
def get_budgets(lst):
  all_bud_lst = [x['budget'] for x in lst]
  all_bud_lst = list(map(int, all_bud_lst))
  return sum(all_bud_lst)

