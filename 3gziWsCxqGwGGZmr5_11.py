
def fat_prime(a, b):
  y = min(a,b)
  z = max(a,b)
  for i in range(z,y,-1):
    if is_prime(i):
      return i
  return None
  
  
def is_prime(n):
  for i in range(2,n):
    if n % i == 0:
      return False
  return True

