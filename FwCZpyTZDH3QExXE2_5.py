
def amount_fib(n):
  if n < 2:
    return n
  f = [1,1]
  while f[-1] < n:
    f.append(f[-1] + f[-2])
  return len(f)

