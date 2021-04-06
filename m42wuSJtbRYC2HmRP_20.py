
import math
def largest_exponential(lst):
  A=[x[1]*math.log(x[0]) for x in lst]
  return A.index(max(A))+1

