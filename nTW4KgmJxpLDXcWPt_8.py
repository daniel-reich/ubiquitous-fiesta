
def move_to_end(lst, el):
  l = []
  r = []
  for e in lst:
    if e == el:
      r.append(e)
    else:
      l.append(e)
  l.extend(r)
  return l

