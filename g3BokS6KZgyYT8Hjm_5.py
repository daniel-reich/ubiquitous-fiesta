
def shift_to_left(x, y,t=1):
  
  if y==0:
    return x*t
  else:
    return shift_to_left(x,y-1,t*2)

