
def is_shape_possible(n, angles):
  for i in angles:
    if i > 180:
      return False
  return sum(angles) == (n-2)*180

