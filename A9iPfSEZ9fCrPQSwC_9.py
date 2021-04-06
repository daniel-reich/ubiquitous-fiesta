
def points_in_circle(points, centerX, centerY, radius):
  return [((centerX - i['x']) * (centerX - i['x']) + (centerY - i['y']) * (centerY - i['y'])) < radius ** 2 for i in points].count(True)

