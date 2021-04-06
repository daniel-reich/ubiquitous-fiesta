
def fib(n):
  if n == 0:
    return 0
  a = 0
  b = 1
  c = 1
  for i in range(0,n):
    a = b
    b = c
    c = a + b
  return a

