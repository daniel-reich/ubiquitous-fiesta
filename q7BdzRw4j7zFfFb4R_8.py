
from itertools import zip_longest 
def merge_arrays(a, b):
   return [x for t in zip_longest(a, b) for x in t  if x]

