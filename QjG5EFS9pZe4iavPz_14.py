
def fib(n):
  if n == 0:
    return 0
  if n == 1:
    return 1
  i = 1
  a = 0
  b = 1
  while i < n:
    i += 1
    c = a
    a = b
    b = b + c
  return b

