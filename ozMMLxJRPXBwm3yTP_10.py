
def is_factorial(n):
  p=1
  for i in range(2, n//2+1):
    p *= i
    if p == n: return True
    
  
  return False

