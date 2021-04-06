
def leader(arr):
  out = [arr[-1]]
  i = len(arr)-1
  while i >= 0:
    if arr[i] > out[0]:
      out = [arr[i]] + out
    i -= 1
  
  return out

