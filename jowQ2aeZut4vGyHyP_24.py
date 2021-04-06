
from math import atan, degrees
​
def convert(slope):
  if slope == 0:
      return 90
  angle = round(degrees(atan(1/slope)))
  if angle < 0:
    return 180 + angle
  return angle

