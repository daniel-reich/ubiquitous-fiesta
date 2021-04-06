
import numpy as np
def block(lst):
  np_array = np.array(lst)
  a, b = np.where(np_array == 2)
  return (len(lst)-1)*len(a)-sum(a)

