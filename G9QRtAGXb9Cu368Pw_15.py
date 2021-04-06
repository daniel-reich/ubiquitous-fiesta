
from functools import reduce
def combinations(*items):
  items = filter(lambda a: a != 0, items)
  return reduce(lambda x,y: x * y,items)

