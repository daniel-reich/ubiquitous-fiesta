
def fib(n):
  f = 0
  g = 1
  i = 0
  while i < n:
    h = g
    g = f + g
    f = h
    i += 1
  return f

