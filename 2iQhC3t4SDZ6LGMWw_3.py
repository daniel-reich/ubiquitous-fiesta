
def on_rectangle_bounds(points):
  trans_points = list(zip(*points))
  max_x, min_x = max(trans_points[0]), min(trans_points[0])
  max_y, min_y = max(trans_points[1]), min(trans_points[1])
  for i in points:
    if max_x == i[0] or min_x == i[0] or max_y == i[1] or min_y == i[1]: continue
    else: return False
  return True

