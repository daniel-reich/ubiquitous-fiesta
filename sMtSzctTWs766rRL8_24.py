
from functools import reduce
def magnitude(lst):
  return reduce(lambda x,y:(x**2+y**2)**.5,lst) if lst else 0

