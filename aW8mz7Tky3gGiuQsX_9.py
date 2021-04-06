
def is_powerful(n):
  facs = get_factors(n)
  for fac in facs:
    if is_prime(fac) and (fac**2) not in facs:
      return False
  return True
  
  
def get_factors(n):
  res = []
  for i in range(2, n-1):
    if not n % i:
      res.append(i)
  return res
  
def is_prime(n):
  if n < 2:
      return False
  else:
      for i in range(2, int(abs(n**0.5)) + 1):
          if not n % i:
              return False
      return True

