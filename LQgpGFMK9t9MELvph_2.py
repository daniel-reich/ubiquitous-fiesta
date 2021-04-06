
import numpy as np
def get_diagonals(lst):
  if not lst: 
    return [[],[]]
  
  lst = np.array(lst)
  a = list(lst.diagonal()) #Converted back to list due to numpy bug
  b = list(np.flipud(lst).diagonal()[::-1])
  
  return [a,b]

