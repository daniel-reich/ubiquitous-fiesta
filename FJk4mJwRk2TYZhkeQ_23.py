
def accum(txt):
  newlst = []
  n = 1
  for char in txt:
    newlst.append(char * n)
    n += 1
  for entry in newlst:
    newlst[newlst.index(entry)] = entry.title()
  return '-'.join(newlst)

