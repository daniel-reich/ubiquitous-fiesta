
def bridge_shuffle(lst1, lst2):
  for i in range(len(lst2)):
      lst1.insert(2*i+1,lst2[i])
  return lst1

