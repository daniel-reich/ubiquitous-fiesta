
def points_in_circle(points, centerX, centerY, radius):
  def inside(point,x0, y0, r):
    return int((point['x']-x0)**2 + (point['y']-y0)**2 < r**2)  
  
  return sum([inside(i,centerX, centerY, radius) for i in points])

