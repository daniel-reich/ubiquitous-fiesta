
from random import randint
def is_prime(num): 
  if num < 2: 
    return False
  for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 
              47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 
              107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 
              167, 173, 179, 181, 191, 193, 197, 199,]:
    if num % p == 0: 
      return False
  rrange, bbreak = 0, num-1
  while bbreak % 2 == 0:
    rrange, bbreak = rrange+1, bbreak//2
  for i in range(100):
    res = pow(randint(2, num-1), bbreak, num)
    if res == 1 or res == num-1:
      for i in range(1, rrange):
        res = res**2 % num
        if res == 1: 
          return False
        if res == num-1: 
          break
    else: return False
  return True

