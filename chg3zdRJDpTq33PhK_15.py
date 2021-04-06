
def int_within_bounds(n, lower, upper):
  if type(n) != int:
    return False
  return lower <= n < upper

