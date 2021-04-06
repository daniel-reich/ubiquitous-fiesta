
import numpy as np
​
def is_prime(x):
  for i in range(2,x):
    if (x % i) ==0:
      return False
      break
            
  else:
    return True
        
​
def primorial(x):
  l = [2]
  y = 3
  a = 1
    
  while len(l) < x:
    if is_prime(y):
      l.append(y)
    y+=1
        
    
    
  return np.prod(l)

