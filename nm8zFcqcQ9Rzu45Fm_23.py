
def bridge_shuffle(lst1, lst2):
  finallist = []
  for i in range(0,min(len(lst1),len(lst2))):
    finallist.append(lst1[i])
    finallist.append(lst2[i])
  for i in range(min(len(lst1),len(lst2)),max(len(lst1),len(lst2))):
    if len(lst1)>len(lst2):
      finallist.append(lst1[i])
    else:
      finallist.append(lst2[i])
  return finallist

