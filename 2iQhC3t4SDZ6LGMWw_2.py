
def on_rectangle_bounds(points):
  bounds = [f(points, key=lambda p:p[i])[i]\
                          for i in range(2) for f in (min,max)]
  return all(x in bounds[:2] or y in bounds[2:] for x,y in points)

