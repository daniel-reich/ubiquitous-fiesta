
def filter_primes(num):
  def is_prime(n):
    if n < 2:
      return False
    for i in range(2, n):
      if n % i == 0:
        return False
    return True
  
  prime_only = []
  for number in num:
    if is_prime(number) == True:
      prime_only.append(number)
  return prime_only

