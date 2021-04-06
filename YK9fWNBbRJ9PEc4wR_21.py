
def tuck_in(lst1, lst2):
  n=[]
  n.append(lst1[0])
  for a in range(0,len(lst2)):
    n.append(lst2[a])
  n.append(lst1[1])
  return n

