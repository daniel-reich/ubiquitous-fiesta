
def transform_matrix(lst):
  n = len(lst)
  m = len(lst[0])
  new = [[0]*m for _ in range(n)]
  for i in range(n):
    for j in range(m):
      new[i][j] = get_new(lst,i, j)
  return new
      
def get_new(lst, i, j):
  sum = 0
  for m in range(len(lst)):
    sum+=lst[m][j]
  for n in range(len(lst[0])):
    sum+=lst[i][n]
  if lst[i][j] == 1:
    sum-=2
  return sum

