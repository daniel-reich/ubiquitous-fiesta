
def primes_below_num(n):
  primes = []
  
  for x in range(2, n + 1):
    factors = []
    for y in range(1, x + 1):
      if x % y == 0:
        factors.append(y)
    if len(factors) == 2:
      primes.append(x)
  return primes

