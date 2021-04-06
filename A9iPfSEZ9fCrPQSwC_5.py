
def points_in_circle(points, centerX, centerY, radius):
  return sum(1 for x in points if ((x['x'] - centerX)**2 + (x['y'] - centerY)**2)**(1/2) < radius)

