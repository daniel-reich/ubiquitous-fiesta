
def filter_primes(lst):
  return [i for i in lst if is_prime(i)]
  
def is_prime(n):
  if n >= 2:
    return all(n%i != 0 for i in range(2, n))
  return False

