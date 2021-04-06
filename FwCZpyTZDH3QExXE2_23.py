
def amount_fib(n):
  a,b,c=0,1,1
  if n==0:
    return 0
  else:
    while b<n:
      a,b=b,a+b
      c+=1
    return c

