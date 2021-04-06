
import math
​
def cone_volume(h, r):
  if h and r > 0:
     x = ((math.pi * (r ** 2) * h) / 3)
     return round(x , 2)
  else:
    return 0

