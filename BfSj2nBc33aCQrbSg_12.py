
def truncatable(n):
  strn = str(n)
  if not isprime(n) or any(i == '0' for i in strn):
    return False
  right = True
  left = True
  for i in range(1,len(strn)):
    right = right and isprime(int(strn[:-i]))
    left = left and isprime(int(strn[i:]))
  if right and left:
    return 'both'
  if right:
    return 'right'
  if left:
    return 'left'
  return False
  
def isprime(n):
  if n in [1,4]:
    return False
  for i in range(2,n//2):
    if n % i == 0:
      return False
  return True

