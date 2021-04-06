
def semiprimes(n,p=[2]):
  m,s,r=max(p),[],[]
  while m<n//2:
    m+=1
    if all(m%q for q in p):p+=[m]
  for i in range(len(p)):
    for j in range(i,len(p)):
      if p[i]*p[j]<n: 
        s+=[p[i]*p[j]]
        if i!=j: r+=[s[-1]]
  return sorted(s),sorted(r)

