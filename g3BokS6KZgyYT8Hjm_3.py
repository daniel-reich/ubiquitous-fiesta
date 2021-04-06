
def shift_to_left(x, y):
  if y==0:
    return x
  else:
    return 2*shift_to_left(x, y-1)

