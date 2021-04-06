
def modulo(x, y):
  if x % y == 0:
    return 0
  if x < 0:
    return -1 + modulo(x+1,y)
  return 1 + modulo(x-1,y)

