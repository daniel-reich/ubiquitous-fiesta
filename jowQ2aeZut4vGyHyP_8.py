
from math import atan, pi
​
def convert(slope):
  return round(90-180*atan(slope)/pi)

