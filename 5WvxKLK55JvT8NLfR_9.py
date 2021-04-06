
def diag_dom(arr):
  arr = [[abs(j) for j in i] for i in arr]
  for i in range(len(arr)):
    if arr[i][i]<=sum(arr[i])-arr[i][i]:
      return False
  return True

