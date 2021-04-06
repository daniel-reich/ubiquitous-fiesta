
def sum_of_missing_nums(lst):
  lst = [int(i) for i in lst if i.isdigit()]
  return max(lst) - min(lst) + 1 - len(lst)

