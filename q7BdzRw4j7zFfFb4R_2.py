
from itertools import zip_longest
​
def merge_arrays(a, b):
  """Takes two lists combines them by alternatingly taking elements from each list in turn."""
  # use itertools.zip_longest() to aggregate elements from each list
  zip_list = list(zip_longest(a,b))
  # flatten out the tuples and pull out the zip_longest fillvalue None
  flattened = [a for b in zip_list for a in b if a != None]
  return flattened

