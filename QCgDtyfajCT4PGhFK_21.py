
from math import sqrt
def addprime(primes):
  if primes==[]:
    return [2]
  if primes==[2]:
    return [2,3]
  number=primes[-1]+2
  while True:
    if not any([ True for x in primes if number%x==0]):
      primes.append(number)
      break
    number+=2
  return primes
  
def prime_factorization(number):
  if number==1:
    return []
  result=[]
  primes=[2]
  while primes[-1] <=sqrt(number):
    print(number)
    if number%primes[-1]==0:
      result.append(primes[-1])
      number=number//primes[-1]
      continue
    else:
      primes=addprime(primes)
  result.append(number)
  return result

