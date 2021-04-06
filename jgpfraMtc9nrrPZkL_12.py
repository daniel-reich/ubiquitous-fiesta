
def transform(lst):
  res = [[None for i in lst] for j in lst[0] ]
  for i,row in enumerate(res):
    for j,cell in enumerate(row):
      res[i][j] = lst[j][i]
  return res
  
def switch_gravity_on(lst):
  lst = transform(lst)
  res = []
  for row in lst:
    count = sum(map(lambda x: x== "#",row))
    row = ['-']*(len(row)-count) + ['#']*count
    res.append(row)
  return transform(res)

