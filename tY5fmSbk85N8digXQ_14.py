
def ones_infection(arr):
  temp = [0] * len(arr)
  for i in range(len(temp)):
    temp[i] = [0] * len(arr[0])
  for i in range(len(arr)):
    for x in range(len(arr[i])):
      if 1 in arr[i] or 1 in [a[x] for a in arr]:
        temp[i][x] = 1
  for i in range(len(arr)):
    for x in range(len(arr[i])):
      if temp[i][x] == 1:
        arr[i][x] = 1
  return arr

