
def pluralize(lst):
  list = set()
  for x in lst:
    if x not in list and x+"s" not in list:
      if lst.count(x) > 1:
        list.add(x+"s")
      else:
        list.add(x)
  return list

