
def truncatable(n):
  s = str(n)
  if '0' in s: return False
  if all(is_prime(int(s[i:])) for i in range(len(s))):
    if all(is_prime(int(s[:i+1])) for i in range(len(s))):
      return 'both'
    return 'left'
  elif all(is_prime(int(s[:i+1])) for i in range(len(s))):
    return 'right'
  return False
​
def is_prime(n):
  if n<2: return False 
  elif n<4: return True
  return not [i for i in range(2, (n//2)+1) if not n%i]

