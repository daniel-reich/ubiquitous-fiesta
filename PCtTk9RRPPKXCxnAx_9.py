
def modulo(x,y):
  if abs(x)<abs(y): return x
  return modulo(x+y,y) if x*y<0 else modulo(x-y,y)

