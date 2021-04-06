
def is_wristband(lst):
  n,m = len(lst),len(lst[0])
  dic = {(i,j):lst[i][j] for j in range(m) for i in range(n)}
  
  dirs = [(1,0),(0,1),(1,1),(1,-1)]
  
  return any(all(len(set(dic[(i+r*k,j+r*l)] for r in range(max(n,m)+2) if (i+r*k,j+r*l) in dic))==1 for (i,j) in dic) for (k,l) in dirs)

