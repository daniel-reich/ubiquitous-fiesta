
def filter_primes(num):
  def is_prime(n):
    i = 2
    while i*i <= n:
      if n % i == 0:
        return False
      i += 1
    return n != 1
  
  return list(filter(is_prime, num))

