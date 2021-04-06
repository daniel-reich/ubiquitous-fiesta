
def fibonacci(n):
  fib = [0,1]
  while len(fib)<=n:
    fib.append(fib[-2]+fib[-1])
  return str(fib[n])

