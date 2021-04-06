
def tuck_in(lst1, lst2):
  lst3=[]
  lst3.append(lst1[0])
  for i in lst2:
    lst3.append(i)
  lst3.append(lst1[1])
  return lst3

