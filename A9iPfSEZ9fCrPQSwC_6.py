
def points_in_circle(points, centerX, centerY, radius):
  in_circle = lambda p: sum((x-y)**2 for x,y in zip(p,[centerX,centerY]))**0.5 < radius
  return sum(in_circle(list(x.values())) for x in points)

