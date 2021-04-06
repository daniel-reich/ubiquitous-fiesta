
def moran(n):
  if ismoran(n):
    return 'M'
  elif harshad(n):
    return 'H'
  else:
    return 'Neither'
  
def harshad(n):
  return n % sum(list([int(x) for x in str(n)])) == 0
  
def ismoran(n):
  return isprime(n // sum(list([int(x) for x in str(n)])))
  
def isprime(n):
  for i in range(2,n):
    if n % i == 0:
      return False
  return True

