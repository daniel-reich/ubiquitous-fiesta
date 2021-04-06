
import math
def circle_or_square(rad, area):
  if (math.pi * 2 * rad) > (math.pow(area, 1/2) * 4):
    return True
  else:
    return False

