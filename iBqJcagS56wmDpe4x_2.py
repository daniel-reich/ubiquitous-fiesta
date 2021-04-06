
import math
def vol_shell(r1, r2):
  radiusDiff = abs(r1 ** 3 - r2 ** 3)
  result = (4 / 3) * math.pi * radiusDiff
  return round(result, 3)

