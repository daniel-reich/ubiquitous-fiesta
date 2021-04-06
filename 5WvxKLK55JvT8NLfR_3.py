
def diag_dom(arr):
  for i in range(len(arr)):
    if abs(arr[i][i]) <= sum([abs(arr[i][k]) for k in range(len(arr[i])) if k != i]):
      return False
  return True

