
def shift_to_left(x, y):
  if y == 0:
    return x
  if y == 1:
    return x * 2
  return 2 * (shift_to_left(x, y-1))

