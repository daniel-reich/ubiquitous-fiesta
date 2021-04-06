
import math
def vol_shell(r1, r2):
  r1 = abs(r1)
  r2 = abs(r2)
  if r1 > r2:
    V = (4/3) * math.pi * (r1**3 - r2**3)
    return round(V,3)
  elif r2 > r1:
    V = (4/3) * math.pi * (r2**3 - r1**3)
    return round(V,3)
  else:
    return 0

