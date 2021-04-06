
def deadly_virus(group, n):
  if not n:
    return group
  r,c=len(group),len(group[0])
  p=list(list(0 for i in range(c)) for i in range(r))
  for i in range(r):
    for j in range(c):
      if group[i][j]=="V":
        p[i][j]+=1
        p[max([i-1,0])][j]+=1
        p[min([i+1,r-1])][j]+=1
        p[i][max([j-1,0])]+=1
        p[i][min([j+1,c-1])]+=1
  for i,x in enumerate(p):
    for j,y in enumerate(x):
      if y:
        p[i][j]="V"
      else:
        p[i][j]="P"
  return deadly_virus(p,n-1)

