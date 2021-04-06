
def crop_hydrated(field):
  n,m = len(field), len(field[0])
  pos = {}
  for t in ['w','c']:
    pos[t] = {(i,j) for i in range(n) for j in range(m) if field[i][j] == t}
  dirs = {(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)}
  
  return all(any((a+i,b+j) in pos['w'] for (i,j) in dirs) for (a,b) in pos['c'])

