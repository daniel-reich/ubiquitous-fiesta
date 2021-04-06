
def int_within_bounds(n, lower, upper):
  return False if not isinstance(n, int) else lower <= n < upper

