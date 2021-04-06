
def hex_distance(grid):
  A=[]
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      if grid[i][j]=='x':
        A.append((i,j))
  s1,s2=abs(A[1][0]-A[0][0]), abs(A[1][1]-A[0][1])
  if s1==0:
    d=s2//2
  else:
    if s2//s1==1 or s2==0:
      d=s1
    else:
      d=s1+((s2-s1)//2 if s1<s2 else 0)
  return abs(d)

