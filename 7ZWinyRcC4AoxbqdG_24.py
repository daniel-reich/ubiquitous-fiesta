
def fibo(n):
  a=1
  b=1
  fib = [a,b]
  for i in range(n-2):
      a,b = b,a+b
      fib.append(b)
  return fib[-1]

