
def shift_to_left(x, y):
  return x if y == 0 else shift_to_left(x * 2, y - 1)

