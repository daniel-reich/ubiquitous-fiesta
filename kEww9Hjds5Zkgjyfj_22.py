
from itertools import zip_longest
​
​
def replace_next_largest(lst):
  swap = dict(zip_longest(sorted(lst), sorted(lst)[1:], fillvalue=-1))
  return [swap[i] for i in lst]

