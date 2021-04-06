
def shift_to_right(x, y):
  # recursive code here
  if not y:
    return x//1
  return shift_to_right(x/2,y-1)

