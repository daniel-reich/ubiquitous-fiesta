
from functools import reduce
def get_products(lst):
  l = []
  for index, x in enumerate(lst):
    e = lst.copy()
    e.pop(index)
    l.append(reduce(lambda x, y: x*y, e))
  return l

