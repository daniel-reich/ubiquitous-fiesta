
from math import sqrt
def areaofhexagon(x):
  if x < 0 or x ==0:
    return None
  return round(((3*sqrt(3))/2) * (x**2),1)

