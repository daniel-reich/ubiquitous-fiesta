
def fibonacci(num):
  prev = 1
  now = 1
  fib = 1
  for i in range(1,num):
    fib = prev + now
    prev = now
    now = fib
  return fib

