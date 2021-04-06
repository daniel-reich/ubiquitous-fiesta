
def complete_factorization(num):
  def isPrime(n):
    for f in range(2, n // 2 + 1):
      if n % f == 0:
        return False
    return True
  
  factors = []
  f = 2
  while num > 1:
    if isPrime(f):
      while num % f == 0:
        factors.append(f)
        num //= f
    f += 1
  return factors

