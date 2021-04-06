
def on_rectangle_bounds(points):
  x_axix = [min(x[0] for x in points), max(x[0] for x in points)]
  y_axis = [min(x[1] for x in points), max(x[1] for x in points)]
  return all(x[0] in x_axix or x[1] in y_axis for x in points)

