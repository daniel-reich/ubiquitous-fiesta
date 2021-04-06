
def fib_fast(n):
  a,b=0,1
  for i in range(1,n):
    c=a+b
    a,b=b,c
  return b

