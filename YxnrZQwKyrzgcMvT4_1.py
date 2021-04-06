
def rotate_transform(arr, num):
  k = (-num)%4
  for _ in range(k):
    rot(arr)
  return arr
​
def rot(arr):
  for i in range(len(arr)):
    for j in range(i):
      arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
  arr.reverse()

