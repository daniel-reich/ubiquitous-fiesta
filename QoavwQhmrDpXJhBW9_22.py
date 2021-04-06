
import numpy as np
def flip_list(lst):
  l = []
  lst = np.array(lst)
  if lst.shape == (len(lst), ):
    for i in lst:
      l.append([i])
  else:
    for i in lst:
      for y in i:
        l.append(y)
  return l

