
def is_shape_possible(n, angles):
  return n > 2 and all(x <= 180 for x in angles) and (n-2) * 180 <= sum(angles)

