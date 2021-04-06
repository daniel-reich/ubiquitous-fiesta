
from itertools import combinations
import numpy as np
def product_pair(lst, k):
  pairs = [np.prod(np.array(arr)) for arr in list(combinations(lst,k))]
  return (min(pairs),max(pairs)) if len(pairs)>0 else None

