
import math
def line_length(dot1, dot2):
  x = abs(dot1[0] - dot2[0])
  print(x)
  y = abs(dot1[1] - dot2[1])
  print(y)
  length = math.sqrt(x**2+y**2)
  return truncate(length, 2)
  
def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier

