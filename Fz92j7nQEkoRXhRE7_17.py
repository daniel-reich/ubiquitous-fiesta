
def jumping_frog(n, stns):
  def update(d,stlst):
    sortlst = sorted(stlst, key = lambda x: d[x])
    j = sortlst[0]
    if d[j] > n:
      return "no chance :-("
    if stns[j]+j >= n:
      return d[j]+1
    d[stns[j]+j] = min(d[stns[j]+j],d[j]+1)
    if j-stns[j] >=0:
      d[j-stns[j]] = min(d[j-stns[j]],d[j]+1)
    return update(d,sortlst[1:])
    
  d = {i:(n+1) for i in range(1,n)}
  d[0] = 1
  return update(d,[i for i in range(n)])

