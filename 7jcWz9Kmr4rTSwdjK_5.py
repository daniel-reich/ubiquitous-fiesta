
import math
def prime_factorize(num):
  primeFactors = []
  for i in range(2, int(math.sqrt(num)) + 1):
    if num % i == 0:
      primeFactors.append(i)
      primeFactors.extend(prime_factorize(int(num / i)))
      break
  if primeFactors == []:
    if num != 1:
      primeFactors.append(num)
  sortedPrimeFactors = sorted(primeFactors)
  return sortedPrimeFactors

