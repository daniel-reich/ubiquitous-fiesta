
import math
def line_length(dot1, dot2):
  x1,y1 = dot1
  x2,y2 = dot2
  return round(math.sqrt((x2-x1)**2+(y2-y1)**2),2)

