
def right_triangle(x, y, z):
  if x <= 0 or y <= 0 or z <= 0:
    return False
  X, Y, Z = x ** 2, y ** 2, z ** 2
  return ((X + Y == Z) or (X + Z == Y) or (Y + Z == X))

