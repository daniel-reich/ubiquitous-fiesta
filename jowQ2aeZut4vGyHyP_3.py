
import math
def convert(slope):
  angle = math.atan(slope)
  return round(90-(angle*180/math.pi), 0)

