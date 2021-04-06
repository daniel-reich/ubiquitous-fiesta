
import math
​
def convert(slope):
  if not slope: 
    return 90
  res = round(abs(math.degrees(math.atan(1/slope))))
  return 180 - res if slope < 0 else res

