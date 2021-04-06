
import math
def foil(length,r = 2,turns = 0):
  length_circ = 2 * math.pi * r
  while length > 0:
    length = length - length_circ
    r += 0.0025
    turns += 1
    length_circ = 2 * math.pi * r
  ans = 4 + 2 * ((turns - 1) * 0.0025)
  if abs(length) / length_circ < 0.5 :
    return round(ans + (0.005),4)
  return round(ans + 0.0025,4)

