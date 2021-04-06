
def perimeter(lst):
  A, B, C = lst
  d = lambda p, q: ((q[0]-p[0])**2 + (q[1]-p[1])**2)**0.5
  return round(d(A, B) + d(B, C) + d(A, C), 2)

