
def ones_infection(arr):
  for row in arr:
    if 1 in row:
      for j in range(len(row)):
        if row[j] == 1:
          row[j] = -1
        else:
          row[j] = 1
          
  for j in range(len(arr[0])):
    for i in range(len(arr)):
      if arr[i][j] == -1:
        for k in range(len(arr)):
          arr[k][j] = 1
        break
        
  return arr

