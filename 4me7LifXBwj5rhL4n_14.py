
import math
def circle_or_square(rad, area):
  pi = 3.14
  cir = 2 * pi * rad
  sq = 4 * math.sqrt(area)
  if cir > sq:
    return True
  elif cir < sq:
    return False

