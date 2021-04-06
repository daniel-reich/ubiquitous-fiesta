
def alternate_pos_neg(lst):
  if lst[0] == 0:
    return False
  isPos = lst[0]>0
  for i in range (1,len(lst)):
    if lst[i] == 0:
      return False
    if isPos is True and lst[i] >0:
      return False
    if isPos is False and lst[i] <0:
      return False 
    
    isPos = (lst[i]>0)
  return True

