
import math
def shortestDistance(txt):
  points = [int(item.strip()) for item in txt.split(',')]
  return round(math.sqrt((points[2] - points[0]) ** 2 + (points[3] - points[1]) ** 2), 2)

