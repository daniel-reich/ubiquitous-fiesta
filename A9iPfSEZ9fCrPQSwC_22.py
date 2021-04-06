
def points_in_circle(points, centerX, centerY, radius):
  cnt=0
  for pt in points:
    if (pt['x']-centerX)**2+(pt['y']-centerY)**2<radius**2: cnt+=1
  return cnt

