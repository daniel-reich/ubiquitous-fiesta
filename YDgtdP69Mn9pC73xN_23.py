
import numpy as np
def num_grid(lst):
  arr = np.array(lst)
  for i in range(len(arr)):
    for j in range(len(arr[0])):
      arr[i,j] = countmine(i,j,arr)
  return list(list(i) for i in arr)
  
def countmine(col, row, arr):
  if arr[col,row] == '#':
    return '#'
  mini_arr = arr[max(0,col-1):col+2,max(0,row-1):row+2]
  n = (mini_arr == '#').sum()
  return n

