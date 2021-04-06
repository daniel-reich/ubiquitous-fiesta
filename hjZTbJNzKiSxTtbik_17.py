
def sort_by_string(lst, txt):
  fsts = []
  for el in lst:
    fsts.append(el[0])
  l = list(txt)
  for let in l:
    if let not in fsts:
      l.remove(let)
  res = []
  for f in l:
    for w in lst:
      if w[0] == f:
        res.append(w)
  return res

