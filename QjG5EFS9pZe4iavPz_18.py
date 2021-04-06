
def fib(n):
  i = 0
  x = 0
  y = 1
  z = 0
  while(i < n):
    x = y + z
    z = y
    y = x
    i += 1
  return z

