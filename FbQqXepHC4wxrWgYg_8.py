
def prime_divisors(num):
  def divisors(num):
    factors = []
    for n in range(1, num//2 + 1):
      if num % n == 0:
        factors.append(n)
        factors.append(num//n)
    return factors
  def is_prime(num):
    if num <= 1:
      return False
    for n in range(2, num):
      if num % n == 0:
        return False
    return True
  
  return sorted([n for n in list(set(divisors(num))) if is_prime(n) == True])

