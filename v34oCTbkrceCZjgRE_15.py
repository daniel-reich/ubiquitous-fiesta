
def shift_to_right(x, y):
  return x if y == 0 else shift_to_right(x, y-1)//2

