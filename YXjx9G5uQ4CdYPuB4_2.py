
def simple_comp(lst1, lst2):
  if lst1==[]:
    return lst2==[]
  if lst1==None:
    return False
  a = sorted([abs(i) for i in lst1])
  b = sorted(lst2)
  for i in range(len(a)):
    if b[i] != a[i]**2:
      return False
  return True

