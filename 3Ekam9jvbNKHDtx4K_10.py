
import math
def line_length(dot1, dot2):
  a = dot1[0] - dot2[0]
  b = dot1[1] - dot2[1] 
  c = math.sqrt((a**2) + (b**2))
  return round(c, 2)

