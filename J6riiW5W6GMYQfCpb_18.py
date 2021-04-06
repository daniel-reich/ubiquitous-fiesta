
def expensive_orders(d, k):
  res={}
  for tag,val in d.items():
    if val>k:
      res[tag] = val
  return res

