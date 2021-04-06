
def lower_triang(arr):
  for i in range(len(arr)):
    for j in range(len(arr[i])):
      if j < i:
        arr[j][i] = 0
  return arr

