
def fibonacci(n):
  a , b = 1, 0
  for num in range(n):
    a, b = b, a+b
  return str(b)

