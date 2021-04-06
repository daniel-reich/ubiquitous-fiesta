
from math import pi
def cone_volume(h, r):
  if h == 0 or r == 0:
    return 0
  
  return round((pi*r**2*h)/3,2)

