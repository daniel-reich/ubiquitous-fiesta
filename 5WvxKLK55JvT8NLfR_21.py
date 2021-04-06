
def diag_dom(arr):
  for i in range(len(arr)):
    if abs(arr[i][i]) <= sum(abs(n) for n in arr[i][:i]+arr[i][i+1:]):
      return False
  return True

