
def sum_minimums(lst):
  result = 0
  for l in lst:
    result += min(l)
  return result

