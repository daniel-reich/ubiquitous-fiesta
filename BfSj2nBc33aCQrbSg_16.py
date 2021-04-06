
def isPrime(x):
  if x == 2: return True
  elif x < 2 or x % 2 == 0: return False
  
  for i in range(3, x // 2 + 2, 2):
    if x % i == 0: return False
  return True
​
def truncatable(n):
  n = str(n)
  if '0' in n: return False
  
  left, right = True, True
  
  for l in range(len(n)):
    if not isPrime(int(n[l:])):
      left = False
      break;
      
  for r in range(1, len(n) + 1):
    if not isPrime(int(n[:r])):
      right = False
      break;
  
  if right and left:
    return 'both'
  elif right:
    return 'right'
  elif left:
    return 'left'
  return False

