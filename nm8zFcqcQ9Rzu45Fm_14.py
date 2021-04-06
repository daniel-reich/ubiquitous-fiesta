
def bridge_shuffle(lst1, lst2):
  l = []
  for i in range(min(len(lst1), len(lst2))):
    l.append(lst1[i])
    l.append(lst2[i])
  l = l + lst1[min(len(lst1), len(lst2)):] + lst2[min(len(lst1), len(lst2)):]
  
  return l

