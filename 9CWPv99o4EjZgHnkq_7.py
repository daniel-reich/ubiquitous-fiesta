
def divide(lst, n):
  c,fl=0,[]
  while c<len(lst): 
    l=[]
    for d,i in enumerate(lst[c:]):
      if sum(l)+i>n:c+=len(l); break
      if d+c+1==len(lst):l=lst[c:]; c=len(lst); break
      l.append(i)
    fl.append(l)
  return fl

