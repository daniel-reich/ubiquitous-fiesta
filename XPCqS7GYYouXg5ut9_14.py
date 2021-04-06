
def simplify_sqrt(n):
  pos = range(1,int(n**0.5)+1)
  ans = []
  for i in pos:
    j = n/(i**2)
    if (i**2)*j==n and n%(i**2)==0:
      ans.append([i,j])
  if ans==[]:
    return (1, n)
  else:
    ans.sort(key=lambda x: x[1])
    return (ans[0][0], ans[0][1])

