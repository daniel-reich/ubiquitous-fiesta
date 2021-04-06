
def min_length(lst, n):
  r=[]
  l=[[r.append(len(lst[i:h])) for h in range(len(lst),1,-1) if sum(lst[i:h])>n] for i in range(len(lst)-1)]
  return -1 if len(r)==0 else min(r)

