
def fib(n,d={0:0,1:1}):
  if n not in d:d[n]=fib(n-1,d)+fib(n-2,d)
  return d[n]

