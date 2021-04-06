
def swap_dict(dct):
  res = {}
  
  for k, v in dct.items():
    if v not in res:
      res[v] = [k]
    else:
      res[v].append(k)
      
  return res

