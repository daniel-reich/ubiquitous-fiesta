
def fibo(n):
  a = 1
  b = 1
  c = 1
  while n > 2:
    a = b
    b = c
    c = a+b
    n -= 1
  
  return c

