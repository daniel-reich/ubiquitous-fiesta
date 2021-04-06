
import itertools
def product_pair(lst, k):
  def prod(lst):
    p = 1
    for num in lst:
      p *= num
    return p
  if len(lst) < k:
    return None
  triplets = list(itertools.combinations(lst, k))
  triplets = list(map(prod, triplets))
  return (min(triplets), max(triplets))

