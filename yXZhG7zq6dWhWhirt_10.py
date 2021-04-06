
def filter_primes(num):
  return list(filter(is_prime, num))
  
def is_prime(num):
  for i in range(2, num):
    if num%i == 0: return False
  return True if num!=1 else False

