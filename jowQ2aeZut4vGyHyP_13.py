
import math
def convert(slope):
  if slope > 0:
    return round(math.atan(1/slope)*(180)/math.pi,0)
  elif slope < 0:
    return round(math.atan(-slope)*(180)/math.pi+90,0)
  else:
    return 90

