
import math
def foil(length):
  r = 2
  i = 0
  while length>0:
    length -= r*math.pi
    if i:
      r += .0025
    i = 1-i
  return round(2*r+0.0025*i,4)

