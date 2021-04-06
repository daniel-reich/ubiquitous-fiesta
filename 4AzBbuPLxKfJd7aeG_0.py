
def encrypt(k,m):
  d={}
  for x,y in zip(k[::2],k[1::2]):
    if x not in d:d[x]=y
    if y not in d:d[y]=x
  return''.join(d.get(x,x)for x in m)

