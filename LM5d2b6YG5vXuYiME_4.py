
def can_enter_cave(x):
  n,m = len(x),len(x[0])
  coord = [(i,j) for i in range(n) for j in range(m)]
  q, v = [(i,0) for i in range(len(x)) if x[i][0] == 0], []
  while q:
    e = q.pop()
    v.append(e)
    if e[1] == m-1:
      return True
    for k,l in [(0,1),(1,0),(-1,0),(0,-1)]:
      p = (e[0]+k,e[1]+l)
      if p in coord and x[p[0]][p[1]] == 0 and p not in v:
        q.append(p)
  return False

