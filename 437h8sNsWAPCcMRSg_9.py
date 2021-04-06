
def primes(num):
  primes = [2]
  number = 3
  while number <= num/2:
    if not any([number%p == 0 for p in primes]):
      primes.append(number)
    number += 2
  return primes
    
def product_of_primes(num):
  prim = primes(num)
  print(prim)
  return any([p*q == num for p in prim for q in prim])

