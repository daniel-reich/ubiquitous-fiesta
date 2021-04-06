
def check(arr):
  chk = sorted(arr)
  if chk == arr:
    return 'NO'
  return 'YES' if any(arr[i:]+arr[:i] == chk for i in range(len(arr))) else 'NO'

