
import math
def circle_or_square(rad, area):
  square_perimeter = math.sqrt(area) * 4
  circle_perimeter = rad * math.pi * 2
  return circle_perimeter > square_perimeter

