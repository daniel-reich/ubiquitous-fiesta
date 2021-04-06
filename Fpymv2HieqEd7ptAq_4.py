
def split(a):
  u,s=0,0
  o=[]
  for i in range(len(a)):
    if a[i]=='(':
      u=u+1
    if a[i]==')':
      u=u-1
    if u == 0:
      o.append(a[s:i+1])
      s=i+1
  return(o)

