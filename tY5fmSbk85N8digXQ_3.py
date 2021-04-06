
def ones_infection(arr):
  copy = arr.copy()
  cols = []
  for r in range(len(arr)):
    for c in range(len(arr[0])):
      if copy[r][c] == 1:
        arr[r] = [1]*len(arr[r])
        cols.append(c)
  for col in cols:
    for r in range(len(arr)):
      arr[r][col] = 1
  return arr

