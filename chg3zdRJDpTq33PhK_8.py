
def int_within_bounds(n, lower, upper):
  if isinstance(n, int):
    return n in range(lower, upper)
  else:
    return False

