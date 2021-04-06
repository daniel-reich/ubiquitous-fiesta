
def sum_minimums(lst):
  res = 0
  for row in lst:
    res += min(row)
  return res

