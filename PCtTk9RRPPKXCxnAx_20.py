
def modulo(x, y):
  if abs(x)-abs(y)<0:
    return x
  elif x<0 and y>0 or x>0 and y<0:
    return modulo(x+y,y)
  return modulo(x-y, y)

