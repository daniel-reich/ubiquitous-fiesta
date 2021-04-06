
def is_icecream_sandwich(txt):
  arr = []
  for i in range(len(txt)-1):
    if txt[i] != txt[i+1]:
      arr.append(i+1)
  if len(arr) != 2: return False
  if txt[0] != txt[-1]: return False
  if arr[0] != len(txt) - arr[-1]: return False
  return True

