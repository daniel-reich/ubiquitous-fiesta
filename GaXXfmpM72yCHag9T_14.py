
def unique(lst):
  d, res = dict(), int(0)
  for i in lst:
    d[i] = d.get(i,0) + 1
  for x in d:
    if d[x] == 1:
      res = x
  return res

