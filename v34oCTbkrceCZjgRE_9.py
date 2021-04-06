
def shift_to_right(x, y):
  return x if y == 0 else shift_to_right(x//2, y-1)

