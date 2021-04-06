
def two_product(l, n):
  l=[i for i in l if i!=0]
  a=[i for i in l if n%i==0 and i!=1 and i!=-1]
  b=[i for i in a if n/i in a]
  if b==[]:
    return None
  else:
    return sorted(b)

