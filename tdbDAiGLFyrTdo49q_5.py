
import math
def find_difference(x, y):
  v1 = x[0]*x[1]*x[2]
  v2 = y[0]*y[1]*y[2]
  test = v1-v2
  return int(math.fabs(test)) 
find_difference([1,9,25],[10,7,9])

