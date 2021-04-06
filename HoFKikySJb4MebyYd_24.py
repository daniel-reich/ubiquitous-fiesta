
import numpy as np
​
def transform_matrix(lst):
  arr = lst[:]
  lst = np.array(arr)
  
  for i in range(len(lst)):
    for j in range(len(lst[0])):
      arr[i][j] = sum(lst[i]) + sum(lst[:,j]) - lst[i][j] * 2
  return arr

