
import itertools
def accumulating_product(lst):
  return list(itertools.accumulate(lst, lambda a,b : a*b))

