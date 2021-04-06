
def fibonacci_sequence():
  fib = [0]
  n = 1
  while n < 255:
    fib.append(n)
    n = fib[-1] + fib[-2]
  return fib

