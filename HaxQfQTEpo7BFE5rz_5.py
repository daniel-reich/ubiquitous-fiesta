
def alternate_pos_neg(lst):
  if lst[0]==0:
    return False
  flg=False
  for i in range(len(lst)-1):
    if lst[i]==0 or lst[i+1]==0:
      flg=True
    if lst[i]>0 and lst[i+1]>0 or lst[i]<0 and lst[i+1]<0:
      flg=True
  
  if flg==True:
    return False
  else:
    return True

