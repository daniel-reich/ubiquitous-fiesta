
import math
def line_length(dot1, dot2):
  x = math.sqrt(((dot1[0] - dot2[0])**2) + ((dot1[1] - dot2[1])**2))
  return(round(x, 2))

