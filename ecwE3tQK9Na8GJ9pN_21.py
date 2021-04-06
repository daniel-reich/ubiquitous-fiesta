
def little_big(n):
  l=[]
  for i,x in enumerate(range(5,6+n//2)):
    l+=[x,100*2**i]
  return l[n-1]

