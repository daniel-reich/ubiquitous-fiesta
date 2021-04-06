
def remove_dups(lst):
  res = []
  for l in lst:
    if l not in res:
      res.append(l)
  return res

