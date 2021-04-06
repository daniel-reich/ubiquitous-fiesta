
def can_complete(i,w):
  p=[]
  for x in i:
    y=w.find(x)
    if y>-1:
      p.append(y)
      w=w.replace(x,'')
    else:
      return 0
  return p==sorted(p)

