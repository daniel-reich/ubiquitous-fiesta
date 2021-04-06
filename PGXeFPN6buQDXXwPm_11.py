
def trace(arr):
  dim = len(arr)
  f = 0
  for d in range(dim):
    f = arr[d][d] +f
  return f

