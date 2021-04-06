
import math
def shift_to_right(x, y, z = 1):
  if y <=0:
    return math.floor(x/z)
  else:
    return shift_to_right(x, y-1, z*2)

