
def shift_left(x, y):
  return shift_left(x, y-1)+shift_left(x, y-1) if y else x

