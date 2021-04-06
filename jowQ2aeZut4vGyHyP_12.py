
from numpy import degrees
from math import atan
def convert(slope):
  return 90 if slope==0 else round(degrees(atan(1/slope))%180)

