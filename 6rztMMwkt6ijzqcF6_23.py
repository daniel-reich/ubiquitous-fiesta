
def is_repeated(strn):
  count = len(strn)
  
  for i in range(len(strn)//2):
    if strn[:i+1] * count == strn:
      return count
    else: count = len(strn)//len(strn[:i+2])
  
  return False

