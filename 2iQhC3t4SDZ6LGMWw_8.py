
def on_rectangle_bounds(points):
  dim = 2
  left_up    = [0] * dim
  right_down = [0] * dim
  points_in   = [True] * dim
  points_on   = [True] * dim
  
  for xy in range(dim):
    left_up[xy]    = min(point[xy] for point in points)
    right_down[xy] = max(point[xy] for point in points)
    points_in[xy]   = all(left_up[xy] <= point[xy] 
                     <= right_down[xy] for point in points)
  
  point_on = lambda point: any((point[xy] == left_up[xy])
                           or (point[xy] == right_down[xy])
                           for xy in range(dim))
                           
  points_on = all(point_on(point) for point in points)
  
  return ((points_in == [True, True]) and points_on)

