
def fat_prime(a, b):
  for i in range(max(a,b),min(a,b-1),-1):
    if is_prime(i):
      return i
  
def is_prime(num):
  for i in range(2,int(num**0.5)+1):
    if num%i==0:
      return False
  return True

