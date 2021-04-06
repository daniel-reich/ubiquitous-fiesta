
def antipodes_average(lst):
  m = len(lst)//2
  res = [0]*m
  for i in range(m):
    res[i] = (lst[i] + lst[-i-1])/2
  return res

