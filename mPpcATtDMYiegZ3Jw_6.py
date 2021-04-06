
def right_triangle(x, y, z):
  a, b, c = sorted([x, y, z])
  if a <= 0:
    return False
  return a**2 + b**2 == c**2

