
def clear_ordering(lst):
  l1=[]
  l3=[]
  for c in lst:
    c=tuple(c)
    l1.append(c)
  l2=zip(*l1)
  for i in l2:
    i=list(i)
    l3.append(i)
  x=len(set(l3[0]))
  return all(x==len(set(m)) for m in l3)

