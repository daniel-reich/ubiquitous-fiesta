
from itertools import zip_longest
def merge_arrays(a, b):
  return [y for x in zip_longest(a, b) for y in x if y is not None]

