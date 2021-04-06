
def is_sorted(w,l):
  def cmp(s,t):
    for x,y in zip(s,t):
      a,b=l.find(x),l.find(y)
      if a<b:return 1
      if a>b:return 0
    return len(s)<=len(t)
  return all(cmp(i,j)for i,j in zip(w,w[1:]))

