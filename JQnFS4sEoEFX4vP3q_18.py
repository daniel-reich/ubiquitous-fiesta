
import itertools, operator
from functools import reduce
def product_pair(lst, k):
  if k > len(lst):
    return None
  prod = lambda x: reduce(operator.mul, x)
  combs = sorted(prod(c) for c in itertools.combinations(lst, k))
  return combs[0], combs[-1]

