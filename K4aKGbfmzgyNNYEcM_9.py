
def is_shape_possible(n, angles):
  w = 0
  for i in angles:
    if i > 180:
      return False
    w += i
  return w == (n-2)*180

