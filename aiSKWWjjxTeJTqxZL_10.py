
import numpy as np
def complete_square(lst):
  shape = np.shape(lst)
  if shape[0]==shape[1]:
    return lst
  pad = min(shape)
  if pad == shape[0]:
    n = [0 for i in range(shape[1])]
    for i in range(shape[1]-pad):
      lst.append(n)
  else:
    for i in lst:
      for num in range(shape[0]-pad):
        i.append(0)
  return lst

