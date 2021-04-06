
def fib_fast(num):
  fib = [0,1]
  for x in range(num):
    fib.append(fib[-1]+fib[-2])
  return fib[num]

