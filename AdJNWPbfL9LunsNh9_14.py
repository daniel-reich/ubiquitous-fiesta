
def multiplication_table(n):
  ans=[]
  for i in range(1,n+1):
    a=[]
    for j in range(1,n+1):a.append(i*j)
    ans.append(a)
  return ans

