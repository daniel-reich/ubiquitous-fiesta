
def intersection_union(lst1, lst2):
  l2=[]
  l=sorted(list(set(lst1+lst2)))
  for i in set(lst1):
    if i in lst2:
      l2.append(i)
  return [sorted(l2),l]

