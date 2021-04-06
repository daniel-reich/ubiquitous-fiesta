
from math import sqrt
def points_in_circle(points, centerX, centerY, radius):
  count = 0
  for point in points:
    if sqrt((point['x'] - centerX)**2 + (point['y'] - centerY)**2) < radius:
      count += 1
  return count

