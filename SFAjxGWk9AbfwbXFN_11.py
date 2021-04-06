
def primes_below_num(n):
  return [x for x in range(1, n+1) if x== 2 or 2**(x-1) % x == 1 ]

