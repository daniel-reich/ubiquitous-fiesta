
def fibonacciSequence():
  fib = [0,1]
  while fib[-1] < 255:
    fib.append(fib[-2] + fib[-1])
  # the first fib number bigger then 255 always added, so remove it 
  return fib[:-1]

