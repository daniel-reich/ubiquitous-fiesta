
def tree(h):
  t=[]
  l=1+2*(h-1)
  for i in range(h):
    t+=[("#"*(1+2*i)).center(l)]
  return t

