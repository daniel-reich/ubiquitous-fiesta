
def combinations(*items):
  if isinstance(items,int):return items
  l=list(items)
  if 0 in l:l.remove(0)
  return eval(str(l).replace(",","*"))[0]

