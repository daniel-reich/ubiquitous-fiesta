
from itertools import combinations
def product_pair(lst, k):
  if len(lst)<k:
    return None
  if k == 1:
    return (min(lst), max(lst))
  prod = lambda x: eval('*'.join(map(str, x)))
  l = [prod(i) for i in combinations(lst, k)]
  return (min(l), max(l))

