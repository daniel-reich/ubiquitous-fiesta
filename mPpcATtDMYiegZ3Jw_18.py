
def right_triangle(x, y, z):
  sides = [x, y, z]
  sides.sort()
  if sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2:
    if sides[0] > 0:
      return True
  return False

