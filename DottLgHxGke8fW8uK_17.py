
def nPr(n, r):
  ans = 1
  for i in range(r):
    ans*= (n-i)
  return ans
​
def nCr(n, r):
  r = min(r,n-r)
  ans = nPr(n,r)
  for i in range(1,r+1):
    ans//= i
  return ans

