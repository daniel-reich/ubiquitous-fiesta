
import math
​
ref = -4 * math.pi + 16 * math.atan(0.5) + 6.4
​
def red_area(r):
  return 0 if r == 0 else round(ref * (r / 4.)**2, 3)

