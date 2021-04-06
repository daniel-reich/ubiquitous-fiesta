
def is_prime(num):
  from math import sqrt
  if num==1: return False
  for i in range(2,int(sqrt(num))):
    if num%i==0: return False
  return True

