
def bridge_shuffle(lst1, lst2):
  l = []
  if len(lst1) >= len(lst2):
    for i in range(len(lst2)):
      l.append(lst1[i])
      l.append(lst2[i])
    l.extend(lst1[len(lst2):])
  if len(lst2) > len(lst1):
    for i in range(len(lst1)):
      l.append(lst1[i])
      l.append(lst2[i])
    l.extend(lst2[len(lst1):])
  return l

