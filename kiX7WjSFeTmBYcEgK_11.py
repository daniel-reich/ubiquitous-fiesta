
def major_sum(l):
  p=sum([i for i in l if i>0])
  n=sum([i for i in l if i<0])
  z=[i for i in l if i==0].count(0)
  a=[p,n,z]
  if -(n)>p and -n>z:
    return n
  else:
    return max(p,z)

