
def deadly_virus(p, n):
  A=[(i,j) for i in range(len(p)) for j in range(len(p[0]))]
  for _ in range(n):
    B=[]
    for i in range(len(p)):
      for j in range(len(p[0])):
        if p[i][j]=='V':
          for x in A:
            if (abs(i-x[0])==1 and x[1]==j) or (abs(j-x[1])==1 and x[0]==i):
              B.append(x)
    for x in B:
      p[x[0]][x[1]]='V'
  return p

