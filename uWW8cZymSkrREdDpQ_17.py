
def sums_up(lst):
  res = [[n,8-n] for i,n in enumerate(lst) if 8-n in lst[i+1:]]
  res.sort(key=lambda x: lst.index(x[1]))
  return {'pairs':[sorted(pair) for pair in res]}

