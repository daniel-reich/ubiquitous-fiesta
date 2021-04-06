
def is_shape_possible(n, angles):
  return n > 2 and sum(angles) == (n - 2) * 180 and max(angles) <= 180

