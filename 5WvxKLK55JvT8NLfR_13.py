
def diag_dom(arr):
  return all(abs(arr[i][i]) > sum(abs(n) for n in arr[i])-abs(arr[i][i]) for i in range(len(arr)))

