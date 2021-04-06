
def count_missing_nums(lst):
  lst = [int(i) for i in lst if i.isnumeric()]
  return max(lst) - min(lst) - len(lst) + 1

