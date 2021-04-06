
def lower_triang(arr):
  n = len(arr)
  for i in range(n):
    for j in range(i+1,n):
      arr[i][j] = 0
  return arr

