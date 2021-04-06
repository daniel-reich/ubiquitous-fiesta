
def deepest(lst):
  depth = 1
  newlst = lst
  while True:
    lst = newlst
    newlst = []
    lst = list(filter(lambda x: isinstance(x,list),lst))
    if not lst:
      return depth
    else:
      depth += 1
      for el in lst:
        newlst.extend(el)

