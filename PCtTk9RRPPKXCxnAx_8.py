
def modulo(x, y):
  # Your recursive solution here.
  if (y == 0): 
    return None
  if (y < 0):  
    y = -y
  if (x < 0):
    return -modulo(-x, y)
  if (x < y):
    return x
  return modulo(x - y, y)

