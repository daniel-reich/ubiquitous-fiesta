
def shift_left(x, y):
  # your recursive solution here
  if y==0:
    return x
  return 2*shift_left(x, y-1)

