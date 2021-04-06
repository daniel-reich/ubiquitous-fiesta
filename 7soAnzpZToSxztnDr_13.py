
def shift_left(x, y):
  return x if not y else shift_left(x*2, y-1)

