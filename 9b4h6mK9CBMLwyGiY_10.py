
import math
​
def get_distance(a, b):
  x1 = a["x"]
  x2 = b["x"]
  x = abs(x2 - x1)
  y1 = a["y"]
  y2 = b["y"]
  y = abs(y2 - y1)
  answer = math.sqrt(x**2 + y**2)
  return round(answer, 3)

