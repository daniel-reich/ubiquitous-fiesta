
def int_within_bounds(n, lower, upper):
  return False if not isinstance(n, int) else n >= lower and n < upper

