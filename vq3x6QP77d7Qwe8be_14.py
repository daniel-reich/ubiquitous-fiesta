
def odd_square_patch(lst):
  p=len(lst)
  q=len(lst[0])
  r=min(p,q)
  for i in range(p):
    for j in range(q):
      if lst[i][j]%2==1:
        lst[i][j]=1  
  if p==1 and 1 in lst[0]:
    return 1
  for x in range(r,0,-1):
    ans=''
    for y in range(p):
      sy=''.join(str(b) for b in lst[y])
      if '1'*x in sy:
        ans+=str(x)
      else:
        ans+='0'
    if str(x)*x in ans:
      return x
  return 0

