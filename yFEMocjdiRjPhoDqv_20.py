
def prime(n):
  if n<=1:
    return False
  if n==2:
    return True
  
  for i in range(2,n):
    if n%i==0:
      return False
  return True
​
def prime_in_range(n1, n2):
  for i in range(n1,n2+1):
    if prime(i):
      return True
  
  return False

