
def ones_infection(arr):
  s = []
  for i in range(len(arr)):
    for j in range(len(arr[i])):
      if arr[i][j] == 1:
        s.append((i, j))
  for i in s:
    arr[i[0]] = [1] * len(arr[i[0]])
    for j in range(len(arr)):
      arr[j][i[1]] = 1
  return arr

