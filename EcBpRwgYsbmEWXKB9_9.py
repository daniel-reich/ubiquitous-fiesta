
import math
def prime(x):
  if x <= 1: return False
  if x <= 3: return True
  if x%2 == 0 or x%3 == 0: return False
  
  for i in range(5, int(math.sqrt(x)) + 1, 6): 
    if x % i == 0: return False
  return True

