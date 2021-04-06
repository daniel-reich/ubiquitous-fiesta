
def alternate_pos_neg(lst):
  try:
    if all((lst[0]>0)==(i>0) for i in lst[::2]) and all((lst[1]>0)==(i>0) for i in lst[1::2]):
      if (lst[0]>0 and lst[1]<0) or (lst[1]>0 and lst[0]<0):
        return True
    return False
  except:
    if lst[0]==0:
      return False
    return True

