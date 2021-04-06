
def break_point(n):
  l=list(map(int,str(n)))
  return any(sum(l[:i])==sum(l[i:])for i in range(len(l)))

