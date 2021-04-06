
def tuck_in(lst1, lst2):
  for i in range(len(lst2)):
    lst1.insert(i+1, lst2[i])
  return lst1

