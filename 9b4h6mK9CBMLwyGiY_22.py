
import math
def get_distance(a, b):
  xDiffSquared = (b['x'] - a['x']) ** 2
  yDiffSquared = (b['y'] - a['y']) ** 2
  return round(math.sqrt(xDiffSquared + yDiffSquared), 3)

