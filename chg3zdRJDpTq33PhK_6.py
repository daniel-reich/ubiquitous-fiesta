
def int_within_bounds(n, lower, upper):
  while n >= lower and n < upper and isinstance(n, int):
    return True
  else:
    return False

