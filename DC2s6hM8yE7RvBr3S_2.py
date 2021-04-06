
def subtract_matrix(lst1, lst2):
  l=[]
  for i in range(len(lst1)):
    sl=[]
    for x,y in zip(lst1[i],lst2[i]):
      if type(x)==str:
        x,y=map(int,[x,y])
      sl+=[x-y]
    l+=[sl]
  return l

