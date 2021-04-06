
def shift_left(x, y):
  if y == 0:
    return x
  else:
    n = shift_left(x, y + (-1))   # This is still addition!
    return n + n

