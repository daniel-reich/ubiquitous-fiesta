
def ascending(t):
  l=len(t)
  for i in range(l,1,-1):
    k=[int(t[j:j+l//i])for j in range(0,l,l//i)]
    if k and all(y-x==1 for x,y in zip(k,k[1:])):return 1
  return 0

