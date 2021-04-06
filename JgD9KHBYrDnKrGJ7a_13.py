
def swap_dict(dic):
  res = {}
  for v,k in dic.items():
    res[k] = res.get(k,[])+[v]
  return res

