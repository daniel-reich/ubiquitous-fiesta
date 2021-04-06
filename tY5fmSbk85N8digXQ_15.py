
def ones_infection(arr):
  i = 0
  while i < len(arr):
    j = 0
    while j < len(arr[i]):
      if arr[i][j] == 1:
        arr[i][j] = 2
      j +=1
    i += 1
  
  i = 0
  while i < len(arr):
    j = 0
    while j < len(arr[i]):
      if arr[i][j] == 2:
        for k in range(len(arr)):
          if arr[k][j] == 0:
            arr[k][j] = 1
        for l in range(len(arr[i])):
          if arr[i][l] == 0:
              arr[i][l] = 1
      j += 1
    i += 1
  
  i = 0
  while i < len(arr):
    j = 0
    while j < len(arr[i]):
      if arr[i][j] == 2:
        arr[i][j] = 1
      j += 1
    i += 1
  
  return arr

