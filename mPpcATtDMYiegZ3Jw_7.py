
def right_triangle(x, y, z):
  a, b, c = sorted([x, y, z])
  return a**2 + b**2 == c**2 if a*b*c > 0 else False

