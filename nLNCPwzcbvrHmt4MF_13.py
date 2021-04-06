
def fibonacci_sequence():
  fib = [0,1]
  while True:
    f = fib[-1] + fib[-2]
    if f < 255:
      fib.append(f)
    else:
      return fib

