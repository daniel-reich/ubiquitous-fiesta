
def fibonacci(n):
  a = 0
  b = 1
  i = 1
  while i < n:
    c = a + b
    a, b = b, c
    i +=1
  return str(c)

