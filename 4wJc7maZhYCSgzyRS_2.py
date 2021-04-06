
def two_product(arr, N):
  for x in range(len(arr)):
    for y in range(x):
      if arr[x]*arr[y]==N:
        return [arr[y], arr[x]]
  return None

