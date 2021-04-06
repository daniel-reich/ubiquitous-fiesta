
def num_type(n):
  s=sum([i for i in range(1,n) if n%i==0])
  if s==n: return 'Perfect'
  if sum([i for i in range(1,s) if s%i==0])==n:return 'Amicable'
  return 'Neither'

