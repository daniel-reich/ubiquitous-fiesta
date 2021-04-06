
def fibo(n):
  a, b = 0, 1
  counter = 0
  while counter < n:
    counter += 1
    a, b = b, a + b
  return a

