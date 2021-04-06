
import math
def shortestDistance(txt):
  n = txt.split(',')
  x1 = int(n[0])
  y1 = int(n[1])
  x2 = int(n[2])
  y2 = int(n[3])
  return round(((((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** (0.5)),2)

