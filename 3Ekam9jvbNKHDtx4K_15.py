
import math
def line_length(dot1, dot2):
  x1, y1 = dot1
  x2, y2 = dot2
  dis = math.pow(x1-x2, 2) + math.pow(y1-y2, 2) 
  return round(math.sqrt(dis), 2)

