
def shift_left(x, y):
  if y > 0:
    x *= 2
    y -=1
    return shift_left(x, y)
  else:
    return x

