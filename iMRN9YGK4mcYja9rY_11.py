
def accumulating_product(lst):
  total, new = 1, []
  for x in lst:
    total *= x
    new += [total]
  return new

