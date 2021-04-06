
import math
def circle_or_square(rad, area):
  squareside = math.sqrt(float(area))
  perimeter = squareside*4
  circumference = 2 * 3.14 * float(rad)
  q = bool(0)
  if circumference > perimeter:
    q = 1
  return q

