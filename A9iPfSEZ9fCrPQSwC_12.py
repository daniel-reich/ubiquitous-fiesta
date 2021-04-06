
from math import sqrt
​
def points_in_circle(points, centerX, centerY, radius):
  total = 0
  for p in points:
    x, y = p.values()
    if sqrt((centerX - x)**2 + (centerY - y)**2) < float(radius):
      total += 1
  return total

