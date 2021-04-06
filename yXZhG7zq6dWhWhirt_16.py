
def filter_primes(num):
​
  def isPrime(n):
    if not isinstance(n, int) or n < 2:
      return False
    for x in range(2,n):
      if n % x == 0:
        return False
    return True
    
  return [n for n in num if isPrime(n)]

