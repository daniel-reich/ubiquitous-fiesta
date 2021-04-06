
def accumulating_product(lst):
  from functools import reduce
  return [reduce((lambda x, y: x*y), lst[:x]) for x in range(1, len(lst)+1)]

