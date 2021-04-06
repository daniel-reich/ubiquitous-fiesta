
from numpy import prod
def combinations(*a):
  return prod([x for x in a if x>0])

