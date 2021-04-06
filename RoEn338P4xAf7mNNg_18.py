
def shortest_path(lst):
  A=[]
  for i in range(len(lst)):
    for j in range(len(lst[0])):
      if lst[i][j]!='0':
        A.append([int(lst[i][j]), (i,j)])
  A=sorted(A)
  B=[x[1] for x in A]
  C=[x for x in zip(B, B[1:])]
  return sum([abs(x[0][0]-x[1][0])+abs(x[0][1]-x[1][1]) for x in C])

