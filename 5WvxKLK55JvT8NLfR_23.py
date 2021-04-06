
def diag_dom(arr):
  for i in range(len(arr)):
    s=d=0
    for j in range(len(arr[i])):
      if i==j:
        d=abs(arr[i][j])
      else:
        s+=abs(arr[i][j])
    if d<=s:
      return False
  return True

