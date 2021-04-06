
import math
def shortestDistance(txt):
  x1,y1,x2,y2 = [int(i) for i in txt.split(',')]
  dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  
  return round(dist,2)

