
def right_triangle(x, y, z):
  x,y,z = sorted([x,y,z])
  return x**2 + y**2 == z**2 and all(a > 0 for a in [x,y,z])

