
def on_rectangle_bounds(points):
  x_range, y_range = [x for x,y in points], [y for x,y in points]
  return all(x in (max(x_range),min(x_range)) or y in (max(y_range),min(y_range)) for x,y in points)

