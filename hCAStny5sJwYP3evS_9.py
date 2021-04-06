
def is_early_bird(_range, n):
  seq, early = "", False
  last = 0
  res = []
  for x in range(_range+1):
    seq += str(x)
    indexfound = seq.find(str(n), last)
    if indexfound != -1:
      last = indexfound + 1
      res += [[x+indexfound for x in range(len(str(n)))]]
      if x<n:
        early = True
  if early:
    res.append('Early Bird!')
  return res

