
def shift_to_left(x, y):
  if y == 0:
    return x
  x = 2 * x
  return x if y == 1 else shift_to_left(x, y - 1)

