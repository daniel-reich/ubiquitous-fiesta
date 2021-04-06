
def points_in_circle(points, centerX, centerY, radius):
  import math
  return sum([1 for point in points if math.sqrt((centerX-point.get('x'))**2 + (centerY-point.get('y'))**2) < radius])

