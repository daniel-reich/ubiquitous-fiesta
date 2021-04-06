
def amount_fib(n):
  a, b, c = 0, 1, 0
  while a<n:
    a,b = b,a+b
    c+=1
  return c

