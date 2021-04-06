
def sle(m):
  (a, b, x), (c, d, y) = tuple(m[0]), tuple(m[1])
  det = a*d - b*c
  if det == 0: return False
  return ((d*x - b*y)/det, (a*y - c*x)/det)

