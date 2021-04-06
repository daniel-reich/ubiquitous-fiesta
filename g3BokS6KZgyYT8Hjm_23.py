
def shift_to_left(x, y):
  # recursive code here
  return x if not y else 2*shift_to_left(x,y-1)

