
import math
​
def convert(slope):
  return 90 - int(round(math.atan(slope) * 180 / math.pi))

