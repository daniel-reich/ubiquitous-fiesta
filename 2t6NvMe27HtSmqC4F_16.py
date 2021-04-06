
def boolean_and(lst):
  if False in lst:
    return False
  else:
    return True
​
def boolean_or(lst):
  if True in lst:
    return True
  else:
    return False
def boolean_xor(lst):
  ret=lst[0]
  for x in range(1,len(lst)):
    if lst[x]==True:
      if ret==True:
        ret=False
      else:
        ret=True
    elif lst[x]==False:
      if ret==False:
        ret=False
      else:
        ret=True
    else:
      ret=True
  return ret

