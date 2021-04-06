
def num_type(n):
  s=sum([i for i in range(1,n) if n%i==0 ])
  if s==n:
    return('Perfect')
  else:
    ss=sum([i for i in range(1,s) if s%i==0])
    if ss==n:
      return('Amicable')
    else:
      return('Neither')

