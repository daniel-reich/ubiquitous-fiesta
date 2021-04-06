
def fibo(n):
  x, y = 1, 0
  for j in range(n):
    x, y = x + y, x
  return y

