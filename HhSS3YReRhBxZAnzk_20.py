
def gen_values(n, i):
  if isinstance(i,float):
    l=[float(0)]
  else:
    l=[0]
  while l[-1]<n:
    l+=[round(l[-1]+i,2)]
  if l[-1]>n:
    return l[:-1]
  else: 
    return l

