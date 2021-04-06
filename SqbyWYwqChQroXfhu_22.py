
def lower_triang(arr):
  m=[]
  for i,x in enumerate(arr):
    n=[]
    for j,y in enumerate(x):
      if j>i:
        n+=[0]
      else:
        n+=[y]
    m+=[n]
  return m

