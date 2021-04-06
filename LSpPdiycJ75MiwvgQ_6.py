
import math
def grid_pos(lst):
  n = sum(lst)
  r = lst[0]
  s = n-r
  return math.factorial(n)/(math.factorial(r)*math.factorial(s))

