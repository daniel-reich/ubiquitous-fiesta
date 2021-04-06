
def points_in_circle(points, centerX, centerY, radius):
  num = 0
  for i in range(len(points)):
    a, b = points[i].values()
    if (a - centerX)**2 + (b - centerY)**2 < radius**2:
      num += 1
  return num

