
def num_type(n):
  sum1=0
  sum2=0
  for i in range(1,n):
    if n%i==0:
      sum1=sum1+i
  if sum1==n:
    return 'Perfect'
  else:
    for x in range(1,sum1):
      if sum1%x==0:
        sum2=sum2+x
    if sum2==n:
      return 'Amicable'
    else:
      return 'Neither'

