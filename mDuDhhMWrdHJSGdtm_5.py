
import math
def is_exactly_three(n):
  root = math.sqrt(n);
  tOrF = False;
  if root-math.floor(root)==0:
    if root > 1:   
      for i in range(2, int(root)):
        if (root % i) == 0:
          tOrF = False;
          break;
      else: 
        tOrF = True;
    else: 
      tOrF = False;
  else:
    tOrF = False;
​
  return tOrF;

