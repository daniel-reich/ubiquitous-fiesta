
def is_prime(n):
  if n == 0 or n == 1:  return False
  for i in range(n - 1, 1, -1):
    if not n % i: 
      return False
  return True

