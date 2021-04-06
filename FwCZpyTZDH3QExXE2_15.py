
def amount_fib(n):
  if n <= 0:
    return 0
  res = [0,1]
  while res[-1] < n:
    res.append(res[-1]+res[-2])
  return len(res)-1

