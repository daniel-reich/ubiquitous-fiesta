
def alternate_sort(lst):
  newlist = zip(sorted(list(filter(lambda x: type(x) == int,lst))),sorted(list(filter(lambda x: type(x) == str,lst))))
  newlst = []
  for el in newlist:
    newlst.extend(el)
  return newlst

