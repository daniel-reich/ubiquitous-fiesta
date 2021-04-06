
import math
def shortestDistance(txt):
  x1, y1, x2, y2 = list(map(float, txt.split(',')))
  return round(((x1 - x2)**2 + (y1 - y2)**2)**.5, 2)

