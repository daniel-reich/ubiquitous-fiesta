
import math
def circle_or_square(rad, area):
  side = math.sqrt(area)
  
  circum = (2 * 3.14 * rad)
  per = (4 * side)
  
  if circum > per :
    return True
  else:
    return False

