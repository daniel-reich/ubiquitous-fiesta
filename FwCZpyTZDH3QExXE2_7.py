
def amount_fib(n):
  fib = {0: 0, 1: 1}
  count = 2
  if n == 0:
    return 0
  if n == 1:
    return 1
  for i in range(2,n+1):
    fib[i] = fib[i-1] + fib[i-2]
    if fib[i] < n:
      count += 1
    else:
      return count
  return count

