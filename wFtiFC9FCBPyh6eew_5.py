
def partitions(n):
  def p(n,k):
    if k==1:
      return 1
    elif n<k:
      return 0
    elif n==k:
      return 1
    else:
      return p(n-1,k-1)+p(n-k,k)
  ans=1
  for i in range(1,n):
    ans=ans+p(n,i)
  return ans

