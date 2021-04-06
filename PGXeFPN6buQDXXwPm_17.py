
def trace(arr):
  res = 0
  
  for i in range(len(arr)):
    res += arr[i][i]
    
  return res

