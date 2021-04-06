
def ones_infection(arr):
  h,w = len(arr), len(arr[0])
  for i in range(h):      
    for j in range(w):
      if arr[i][j] == 1:
        arr[i] = [1 if val == 1 else -1 for val in arr[i]]
        for ii in range(h):
          arr[ii][j] = 1 if arr[ii][j] == 1 else -1
  for i in range(h):      
    for j in range(w):
      arr[i][j] = 1 if arr[i][j] == -1 else arr[i][j]
  return arr

