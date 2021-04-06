
def goldbach_conjecture(n):
  for i in range(2, n):
    if is_prime(i) and is_prime(n-i):
      return [i, n-i]
  return []
  
def is_prime(n):
  for i in range(2, n):
    if n % i == 0:
      return False
  return True

