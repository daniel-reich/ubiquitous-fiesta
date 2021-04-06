
def trace(arr):
  n = len(arr)
  result = 0
  for x in range(n):
    result = result + arr[x][x]
  return result

