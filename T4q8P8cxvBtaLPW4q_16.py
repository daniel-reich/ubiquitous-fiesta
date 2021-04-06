
def is_prime(num):
  if num == 1:
    return False
  for f in range( 2, int(num**0.5)+1 ):
    if num % f == 0:
      return False
  return True
​
def extract_primes(num):
  primes = []
  for f in range(2, num+1):
    if is_prime(f) and str(f) in str(num):
      for c in range( 0, str(num).count( str(f) ) ):
        primes.append(f)
  return primes

