
def ascii_sort(lst):
  l=[sum(c) for c in [list(map(lambda y:ord(y),list(x))) for x in lst]]
  return lst[l.index(min(l))]

