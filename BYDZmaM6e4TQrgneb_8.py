
def fib_fast(num):
  f = [0, 1]
  for i in range(2, num+1): f.append(f[-1] + f[-2])
  return f [-1]

