
def is_prime(n):
  if n == 0 or n == 1: return False
  
  for i in range(2, n):
    if not bool(n % i): return False
    
  return True

