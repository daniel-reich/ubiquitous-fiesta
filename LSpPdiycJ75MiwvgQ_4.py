
def grid_pos(lst):
  res = [[1]*(lst[0]+1)]*(lst[1]+1)
  for i in range(1,len(res)):
    for j in range(1,len(res[0])):
      res[i][j] = res[i-1][j]+res[i][j-1]
  return res[-1][-1]

