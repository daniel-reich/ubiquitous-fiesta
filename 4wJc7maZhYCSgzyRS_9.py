
def two_product(arr, N):
  for i in range(len(arr)):
    if N / arr[i] in arr[:i]:
      return [N // arr[i], arr[i]]

