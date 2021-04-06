
def prime_factorization(number):
  primes = [2,3]
  arr = []
  for i in range(4,number-1):
    if is_prime(i):
      primes.append(i)
  while number > 1:
    for x in primes:
      if number % x == 0:
        number /= x
        arr.append(x)
  return sorted(arr)
    
def is_prime(num):
  if num > 1:
    for i in range(2,num):
      if num % i == 0:
        return False
    return True
  else : return True

