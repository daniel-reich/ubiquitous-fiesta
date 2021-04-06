
def shift_left(x, y):
  if y == 0:return x
  return shift_left(x*2,y-1)

