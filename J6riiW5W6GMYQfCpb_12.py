
def expensive_orders(d, k):
  dict = {}
  for item in d.keys():
    if d[item]>k:
      dict[item] = d[item]
  return dict

