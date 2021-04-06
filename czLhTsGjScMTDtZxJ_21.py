
import numpy
def primorial(n):
  primes = []
  k = n*n if n>2 else 2
  for possiblePrime in range(2, n+k):
    isPrime = True
    for num in range(2, possiblePrime):
      if possiblePrime % num == 0:
        isPrime = False 
    if isPrime:
      primes.append(possiblePrime)
  return numpy.prod(primes[:n])

