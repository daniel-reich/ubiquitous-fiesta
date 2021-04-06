
import math
def convert(slope):
  return 90 if slope==0 else round(math.degrees(math.atan(1/slope)))%180

