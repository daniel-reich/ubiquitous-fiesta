
import math
​
def get_distance(a, b):
  return round(math.sqrt((pow((b['x']-a['x']),2)) + (pow((b['y']-a['y']),2))),3)

