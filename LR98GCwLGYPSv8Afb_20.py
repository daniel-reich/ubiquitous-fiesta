
def pluralize(lst):
  plurals = {}
  plurals = set()
  for i in lst:
    if lst.count(i)>1:
      plurals.add(i+"s")
    else:
      plurals.add(i)
  
  return plurals

