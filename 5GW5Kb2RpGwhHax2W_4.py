
import numpy as np
def spiral_transposition(lst):
  a = len(lst)*len(lst[0])
  lst = np.array(lst)
  empty_list = []
  while lst.any():
    l = lst.transpose()
    length = len(lst)
    x = lst[0].tolist() + l[-1][1:length - 1].tolist() + lst[-1][::-1].tolist() + l[0][1:length - 1][::-1].tolist()
    empty_list += x
    lst = lst[1:-1, 1:-1] 
  
  return empty_list[:a]

