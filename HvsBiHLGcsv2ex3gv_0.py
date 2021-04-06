
import math
​
def shortestDistance(txt):
  x1, y1, x2, y2 = (int(num) for num in txt.split(','))
  return round(math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2), 2)

