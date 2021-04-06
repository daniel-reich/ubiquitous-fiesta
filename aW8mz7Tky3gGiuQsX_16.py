
def is_powerful(n):
  factors = [i for i in range(1, (n//2)+1) if is_prime(i) and not n%i]
  return all(not n%(i**2) for i in factors)
​
def is_prime(n):
  if n<2: return False
  elif n<4: return True
  return not [i for i in range(2,n) if not n%i]

