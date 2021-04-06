
def swap_dict(dic):
  nd = {}
  for k in dic.keys():
    v = dic[k]
    if v not in nd.keys():
      nd[v] = [k]
    else:
      nd[v].append(k)
  return nd

