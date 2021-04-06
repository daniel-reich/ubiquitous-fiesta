
def consecutive_combo(lst1, lst2):
  lst=lst1+lst2
  lst = sorted(lst)
  for i in range(0,len(lst)-1):
    if lst[i+1]-lst[i]!=1:
      return False
  else:
    return True

