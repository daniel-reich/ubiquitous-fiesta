
def on_rectangle_bounds(points):
  if len(points) <= 2:
    return True
  else:
    y = list(map(lambda x: x[1],points))
    x = list(map(lambda x: x[0],points))
    x1 = min(x)
    x2 = max(x)
    y1 = min(y)
    y2 = max(y)
    for point in points:
      if point[0] != x1 and point[1] != y1 and point[0] != x2 and point[1] != y2:
        return False
    return True

