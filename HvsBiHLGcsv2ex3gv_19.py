
import math
def shortestDistance(txt):
  txt = txt.split(",")
  x1 = int(txt[0])
  y1 = int(txt[1])
  x2 = int(txt[2])
  y2 = int(txt[3])
  return round(math.sqrt((x1-x2)**2 + (y1-y2)**2), 2)

