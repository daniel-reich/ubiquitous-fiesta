
def on_rectangle_bounds(points):
  x,y=[points[i][0] for i in range(len(points))],[points[i][1] for i in range(len(points))]
  return sum([1 for i in range(len(points)) \
  if (((points[i][0]== max(x) or points[i][0]==min(x)) and (points[i][1]<=max(y) and points[i][1]>=min(y))) \
  or ((points[i][1]== max(y) or points[i][1]==min(y)) and (points[i][0]<=max(x) and points[i][0]>=min(x))))]) == len(points)

