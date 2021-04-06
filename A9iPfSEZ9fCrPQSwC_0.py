
def points_in_circle(points, centerX, centerY, radius):
  return sum((p['x']-centerX)**2+(p['y']-centerY)**2 < radius**2 for p in points)

