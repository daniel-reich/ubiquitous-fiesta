
def primes_below_num(n):
  return [y for y in range(2,n+1) if all(y % x != 0 for x in range(2,y))]

