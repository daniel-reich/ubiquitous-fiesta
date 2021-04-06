
def expensive_orders(d, k):
  new_dic = {}
  
  for key in d.keys():
    if d[key] > k:
      new_dic[key] = d[key]
  
  return new_dic

