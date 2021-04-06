
def fibo(n):
  a, b = 1, 1
  if n == 1: return a
  elif n == 2: return b
  else:
    for i in range(2, n):
      c = a + b
      a = b
      b = c
    return b

