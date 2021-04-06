
def int_within_bounds(n, lower, upper):
  if n%1 == 0:
    if n in range(lower, upper):
      return True
    else:
      return False
  else:
    return False

