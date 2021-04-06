
def pluralize(lst):
  x = set()
  for item in lst:
    if lst.count(item) > 1:
      x.add(item + "s")
    else:
      x.add(item)
  return x

