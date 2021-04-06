
from itertools import chain, zip_longest
def merge_arrays(a, b):
  return [i for i in chain(*zip_longest(a, b)) if i is not None]

