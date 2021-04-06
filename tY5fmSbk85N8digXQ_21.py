
def ones_infection(arr): 
  row = [i for i in range(len(arr)) if 1 in arr[i]]
  col = [j for j in range(len(arr[0])) if any(i[j]==1 for i in arr)]
  for i in range(len(arr)):
    for j in range(len(arr[0])):
      if i in row or j in col:
        arr[i][j]=1
  return arr

