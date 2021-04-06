
from math import pi
def foil(length):
  d, inc = 4, 0.005
  while length > 0:
    c = d * pi
    d += inc if length >= c/2 else inc/2
    length -= c
  return round(d, 4)

