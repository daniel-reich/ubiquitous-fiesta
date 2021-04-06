
def paths(n):
  x = n
  y = n
  while x > 1:
    x -= 1
    y *= x
  
  return y

