
def lower_triang(arr):
  for row in range(0, len(arr) , 1):
    for col in range((row + 1), len(arr[row]), 1):
      arr[row][col] = 0
  return arr

