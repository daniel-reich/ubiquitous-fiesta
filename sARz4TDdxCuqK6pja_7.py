
def deadly_virus(persons, n):
  dirs = [(1,0),(0,1),(-1,0),(0,-1)]
  lp,lp0 = len(persons),len(persons[0])
  for _ in range(n):
    pos = [(i,j) for i in range(lp) for j in range(lp0) if persons[i][j] == 'V']
    for x,y in pos:
      for k,l in dirs:
        if 0<=x+k<lp and 0<=y+l<lp0:
          persons[x+k][y+l] = 'V'
  return persons

