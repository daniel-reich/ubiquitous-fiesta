
import math
def circle_or_square(rad, area):
  peri_square = 4 * math.sqrt(area)
  peri_circle = 2 * 3.14 * rad
  if peri_circle > peri_square: return True 
  else: return False

