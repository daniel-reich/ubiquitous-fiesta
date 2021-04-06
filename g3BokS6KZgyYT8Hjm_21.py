
def shift_to_left(x, y):
  return x if not y else 2 * shift_to_left(x, y - 1)

