
def is_prime(n):
  if n >= 2:
    if n==2:
      return True
    else:
      return all(n%x !=0 for x in range (2,n))
  return False

