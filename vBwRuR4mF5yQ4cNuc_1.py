
def sum_of_missing_nums(lst):
  s = set(int(n) for n in lst if n.isdigit())
  return max(s) - min(s) - len(s) + 1

