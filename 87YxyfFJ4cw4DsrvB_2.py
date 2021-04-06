
import numpy as np
def generate_rug(n):
  res = np.zeros((1,1))
  for i in range(1,(n//2)+1):
      res = np.pad(res,1,mode ='constant',constant_values =i)
  return res.tolist()

