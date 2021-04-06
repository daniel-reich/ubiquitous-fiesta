
import math
def largest_exponential(lst):
  return lst.index(max(lst, key=lambda x:math.log2(x[0])*x[1])) + 1

