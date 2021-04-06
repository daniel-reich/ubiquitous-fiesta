
def simple_comp(lst1, lst2):
  counter=0
  if lst1==None or lst2==None:
    return False
  if len(lst1)!=len(lst2):
    return False
  else:
    for i in range(0,len(lst1)):
      if lst1[i]**2 in lst2:
        counter=counter+1
        lst2.remove(lst1[i]**2)
    if counter==len(lst1):
      return True
    else:
      return False

