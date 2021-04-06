
def shift_to_right(x, y):
  # recursive code here
  if y==0:
    return x
  else:
    return shift_to_right(x, y-1)//2

