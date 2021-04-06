
import numpy as np
def is_odd(npa):
  for i in range(npa.shape[0]):
    for j in range(npa.shape[1]):
      if npa[i,j]%2==0:
        return False
  return True
def odd_square_patch(l2d):
  np2d=np.array(l2d)
  r,c=np2d.shape
  ret=0
  for i in range(r):
    for j in range(c):
      for k in range(1,min(r-i,c-j)+1):
        if k>ret and is_odd(np2d[i:i+k,j:j+k]):
          ret=k
  return ret

