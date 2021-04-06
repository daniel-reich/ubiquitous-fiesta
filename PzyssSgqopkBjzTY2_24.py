
import math
def can_exit(arr):
  rows=len(arr)
  col=len(arr[0])
  for j in range(1,col):
    arr[0][j]+=arr[0][j-1]
  for i in range(1,rows):
    arr[i][0]+=arr[i-1][0]
  
  for i in range(1,rows):
    for j in range(1,col):
      arr[i][j]+=min(arr[i-1][j],arr[i][j-1])
  
  return not arr[rows-1][col-1]

