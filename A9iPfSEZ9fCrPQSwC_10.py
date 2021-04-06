
def points_in_circle(points, centerX, centerY, radius):
  return sum(1 for p in points if radius > ( ((p['x']-centerX)**2 + (p['y']-centerY)**2)**0.5 ))

