
def fibonacci(n):
  a = 0
  b = 1
​
  for _ in range(n + 1):
    a, b = a + b, a
​
  return str(b if n > 1 else 0)

