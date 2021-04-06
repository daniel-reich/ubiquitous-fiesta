
def prime_factorization(number):
  a = []
  from math import sqrt; from itertools import count, islice
  def isPrime(n):
      return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))
  for x in range(number):
    if isPrime(x): 
      while number%x==0:
        a.append(x)
        number  = number/x
  return a

