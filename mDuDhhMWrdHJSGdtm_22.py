
import math
def is_prime(n):
  ret=True if n>1 else False
  for i in range(2,math.floor(math.sqrt(n))+1):
    if n%i==0:
      ret=False
      break
  return ret
def is_exactly_three(n):
  a=math.sqrt(n)
  b=math.floor(a)
  return n!=1 and a==b and is_prime(b)

