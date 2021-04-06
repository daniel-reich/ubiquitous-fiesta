
def on_rectangle_bounds(points):
  x_values = list(map(lambda x: x[0],points))
  y_values = list(map(lambda x: x[1],points))
  return all(list(map(lambda x: x[0] == min(x_values) or x[0] == max(x_values) or x[1] == min(y_values) or x[1] == max(y_values),points)))

