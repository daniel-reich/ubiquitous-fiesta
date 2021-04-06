
import math
​
def vol_shell(r1, r2):
  volume = 4/3 * math.pi * (r1**3 - r2**3)
  return abs(round(volume, 3))

