
def find_fulcrum(lst):
  l=lst
  n=len(l)
  pre=[0]*n
  suf=[0]*n
  pre[0]=l[0]
  suf[n-1]=l[n-1]
  for i in range(1,n,1):
    pre[i]=pre[i-1]+l[i]
  for j in range(n-2,-1,-1):
    suf[j]=suf[j+1]+l[j]
  for i in range(1,n,1):
    if pre[i]==suf[i]:
      return l[i]
  return -1

