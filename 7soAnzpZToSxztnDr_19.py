
def shift_left(x, y):
  return x if y == 0 else shift_left(x + x, y - 1)

