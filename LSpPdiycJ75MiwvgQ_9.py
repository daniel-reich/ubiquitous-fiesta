
import math
def grid_pos(lst):
  a = math.factorial(lst[0] + lst[1])
  ans = a/( math.factorial(lst[0]) * math.factorial(lst[1]) )
  return ans

