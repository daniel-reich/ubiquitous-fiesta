
def is_powerful(n):
  is_prime = lambda x: all(x % i for i in range(2, x-1))
  factors = [x**2 for x in range(2, n-1) if not n % x and is_prime(x)]
  return all(not n % i for i in factors)

