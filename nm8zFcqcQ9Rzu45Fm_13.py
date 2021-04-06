
def bridge_shuffle(lst1, lst2):
  length = max(len(lst1),len(lst2))
  res = []
  for i in range(length):
    if i<len(lst1): res.append(lst1[i])
    if i<len(lst2): res.append(lst2[i])
  return res

