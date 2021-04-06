
def fibonacci_sequence():
  fib = [0, 1]
  i = fib[-2] + fib[-1]
  while i <= 255:
    fib.append(i)
    i = fib[-2] + fib[-1]
    
  return fib

