
def right_triangle(x, y, z):
  x, y, z = sorted([x,y,z])
  return all(i > 0 for i in [x,y,z]) and x**2 + y**2 == z**2

