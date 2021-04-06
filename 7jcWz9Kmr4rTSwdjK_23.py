
def is_prime(n):
  for f in range( 2, int(n**0.5) + 1 ):
    if n % f == 0:
      return False
  return True
​
prime_factors = []
​
def prime_factorize(num):
  global prime_factors
  
  for f in range(2, num+1):
    if num % f == 0:     # f is a factor
      if is_prime(f):
        prime_factors.append(f)     # f is a factor and prime
        return prime_factorize( int(num / f) )
      else:
        return prime_factorize( int(num / f) )    # f is a factor but not prime
  pf = prime_factors
  prime_factors = []
  return sorted(pf)

