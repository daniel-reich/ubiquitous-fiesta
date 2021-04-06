
def sums_up(lst):
  res = {'pairs':[]}
  for i in range(len(lst)):
    for j in range(i):
      if lst[i]+lst[j]==8:
        res['pairs'].append(sorted([lst[i],lst[j]]))
  return res

