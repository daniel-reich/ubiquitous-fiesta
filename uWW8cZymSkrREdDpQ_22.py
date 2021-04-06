
def sums_up(lst):
  A=[]
  B=[]
  while lst:
    A.append(lst.pop(0))
    for x in A[:-1]:
      if A[-1]+x==8:
        B.append(sorted([A[-1],x]))
  d={}
  d['pairs']=B
  return d

