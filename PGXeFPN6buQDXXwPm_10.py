
def trace(arr):
  sum = 0
  for i in range(len(arr)):
    sum += arr[i][i]
  return sum

