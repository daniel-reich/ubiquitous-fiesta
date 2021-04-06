
def nPr(n,r) : 
  res = 1
  for i in range(n-(r-1),n+1):
    res *= i
  return res
​
def nCr(n, r):
  if r < (n-r) :return round(nPr(n,r)/fact(r))
  res = 1
  for i in range(r+1,n+1):
    res *= i
  return round(res/fact(n-r))
  
def fact(n): 
  return 1 if (n==1 or n==0) else n * fact(n - 1)

