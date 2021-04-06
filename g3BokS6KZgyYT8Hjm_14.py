
def shift_to_left(x, y):
  return 2*shift_to_left(x, y-1) if y else x

