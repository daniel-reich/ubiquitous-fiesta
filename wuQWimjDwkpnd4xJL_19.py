
def balanced(lst):
  m=len(lst)//2
  l1=lst[:m]
  l2=lst[m:]
  s1=sum(l1)
  s2=sum(l2)
  D={
    s1:l1,
    s2:l2
  }
  if s1==s2:
    return lst
  else:
    return D[max([s1,s2])]*2

