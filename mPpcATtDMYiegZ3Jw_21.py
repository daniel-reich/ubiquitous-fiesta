
def right_triangle(x, y, z):
  x, y, d = tuple(sorted([x,y,z]))
  return d == (x**2 + y**2)**(1/2) if x > 0 and y > 0 and d > 0 else False

