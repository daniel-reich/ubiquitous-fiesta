
def tuck_in(lst1, lst2):
  lst = []
  lst.append(lst1[0])
  for i in range(0, len(lst2)):
    lst.append(lst2[i])
  lst.append(lst1[1])
  return lst

