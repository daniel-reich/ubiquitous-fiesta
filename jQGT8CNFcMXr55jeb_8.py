
def numbers_sum(lst):
  total = 0
  for i in lst:
    if type(i) == int:
      total += i
  return total

