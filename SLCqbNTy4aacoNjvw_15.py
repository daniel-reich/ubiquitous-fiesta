
def remove_dups(lst):
  r = []
  for l in lst:
    if l not in r:
      r.append(l)
  return r

