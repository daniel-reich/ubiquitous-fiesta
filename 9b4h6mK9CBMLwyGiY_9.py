
import math
​
def get_distance(a, b):
  return round(math.sqrt((b['x'] - a['x'])**2 + (b['y'] - a['y'])**2), 3)

