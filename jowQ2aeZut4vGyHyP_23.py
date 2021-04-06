
import math
def convert(slope):
  if slope == 0:
    return 90;
  if slope < 0:
    angle = round(math.degrees(math.atan(-1/slope)));
    return 180 - angle;
  else:
    angle = round(math.degrees(math.atan(1/slope)));
    return  angle;

