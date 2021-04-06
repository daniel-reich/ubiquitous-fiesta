
def right_triangle(x, y, z):
  if any(i < 1 for i in (x, y, z)):
    return False
  a, b, h = sorted((x, y, z))
  return a**2 + b**2 == h**2

