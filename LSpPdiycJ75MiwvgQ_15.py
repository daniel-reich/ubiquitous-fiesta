
import math
def grid_pos(lst):
  rights = lst[1]
  ups = lst[0]
  total = rights+ups
  combos = math.factorial(total) / math.factorial(rights)
  return combos / math.factorial(ups)

