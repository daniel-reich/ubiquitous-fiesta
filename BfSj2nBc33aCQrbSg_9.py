
def isPrime(x):
  if x <= 1:
    return False
  for n in range(2, x):
    if x%n == 0:
      return False
  return True
​
def truncatable(x):
  strx = str(x)
  left = True
  right = True
  
  for a in range(0, len(strx)):
    if strx[a] == '0':
      return False
      
  if not isPrime(x):
    return False
    
  for a in range(1, len(strx)):
    if left:
      if not isPrime(int(strx[a:])):
        left = False
    if right:
      if not isPrime(int(strx[:a])):
        right = False
        
  if left and right:
    return "both"
  elif left:
    return "left"
  elif right:
    return "right"
  return False

