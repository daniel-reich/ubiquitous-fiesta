
def is_isomorphic(s, t):
  A=[x for x in zip(s,t)]
  B=[]
  for x in A:
    if not B or not any(x[0]==y[0] for y in B):
      B.append(x)
  C=[x[::-1] for x in B]
  d1=dict(B)
  d2=dict(C)
  res1=''
  for x in s:
    res1+=d1[x]
  res2=''
  for x in t:
    res2+=d2[x]
  return res1==t and res2==s

