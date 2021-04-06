
def shift_to_right(x, y):
  if y == 0:
    return x
  return shift_to_right(x//2, y-1)

