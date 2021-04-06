
import math
def points_in_circle(points, centerX, centerY, radius):
  counter = 0
  for point in points:
    if math.sqrt((centerX - point['x'])**2 + (centerY - point['y'])**2) < radius:
      counter += 1
  return counter

