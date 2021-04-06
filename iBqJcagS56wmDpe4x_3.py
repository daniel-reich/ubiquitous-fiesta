
import math
def vol_shell(r1, r2):
  if r1>=r2:
    return abs(round(math.pi*4/3*(r1**3-r2**3), 3))
  else:
    return abs(round(math.pi*4/3*(r2**3-r1**3), 3))

