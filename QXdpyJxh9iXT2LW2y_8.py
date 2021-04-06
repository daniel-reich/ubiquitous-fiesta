
def isPrime(n):
  if n == 1:
    return False
  elif n == 2:
    return True   
  for f in range(2, int(n**0.5)+2 ):
    if n % f == 0:
      return False
  return True
  
def is_semiprime(n):
  if isPrime(n):
    return False
    
  factors = []
  for f in range( 2, int(n**0.5) + 1 ):
    if n % f == 0:
      factors.append(f)
      factors.append(int(n/f))
  for f in factors:
    if isPrime(f) == False:   # have a non-prime factor
      return False
  return True
      
​
def semiprimes(n):
  list1 = []
  list2 = []
  for f in range(4, n):
    if is_semiprime(f):
      list1.append(f)
      if (f**0.5) % 1 > 0:    # not a perfect square
        list2.append(f)
  return list1, list2

