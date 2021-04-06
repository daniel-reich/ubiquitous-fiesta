
import math
def foil(length):
  d=4
  s=0
  while s<length:
    s+=d*math.pi
    d+=0.005
  if s-length>d*math.pi/2:
    d=d-0.0025
  return round(d,4) if length else 4

