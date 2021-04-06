
def combine(lst):
  d = {}
  for i,c,f in lst:
    if i not in d:
      d[i] = [f]
    else:
      d[i].append(f)
  return d

