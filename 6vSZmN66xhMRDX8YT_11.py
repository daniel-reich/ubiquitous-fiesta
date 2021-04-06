
def advanced_sort(lst):
  d = dict()
  order = []
  items = set()
  for item in lst:
    d[item] = []
    if item not in items:
      order.append(item)
    items.add(item)
  
  for item in lst:
    d[item].append(item)
  
  lsts = []
  for key in order:
    lsts.append(d[key])
  return lsts

