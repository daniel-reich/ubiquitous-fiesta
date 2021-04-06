
import numpy as np
def contains_set(lst):
  rows = list(map(lambda x: len(set(x))==1,lst))
  return all(rows)
def diagonal(lst):
  diagonals = list(map(lambda x: np.diag(lst,k = x),range(-len(lst)+1,len(lst[0])-1)))
  return contains_set(diagonals)
def is_wristband(lst):
  if contains_set(lst):
    return True
  elif contains_set(zip(*lst)):
    return True
  elif diagonal(lst):
    return True
  else:
    array = np.array(lst,str)
    array = np.rot90(array)
    return diagonal(array)

