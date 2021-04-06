
def right_triangle(*args):
  a = sorted(list(args))
  if a[0] <= 0:
    return False
  else:
    return a[2] ** 2 == ((a[0] ** 2) + (a[1] ** 2))

