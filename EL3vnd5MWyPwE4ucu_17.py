
def fibonacci(n):
  a = 0
  b = 1
  if n <= 0:
    return str(a)
  elif n == 1:
    return str(b)
  else:
    for i in range(1, n):
      c = a + b
      a = b
      b = c
    return str(b)

