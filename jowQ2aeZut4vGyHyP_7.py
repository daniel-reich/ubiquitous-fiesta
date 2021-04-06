
from math import *
def convert(slope):
  positive = True
  if slope < 0:
    positive = False
  num = float(slope * slope + 1)
  x = sqrt(1.0 / num)
  if positive:
    return round(180.0 * asin(x) / pi)
  return 180 - round(180 * asin(x) / pi)

