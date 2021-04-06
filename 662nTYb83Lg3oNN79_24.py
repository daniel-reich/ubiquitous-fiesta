
def is_parallelogram(lst):
  A, B, C, D = lst
  p1 = slope(A,B) == slope(C,D)
  p2 = slope(A,C) == slope(B,D)
  p3 = slope(A,D) == slope(B, C)
  return p1 + p2 + p3 == 2
​
def slope(a, b):
  rise = b[1] - a[1]
  run = b[0] - a[0]
  return rise/run if run else rise

