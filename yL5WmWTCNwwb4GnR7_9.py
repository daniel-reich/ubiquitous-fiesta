
def return_unique(lst):
  nw = []
  for i in lst:
    if lst.count(i) == 1:
      nw.append(i)
  return nw

