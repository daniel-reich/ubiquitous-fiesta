
def alternate_pos_neg(lst):
  if 0 not in lst:
    if lst[0]>0:
      for i in range(0,len(lst),2):
        if lst[i]<0:
          return False
      for i in range(1,len(lst),2):
        if lst[i]>0:
          return False
    else:
      for i in range(0,len(lst),2):
        if lst[i]>0:
          return False
      for i in range(1,len(lst),2):
        if lst[i]<0:
          return False
  else:
    return False
  return True

