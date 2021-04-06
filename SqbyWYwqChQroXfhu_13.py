
def lower_triang(arr):
  for x in range(len(arr)):
    for y in range(x+1,len(arr)):
      arr[x][y] = 0
  return arr

