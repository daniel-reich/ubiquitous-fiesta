
import math
def circle_or_square(rad, area):
  perimeter = 4*math.sqrt(area)
  circumference = 2 * 3.14 * rad
  if circumference > perimeter:
    return True
  else:
    return False

