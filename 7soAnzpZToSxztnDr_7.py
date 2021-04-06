
def shift_left(x, y):
  if y==0:
    return x
  v=shift_left(x, y-1)*2
  return v

