
def score31(c1, c2, c3):
  H=[c1,c2,c3]
  S=[x[0] for x in H]
  N=[]
  for x in H:
    if x[1:]=='A':
      N.append(11)
    elif x[1:] in 'JQK':
      N.append(10)
    else:
      N.append(int(x[1:]))
  if len(set(S))==1:
    if len(set(N))==1:
      if 11 in N:
        p=32
      else:
        p=30.5
    else:
      p=sum(N)
  elif len(set(S))==2:
    p=sum(x for x,y in zip(N,S) if S.count(y)==2)
  else:
    if len(set(N))==1:
      if 11 in N:
        p=32
      else:
        p=30.5
    else:
      p=max(N)
  return p

