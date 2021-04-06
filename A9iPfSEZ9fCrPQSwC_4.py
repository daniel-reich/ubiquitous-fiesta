
def points_in_circle(points, centerX, centerY, radius):
  return sum([1 for p in points if radius ** 2 > (dict(p)['x'] - centerX) ** 2  + (dict(p)['y'] - centerY) ** 2])

