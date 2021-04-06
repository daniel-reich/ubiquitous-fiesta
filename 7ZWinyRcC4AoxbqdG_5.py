
def fibo(n):
  fib = {1: 1, 2: 1, 3: 2}
  for i in range(3,n+1):
    fib[i] = fib[i-1] + fib[i-2]
  return fib[n]

