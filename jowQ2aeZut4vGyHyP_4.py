
import math
def convert(slope):
  if slope != 0:
    x = round(math.degrees(math.atan(1/slope)))
    while x > 180:
      x-=180
    while x < 0:
      x+=180
    return x
  else:
    return 90

