
def ulaml(n):
  if n==2:
    return [1,2],{3:1}
  lnml,lnmls=ulaml(n-1)
  nn=min([x for x in lnmls if x>lnml[-1] and lnmls[x]==1])
  l=lnml+[nn]
  for x in lnml:
    if nn+x in lnmls:
      lnmls[nn+x]+=1
    else:
      lnmls[nn+x]=1
  return l,lnmls
def ulam(n):
  return ulaml(n)[0][-1]

