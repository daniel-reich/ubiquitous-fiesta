
def guess_score(c,g):
  r={'black':0,'white':0}
  for x in g:
    p=c.find(x)
    if-1<p:
      r[('white','black')[g[p]==x]]+=1
      c=c[:p]+'X'+c[p+1:]
  return r

