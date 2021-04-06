
def multiplicity(lst):
  r=[]
  while len(lst):
    x = lst[0]
    r.append([x, lst.count(x)])
    while x in lst:
     lst.remove(x)
  return r

