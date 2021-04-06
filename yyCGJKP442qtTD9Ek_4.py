
def sums_of_powers_of_two(n):
  p2=[2**i for i in range(30)]
  l=[]
  while n>0:
    m=min(p2,key=lambda x:n-x if x<=n else 2**29)
    l.append(m)
    n-=m
  return sorted(l)

