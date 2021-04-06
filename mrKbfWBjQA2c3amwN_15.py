
def mult_table(n):
  l=[]
  for i in range(1,n+1):
    k=[]
    for j in range(1,n+1):
      k+=[i*j]
    l+=[k]
  return l

