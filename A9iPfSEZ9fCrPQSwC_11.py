
import math
def points_in_circle(points, centerX, centerY, radius):
  count = 0
  for pt in points:
    dist = math.sqrt((pt['x'] - centerX)**2 + (pt['y'] - centerY)**2)
    if dist < radius: count += 1
  return count

