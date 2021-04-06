
def modulo(x, y):
  # Your recursive solution here.
  if abs(x)<abs(y):
    return x
  else:
    return modulo(x-y, y) if x*y>0 else modulo(x+y, y)

