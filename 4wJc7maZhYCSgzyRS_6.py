
def two_product(arr, N):
  for i in range(len(arr)):
    for j in range(i):
      if arr[i]*arr[j]==N:
        return [arr[j],arr[i]]

