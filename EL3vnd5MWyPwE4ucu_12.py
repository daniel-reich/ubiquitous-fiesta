
fib=[0,1]
def fibonacci(n):
  global fib
  while len(fib)<201:
    fib+=[fib[-2]+fib[-1]]
  return str(fib[n])

