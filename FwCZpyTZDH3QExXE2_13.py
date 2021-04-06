
def amount_fib(n):
  if n<2:
    return n
  else:
    a,b=0,1
    c=1
    while b<n:
      a,b=b,a+b
      c+=1
    return c

