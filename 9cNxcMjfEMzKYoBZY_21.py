
def num_type(n):
  l=sum([i for i in range(1,n) if n%i==0])
  if l==n: return 'Perfect'
  k=sum([i for i in range(1,l) if l%i==0])
  return 'Amicable' if k==n else 'Neither'

