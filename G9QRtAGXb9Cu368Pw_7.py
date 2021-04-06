
def combinations(*items):
  items=list(items)
  for i in items:
    if i==0:
      items.remove(i)
  count = 1
  for i in items:
    count*=i
  return count

