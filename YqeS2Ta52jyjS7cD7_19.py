
def is_prime(n):
  if not n or n == 1:
    return False
  i = 2
  while i < n:
    if not n % i:
      return False
    i += 1
  return True

