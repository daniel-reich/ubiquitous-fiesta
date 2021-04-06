
def right_triangle(x, y, z):
  t = sorted([x, y, z])
  return t[0] ** 2 + t[1] ** 2 == t[2] ** 2 if all([ x > 0 for x in t ]) else False

