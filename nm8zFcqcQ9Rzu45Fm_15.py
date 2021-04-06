
from itertools import chain, zip_longest
def bridge_shuffle(lst1, lst2):
  return list(filter(None,chain(*zip_longest(lst1,lst2))))

