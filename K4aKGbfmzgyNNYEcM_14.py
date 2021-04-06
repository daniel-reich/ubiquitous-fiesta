
def is_shape_possible(n, angles):
  return (sum(angles) == (180 - (360 / n)) * n) and all([foo < 180 for foo in angles])

