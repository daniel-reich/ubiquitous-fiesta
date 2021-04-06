
def harry(po):
  if po[0]:
    m,n=len(po), len(po[0])
    a=sum(po[0])+sum([x[-1] for x in po[1:]])
    b=sum([x[0] for x in po[:-1]])+sum(po[-1])
    return max(a,b)
  else:
    return -1

