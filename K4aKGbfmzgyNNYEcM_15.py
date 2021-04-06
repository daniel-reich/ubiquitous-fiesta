
def is_shape_possible(n, angles):
  return sum(x for x in angles if x < 181) == (n - 2) * 180

