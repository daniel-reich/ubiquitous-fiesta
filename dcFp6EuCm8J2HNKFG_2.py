
def func(lst):
  count = len(lst)
  newlst = []
  for el in lst:
    if isinstance(el,list):
      newlst.extend(el)
  if not newlst:
    return count
  else:
    return func(newlst) + count

