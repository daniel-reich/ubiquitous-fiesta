
import math
# Sandu Leonard on social media (code:130n4rd)
​
def number_split(n):
  if n%2 == 0:
    return [n/2, n/2]
    
  else:
    return [math.floor(n/2), math.floor(n/2) + 1]

