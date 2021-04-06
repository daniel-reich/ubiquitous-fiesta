
def transpose_matrix(lst):
  m = len(lst)
  n = len(lst[0])
  res = [[0]*m for i in range(n)] 
  for i in range(n):
    for j in range(m):
      res[i][j]=lst[j][i]
  return res

