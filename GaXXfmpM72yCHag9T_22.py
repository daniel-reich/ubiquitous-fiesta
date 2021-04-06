
def unique(lst):
  dc = {}
  for x in lst:
    dc[x] = dc.get(x,0) + 1
  print(dc)
  for i in dc:
    if dc[i] == 1:
      return i

