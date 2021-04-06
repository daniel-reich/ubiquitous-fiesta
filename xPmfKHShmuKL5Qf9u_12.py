
def scale_tip(lst):
  arr = []
  brr = []
  isSplit = False
  
  for c in lst:
    if type(c) == str:
      isSplit=True
    elif type(c) == int:
      if isSplit:
        brr.append(c)
      else : arr.append(c)
  
  a = sum(arr)
  b = sum(brr)
​
  if a == b:
    return "balanced"
  elif a > b:
    return "left"
  else : return "right"

