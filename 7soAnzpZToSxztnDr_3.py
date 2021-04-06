
def shift_left(x, y, c=0):
  return x+shift_left(x, y, c+1) if c<2**y else 0

