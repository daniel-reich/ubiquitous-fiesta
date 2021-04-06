
def int_within_bounds(n, lower, upper):
  if type(n) == int:
    if n >= lower and n < upper:
      return True
    else:
      return False
  else:
    return False

