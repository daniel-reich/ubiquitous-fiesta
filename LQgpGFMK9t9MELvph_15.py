
def get_diagonals(lst):
  res=[[] , []]
  for i in range(len(lst)):
    res[0] += [lst[i][i]] 
    res[1] += [lst[i][-1-i]]
  return res

