
def trace(arr):
  n = 0
  total = 0
  for x in arr:
    total = total + arr[n][n]
    n += 1
  return total

