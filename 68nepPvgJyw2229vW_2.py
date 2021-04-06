
asc=lambda x:sum(map(ord,str(x)))
def pairwise_swap(l):
  r=[i for s in zip(l[1::2],l[::2])for i in s]
  if len(l)&1:
    m=0,0
    for i,x in enumerate(r):
      s=asc(x)
      if s>m[0]:m=s,i
    if asc(l[-1])>m[0]:r.append(l[-1])
    else:r.append(r[m[1]]);r[m[1]]=l[-1]
  return r

