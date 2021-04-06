
def filter_primes(num):
  return [x for x in num if is_prime(x)]
  
def is_prime(n):
  if n < 2: return False
  for x in range(2,n//2+1):
    if n % x == 0: return False
  return True

