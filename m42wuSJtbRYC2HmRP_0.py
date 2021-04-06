
from math import log
def largest_exponential(lst):
  return lst.index(max(lst,key=lambda x: x[-1]*log(x[0]))) + 1

