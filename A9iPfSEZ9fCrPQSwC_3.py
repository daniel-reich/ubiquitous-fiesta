
def points_in_circle(points, centerX, centerY, radius):
  return sum([(a['x']-centerX)**2+(a['y']-centerY)**2<radius**2 for a in points])

