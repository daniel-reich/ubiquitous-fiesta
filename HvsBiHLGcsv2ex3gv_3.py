
import math
def shortestDistance(txt):
  spltxt = txt.split(",")
  print(spltxt)
  x1 = int(spltxt[0])
  y1 = int(spltxt[1])
  
  x2 = int(spltxt[2])
  y2 = int(spltxt[3])
  
  print(round(math.sqrt((x2-x1)**2+(y2-y1)**2),2))
  
  return round(math.sqrt((x2-x1)**2+(y2-y1)**2),2)

