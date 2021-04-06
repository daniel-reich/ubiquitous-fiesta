
def fibonacci(num):
  a, b = 1, 1
  for i in range(1, num):
    a, b = b, a+b
  return b

