
def can_fit(weights, bags):
  if sum(weights)>bags*10:
    return False
  else:
    while weights:
      n=len(weights)
      r=[[]]
      for i in range(n):
        for j in range(len(r)):
          if sum(r[j]+[weights[i]])<=10:
            r.append(r[j]+[weights[i]])
      r=sorted(r,key=lambda x:sum(x))
      for i in r[-1]:
        weights.remove(i)
      bags-=1
    return bags>=0

