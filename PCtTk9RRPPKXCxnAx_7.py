
def modulo(x, y):
  y = abs(y)
  return x if abs(x)<y else modulo(x-y, y) if x>0 else modulo(x+y, y)

