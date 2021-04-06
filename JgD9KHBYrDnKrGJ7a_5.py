
def swap_dict(dic):
  A=[(y,x) for x,y in dic.items()]
  B=set([x[0] for x in A])
  d={x:[] for x in B}
  for x in A:
    for k in d:
      if x[0]==k:
        d[k].append(x[1])
  return d

