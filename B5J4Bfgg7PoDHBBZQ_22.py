
def within_triangle(p1, p2, p3, test):
  chk1 = points_on_same_side_of_line(p1, p2, p3, test)
  chk2 = points_on_same_side_of_line(p2, p3, p1, test)
  chk3 = points_on_same_side_of_line(p3, p1, p2, test)
  return chk1 and chk2 and chk3
​
def points_on_same_side_of_line(start, end, p1, p2):
  (x1, y1) = start
  (x2, y2) = end
  (x, y) = p1
  p1_check = ((x-x1)*(y2-y1))-((y-y1)*(x2-x1)) > 0
  (x, y) = p2
  p2_check = ((x-x1)*(y2-y1))-((y-y1)*(x2-x1)) > 0
  return p1_check == p2_check

