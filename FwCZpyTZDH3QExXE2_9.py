
def amount_fib(n):
  if n<2:
    return n
  fib = [0,1]
  while fib[-1]<n:
    fib.append(fib[-1]+fib[-2])
  return len(fib)-1

