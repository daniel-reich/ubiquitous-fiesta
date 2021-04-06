
import math
def line_length(dot1, dot2):
  x_change = (dot1[0] - dot2[0]) ** 2
  y_change = (dot1[1] - dot2[1]) ** 2
  return round(math.sqrt(x_change + y_change), 2)

