
def modulo(x, y):
​
  if x < 0:
    if abs(x) < abs(y):
      return x
    elif y < 0:
      return modulo(x-y,y)
    else:
      return modulo(x+y,y)
  if x < abs(y):
    return x
  
  if y < 0:
  # print(x,y)
    return modulo(x+y,y)
  else:
    return modulo(x-y,y)

