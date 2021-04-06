
from itertools import *
def merge_arrays(a, b):
  return list(filter(lambda x: x is not None, chain(*zip(a+[None]*len(b), b+[None]*len(a)))))

