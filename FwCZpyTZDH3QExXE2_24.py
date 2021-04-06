
def amount_fib(n):
  if n == 0: return 0
  a, b = 0, 1
  ctr = 1
  while b < n:
    a, b = b, a + b
    ctr += 1
  return ctr

