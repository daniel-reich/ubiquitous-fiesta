
def lower_triang(arr):
  return [[0 if j>i else arr[i][j] for j in range(len(arr))] for i in range(len(arr))]

