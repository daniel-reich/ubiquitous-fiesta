
def modulo(x, y):
  if x < 0:
    if y < 0:
      return modulo(x-y,y) if x-y <= 0 else x
    if y > 0:
      return modulo(x+y, y) if x+y <= 0 else x
  elif y < 0:
    y *= -1
  return modulo(x-y, y) if x-y >= 0 else x

