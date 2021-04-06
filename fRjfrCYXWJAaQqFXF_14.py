
def isPrime(val):
  if val >= 2:
    for y in range(2, val):
      if not ( val % y ):
        return False
  else:
    return False
  return True
​
def primorial(n):
  num = 2
  primes = []
  while len(primes) < n:
    if isPrime(num):
      primes.append(num)
    num += 1
  product = 1
  for prime in primes:
    product *= prime
  return product

