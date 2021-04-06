
def concatenation_sum(n):
  m,d,ans=9,1,0
  while n>0:
    if n-m>=0:
      ans+=d*m
    else:
      ans+=d*n
    n-=m
    d+=1
    m*=10
  return ans

