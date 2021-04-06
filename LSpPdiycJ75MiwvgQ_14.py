
import math
def grid_pos(lst):
  return math.factorial(lst[0] + lst[-1]) / math.factorial(lst[0]) / math.factorial(lst[-1])

