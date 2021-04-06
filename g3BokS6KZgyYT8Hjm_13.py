
def shift_to_left(x, y):
  # recursive code here
  if y > 0:
    return shift_to_left(x * 2, y - 1)
  else:
    return x

