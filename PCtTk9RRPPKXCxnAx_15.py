
def modulo(x, y):
  if abs(x) < abs(y):
    return x
  return modulo(x // abs(x) * (abs(x)- abs(y)), y)

