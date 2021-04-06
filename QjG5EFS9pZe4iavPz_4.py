
def fib(n):
  a, b = 0, 1
  while n > 0:
    a, b = a+b, a
    n -= 1
  return a

