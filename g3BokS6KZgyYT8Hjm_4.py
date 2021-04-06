
def shift_to_left(x, y):
  if y==0:
    return x
  return 2*shift_to_left(x,y-1)

