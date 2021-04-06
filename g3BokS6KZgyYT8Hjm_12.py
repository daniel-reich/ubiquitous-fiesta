
def shift_to_left(x, y):
  if y<1: return x
  return x*2*shift_to_left(1,y-1)

