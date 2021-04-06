
def diag_dom(arr):
  return all(sum(abs(x) for x in row) < 2*abs(arr[i][i]) for i, row in zip(range(len(arr)), arr))

