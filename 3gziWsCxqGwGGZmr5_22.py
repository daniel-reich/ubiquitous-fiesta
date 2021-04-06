
def fat_prime(a, b):
  for i in range(max(a,b),min(a,b),-1):
    if prime(i):
      return i
  
def prime(n):
  for i in range(2,n//2):
    if n%i==0:
      return False
  return n>1

