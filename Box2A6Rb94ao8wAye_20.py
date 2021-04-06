
def leader(arr):
  ans = []
  arr = arr[arr.index(max(arr)):]
  for j in range(len(arr)):
    k = max(arr[j:])
    if k not in ans:
      ans.append(k)
  return ans

