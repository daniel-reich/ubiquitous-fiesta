
def fib(n):
  a=0
  b , c = 0 , 1
  while a<n:
    d = b + c
    b = c
    c = d
    a+= 1
  return b

