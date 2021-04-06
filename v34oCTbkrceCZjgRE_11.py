
from math import floor
def shift_to_right(x, y):
  if y == 0:
    return x
  else:
    return shift_to_right(floor(x/2),y-1)

