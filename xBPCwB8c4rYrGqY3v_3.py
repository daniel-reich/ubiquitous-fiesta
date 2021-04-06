
def missing(lst):
  lst2=[]
  a=min(lst[1]-lst[0],lst[-1]-lst[-2])
  for i in range(len(lst)-1):
    if lst[i+1]-lst[i]!=a:
      return lst[i]+a

