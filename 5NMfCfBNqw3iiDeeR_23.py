
def sum_minimums(lst):
  min_total = 0
  for i in lst:
    min_total += min(i)
  return min_total

