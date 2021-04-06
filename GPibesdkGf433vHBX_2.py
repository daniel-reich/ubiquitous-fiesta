
def goldbach_conjecture(n):
  for i in range(2, n):
    if is_prime(i) and is_prime(n - i):
      return [i, n - i]
  
def is_prime(n):
  return all(n % i for i in range(2, int(n ** 0.5) + 1))

