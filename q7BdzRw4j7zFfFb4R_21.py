
import itertools as it
def merge_arrays(a, b):
  return [i for t in it.zip_longest(a, b) for i in t if i is not None]

