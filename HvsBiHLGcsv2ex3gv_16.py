
import math
def shortestDistance(txt):
  x1, y1, x2, y2 = list(map(int,txt.split(',')))
  
  return round(((x2-x1)**2 + abs(y2-y1)**2)**0.5, 2)

