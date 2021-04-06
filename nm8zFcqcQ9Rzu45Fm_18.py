
def bridge_shuffle(lst1, lst2):
  l = [len(lst1), len(lst2)]
  res = []
  for x in range(max(l)):
    if x< len(lst1):
      res.append(lst1[x])
    if x <len(lst2):
        res.append(lst2[x])
  return res

