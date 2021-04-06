
import math
def is_exact(n, x=0, y=1):
  if x >= n:
    return [n, y-1] if math.factorial(y-1) == n else "Not exact!"
  else : 
    return is_exact(n,math.factorial(y), y+1)

