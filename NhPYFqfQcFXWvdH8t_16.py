
def mod_inv(n, m):
  ans=False
  mnew=m%n
  for i in range(1,n):
    if (mnew*i)%n==n-1:
      ans=int((m*i+1)/n)
      break
  return ans

