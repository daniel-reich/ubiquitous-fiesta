
def findPrime(n):
  x = n-1
  while x > 1:
    if n % x == 0:
      return 0
    else:
      x -= 1
  return n
​
​
def primes_below_num(n):
  primesUnder = []
  while n > 1:
    if findPrime(n) > 0:
      primesUnder.append(n)
      n -= 1
    else:
      n -= 1
  return sorted(primesUnder)

