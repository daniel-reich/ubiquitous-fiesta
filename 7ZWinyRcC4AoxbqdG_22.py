
def fibo(n):
  x, y = 0, 1
  for _ in range(n):
    temp = y
    y += x
    x = temp
  return x

