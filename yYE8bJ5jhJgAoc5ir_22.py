
import numpy as np
def bugger(num):
  count = 0
  while len(str(num))>1:
    num = np.product([int(x) for x in str(num)])
    count+=1
  return count

