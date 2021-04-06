
def shift_to_right(x, y,m=2):
  return x if y==0 else x//m if y==1 else shift_to_right(x, y-1,m*2)

