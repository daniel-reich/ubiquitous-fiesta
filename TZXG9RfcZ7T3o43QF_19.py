
def same_length(txt):
  arr = [0]
  for i in range(1,len(txt)):
    if txt[i] != txt[i-1]:
      arr.append(i)
  arr.append(len(txt))
  if len(arr)%2 == 0: return False
  for i in range(1,len(arr),2):
    if arr[i] - arr[i-1] != arr[i+1] - arr[i]:
      return False
  return True

