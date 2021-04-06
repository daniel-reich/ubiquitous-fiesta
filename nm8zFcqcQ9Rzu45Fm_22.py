
def bridge_shuffle(lst1, lst2):
  if len(lst2)==1:
    lst1.insert(1,lst2[0])
    return lst1
  for i in range(1,len(lst2)*2,2):
    lst1.insert(i,lst2[0])
    lst2.pop(0)
  if len(lst1)<len(lst2):
    lst1.append(lst2[-1])
  return lst1

