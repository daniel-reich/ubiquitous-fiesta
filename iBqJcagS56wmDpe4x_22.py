
import math
def vol_shell(r1, r2):
  return abs(round((4*math.pi*(r1**3-r2**3))/3, 3))

