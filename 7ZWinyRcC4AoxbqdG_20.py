
def fibo(n):
  a, b = 1, 0
  for i in range(n + 1):
    a, b = b, a + b
  return a

