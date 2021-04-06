
from itertools import accumulate
def harry(po):
  if not po or not po[0]:
    return -1
  n,m = len(po),len(po[0])
  res = [[0] * m for _ in range(n)]
  res[0] = list(accumulate(po[0]))
  for i in range(1,n):
    res[i][0] = po[i][0]+res[i-1][0]
  for i in range(1,n):
    for j in range(1,m):
      res[i][j] = po[i][j]+(max(res[i-1][j],res[i][j-1]))
  return res[n-1][m-1]

