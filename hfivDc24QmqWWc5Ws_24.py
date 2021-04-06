
def is_prime(n):
  if n >= 2:
    for y in range(2, n):
      if not (n % y):
        return False
  else:
    return False
  return True
def filter_primes(num):
  return list(filter(is_prime, num))
def eratosthenes(num):
  
  return filter_primes(list(range(num)))

