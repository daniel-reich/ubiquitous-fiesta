
def numbers_sum(lst):
  total = 0
  for x in lst:
    if isinstance(x, int) and not isinstance(x, bool):
      total = total + x
  return total

